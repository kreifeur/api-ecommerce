# Generated by Django 4.2.7 on 2023-11-18 18:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('yourappname', '0002_product_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='places',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10),
        ),
    ]