# serializers.py
from rest_framework import serializers
from .models import Product, Order ,Color , Size , Message


class ColorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Color
        fields = '__all__'

class SizeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Size
        fields = '__all__'


class ProductSerializer(serializers.ModelSerializer):
    """ colors = ColorSerializer(many=True, read_only=True)
    sizes = SizeSerializer(many=True, read_only=True) """
    class Meta:
        model = Product
        fields = ['id','name','category','subcategory','description','newprice','oldprice','image','colors','sizes']
        depth=2


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = '__all__' 

""" class OrderSerializer(serializers.ModelSerializer):
    products = ProductSerializer(many=True, read_only=True)

    class Meta:
        model = Order
        fields = '__all__' """



class MessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = '__all__' 