from django.contrib import admin
from .models import Product, ProductPhoto, Cart, CartProduct,  CountProduct


class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'description', 'price')
    list_display_links = ('id', 'name')
    search_fields = ('name', 'description')


class ProductPhotoAdmin(admin.ModelAdmin):
    list_display = ('id', 'url')
    list_display_links = ('id', 'url')
    search_fields = ('id', )


class CartProductAdmin(admin.ModelAdmin):
    list_display = ('cart_id', 'product_id')
    list_display_links = ('cart_id', 'product_id')
    search_fields = ('cart_id', 'product_id')


class CountProductAdmin(admin.ModelAdmin):
    list_display = ('product_id', 'count', 'place')
    list_display_links = ('count',)
    search_fields = ('product_id', 'place')


admin.site.register(Product, ProductAdmin)
admin.site.register(ProductPhoto, ProductPhotoAdmin)
admin.site.register(Cart)
admin.site.register(CartProduct, CartProductAdmin)
admin.site.register(CountProduct, CountProductAdmin)
