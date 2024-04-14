from django.contrib import admin
from .models import Product , Order ,Color,Size , ProductColor,ProductSize
# Register your models here.
admin.site.register(Product)
admin.site.register(Color)
admin.site.register(Size)
admin.site.register(Order)
admin.site.register(ProductColor)
admin.site.register(ProductSize)