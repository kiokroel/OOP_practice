from django.contrib.auth import logout
from django.contrib.auth.views import LoginView
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, JsonResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView
from .models import *
from .forms import RegisterUserForm, LoginUserForm


def index(request):
    return render(request, "base.html")


class Main(ListView):
    model = Product
    template_name = "main.html"
    context_object_name = "product"

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = "Главная страница"
        return context

    def get_queryset(self):
        return Product.objects.filter()


class Catalog(ListView):
    model = Product
    template_name = "main.html"
    context_object_name = "product"

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = "Главная страница"
        return context

    def get_queryset(self, ):
        return Product.objects.filter()


def check_products(request):
    return HttpResponse("Каталог")


def buy_product(request, id_product):
    return HttpResponse("Покупка")


def check_cart(request):
    if not request.user.is_authenticated:
        return redirect('login')
    user_id = request.user.id
    cart = Cart.objects.filter(user_id=user_id)
    if not cart:
        Cart.objects.create(user=request.user)
        return render(request, 'cart.html')
    cart_id = cart[0].id
    products = CartProduct.objects.filter(cart_id=cart_id)
    products_count = dict()
    for prod in products:
        if prod.product_id in products_count.keys():
            products_count[prod.product_id] += 1
        else:
            products_count[prod.product_id] = 1
    products_count = products_count.items()
    products_list = list()
    total_price = 0
    for prod_id, prod_count in products_count:
        prod = Product.objects.filter(id=prod_id)[0]
        prod.count = prod_count
        total_price += prod.price
        prod.price_all = prod_count * prod.price
        products_list.append(prod)
    context = {
        'products': products_list,
        'total_price': total_price,
    }
    return render(request, 'cart.html', context=context)


def delete_from_cart(request, product_id):
    if not request.user.is_authenticated:
        return redirect('login')
    user_id = request.user.id
    cart = Cart.objects.filter(user_id=user_id)[0]
    cart_id = cart.id
    CartProduct.objects.filter(cart_id=cart_id, product_id=product_id)[0].delete()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


def add_to_cart(request, product_id):
    if not request.user.is_authenticated:
        return redirect('login')
    user_id = request.user.id
    cart = Cart.objects.filter(user_id=user_id)[0]
    CartProduct.objects.create(cart=cart, product_id=product_id)
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


def check_purchase_history(request):
    user_id = request.user.id
    cart = Cart.objects.filter(user_id=user_id)
    if not cart:
        Cart.objects.create(user=request.user)
    cart = Cart.objects.filter(user_id=user_id)
    cart_id = cart[0].id
    purchased_goods = SoldProducts.objects.filter(cart_id=cart_id)
    for i in range(len(purchased_goods)):
        purchased_goods[i].name = Product.objects.filter(id=purchased_goods[i].product_id)[0]
    context = {
        'products': purchased_goods,
    }
    return render(request, 'purchase_history.html', context=context)


def buy_products(request):
    user_id = request.user.id
    cart = Cart.objects.filter(user_id=user_id)
    if not cart:
        Cart.objects.create(user=request.user)
        return redirect('cart')
    cart_id = cart[0].id
    cart_product = CartProduct.objects.filter(cart_id=cart_id)
    for i in range(len(cart_product)):
        product_id = cart_product[i].product_id
        product_count = CountProduct.objects.filter(product_id=product_id)
        if product_count and product_count[0].count > 0:
            count = product_count[0].count - 1
            product_count.update(count=count)
            cart_product[i].delete()
            SoldProducts.objects.create(cart_id=cart_id, product_id=product_id)

    return redirect('purchase_history')


class RegisterUser(CreateView):
    form_class = RegisterUserForm
    template_name = "registration.html"
    success_url = reverse_lazy('login')


class LoginUser(LoginView):
    form_class = LoginUserForm
    template_name = "login.html"


def logout_user(request):
    logout(request)
    return redirect("/login")


def user_profile(request):
    if not request.user.is_authenticated:
        return redirect('login')
    user = request.user
    context = {
        'username': user.username,
        'email': user.email,
        'date_joined': user.date_joined,
    }
    return render(request, "user_profile.html", context=context)


def show_product(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    images = ProductPhoto.objects.filter(product_id=product_id)
    context = {
        'product': product,
        'name': product.name,
        'description': product.description,
        'price': product.price,
    }
    if images:
        context['images'] = images
    return render(request, "product.html", context=context)


def pageNotFound(request, exception):
    return HttpResponseNotFound("<h1>Страница не найдена</h1>")
