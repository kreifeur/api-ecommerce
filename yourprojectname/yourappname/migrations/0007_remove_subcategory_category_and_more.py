# Generated by Django 4.2.7 on 2023-11-20 15:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('yourappname', '0006_category_rename_newprice_product_price_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='subcategory',
            name='category',
        ),
        migrations.RenameField(
            model_name='product',
            old_name='price',
            new_name='newprice',
        ),
        migrations.AddField(
            model_name='product',
            name='category',
            field=models.CharField(default='', max_length=255),
        ),
        migrations.AddField(
            model_name='product',
            name='image',
            field=models.ImageField(null=True, upload_to='product_images/'),
        ),
        migrations.AddField(
            model_name='product',
            name='oldprice',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10),
        ),
        migrations.AlterField(
            model_name='product',
            name='subcategory',
            field=models.CharField(default='', max_length=255),
        ),
        migrations.DeleteModel(
            name='Category',
        ),
        migrations.DeleteModel(
            name='Subcategory',
        ),
    ]