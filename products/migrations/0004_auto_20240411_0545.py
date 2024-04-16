# Generated by Django 3.2.25 on 2024-04-11 05:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_auto_20240405_2241'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='sku',
        ),
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ImageField(default='default_image.jpg', upload_to='product_images'),
        ),
    ]