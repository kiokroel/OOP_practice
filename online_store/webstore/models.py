from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse


class Product(models.Model):
    name = models.TextField(verbose_name='Название')
    description = models.TextField(verbose_name="Описание")
    price = models.FloatField(verbose_name='Цена')

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('product', kwargs={'product_id': self.pk})

    class Meta:
        verbose_name = "Товар"
        verbose_name_plural = "Товары"
        ordering = ['id']


def directory_path(instance, filename):
    return 'images/{0}/{1}'.format(instance.product, filename)


class ProductPhoto(models.Model):
    url = models.ImageField(upload_to=directory_path)
    product = models.ForeignKey('Product', on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Фотографию"
        verbose_name_plural = "Фотографии"


class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)


class CartProduct(models.Model):
    cart = models.ForeignKey('Cart', on_delete=models.CASCADE)
    product = models.ForeignKey('Product', on_delete=models.CASCADE)

    class Meta:
        ordering = ['cart_id', 'product_id']


class CountProduct(models.Model):
    product = models.ForeignKey('Product', on_delete=models.CASCADE)
    count = models.PositiveIntegerField()
    place = models.TextField()

    class Meta:
        verbose_name = 'Количество товаров'
        verbose_name_plural = 'Количество товаров'
        ordering = ['product_id', 'count']
