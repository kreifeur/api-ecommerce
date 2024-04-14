# Generated by Django 4.2.7 on 2023-11-18 20:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('yourappname', '0004_rename_places_product_old'),
    ]

    operations = [
        migrations.CreateModel(
            name='Color',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Size',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.RenameField(
            model_name='product',
            old_name='price',
            new_name='newprice',
        ),
        migrations.RenameField(
            model_name='product',
            old_name='old',
            new_name='oldprice',
        ),
        migrations.AddField(
            model_name='product',
            name='category',
            field=models.CharField(default='', max_length=255),
        ),
        migrations.AddField(
            model_name='product',
            name='subcategory',
            field=models.CharField(default='', max_length=255),
        ),
        migrations.AddField(
            model_name='product',
            name='colors',
            field=models.ManyToManyField(to='yourappname.color'),
        ),
        migrations.AddField(
            model_name='product',
            name='sizes',
            field=models.ManyToManyField(to='yourappname.size'),
        ),
    ]