# Generated by Django 5.1.7 on 2025-03-11 19:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0003_alter_product_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='product_images/'),
        ),
    ]
