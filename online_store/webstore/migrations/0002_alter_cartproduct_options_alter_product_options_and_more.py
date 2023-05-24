# Generated by Django 4.2.1 on 2023-05-24 16:18

from django.db import migrations, models
import webstore.models


class Migration(migrations.Migration):

    dependencies = [
        ('webstore', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='cartproduct',
            options={'ordering': ['cart_id', 'product_id']},
        ),
        migrations.AlterModelOptions(
            name='product',
            options={'ordering': ['id'], 'verbose_name': 'Товар', 'verbose_name_plural': 'Товары'},
        ),
        migrations.AlterModelOptions(
            name='productphoto',
            options={'verbose_name': 'Фотографию', 'verbose_name_plural': 'Фотографии'},
        ),
        migrations.AlterField(
            model_name='product',
            name='description',
            field=models.TextField(verbose_name='Описание'),
        ),
        migrations.AlterField(
            model_name='product',
            name='name',
            field=models.TextField(verbose_name='Название'),
        ),
        migrations.AlterField(
            model_name='product',
            name='price',
            field=models.FloatField(verbose_name='Цена'),
        ),
        migrations.AlterField(
            model_name='productphoto',
            name='url',
            field=models.ImageField(upload_to=webstore.models.directory_path),
        ),
    ]