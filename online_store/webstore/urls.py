from django.urls import path, include
from webstore import views
from online_store import settings
from django.conf.urls.static import static


user_patterns = [
    path('', views.user_profile, name='user_profile'),
    path('cart', views.check_cart, name='cart'),
    path('cart/delete/<int:product_id>', views.delete_from_cart, name='cart_delete'),
    path('cart/add/<int:product_id>', views.add_to_cart, name='cart_add'),
    path('purchase_history', views.check_purchase_history, name='purchase_history'),
    path('card/buy', views.buy_products, name='buy_products'),
]

urlpatterns = [
    path("product/<int:product_id>/", views.show_product, name='product'),
    path("user/", include(user_patterns)),
    path("register", views.RegisterUser.as_view(), name='reg'),
    path("login", views.LoginUser.as_view(), name='login'),
    path("logout", views.logout_user, name='logout'),
    path("", views.Main.as_view(), name='main'),
    path('catalog', views.check_products, name='catalog'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
