# views.py
from django.http import HttpResponse
from rest_framework import generics
from .models import Product, Order
from .serializers import ProductSerializer, OrderSerializer 
from django.shortcuts import get_object_or_404 ,render
from rest_framework.response import Response 
from rest_framework.views import APIView
from rest_framework import status
from .models import Order
from .serializers import OrderSerializer
from .models import Color, Size , ProductColor , ProductSize , Message
from .serializers import ColorSerializer, SizeSerializer , MessageSerializer
from rest_framework.decorators import api_view

class ColorListView(generics.ListAPIView):
    queryset = Color.objects.all()
    serializer_class = ColorSerializer

class ColorDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Color.objects.all()
    serializer_class = ColorSerializer

class SizeListView(generics.ListAPIView):
    queryset = Size.objects.all()
    serializer_class = SizeSerializer

class SizeDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Size.objects.all()
    serializer_class = SizeSerializer

class OrderListCreateView(generics.ListCreateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

class OrderDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

    
# a modifier le seialiser
class SubView(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        category_name = self.request.query_params.get('category', None)

        if category_name:
            queryset = queryset.filter(category=category_name)
            values = list(set(queryset.values_list('subcategory', flat=True)))
            # Assuming 'subcategory' is the field you want to extract values from
            return Response({'subcategories': values})

        return super().list(request, *args, **kwargs)

       
    
    def perform_create(self, serializer):
        serializer.save()


class ProductListCreateView(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def get_queryset(self):
        category_name = self.request.query_params.get('category', None)
        color_name = self.request.query_params.get('color', None)
        subcategory_name = self.request.query_params.get('subcategory', None)
        min_price = self.request.query_params.get('min', None)
        max_price = self.request.query_params.get('max', None)
        queryset = Product.objects.all()

        if category_name:
            queryset = queryset.filter(category=category_name)

        if color_name:
            queryset = queryset.filter(colors = color_name)

        if subcategory_name:
            queryset = queryset.filter(subcategory = subcategory_name)

        if min_price:
            queryset = queryset.filter(newprice__gt=min_price)

        if max_price:
            queryset = queryset.filter(newprice__lt=max_price)

        return queryset

       
    
    """ def perform_create(self, serializer):
        serializer.save() """

""" class ProductDetailView(APIView):
    def get(self, request, pk):
        product = get_object_or_404(Product, pk=pk)
        serializer = ProductSerializer(product)
        return Response(serializer.data, status=status.HTTP_200_OK) """
class ProductDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class OrderListCreateView(generics.ListCreateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer



@api_view(['POST','GET'])
def add(request , methods=['POST','GET']):
    if request.method=='POST':
        data ={
        'category':request.data['category'],
        'description':request.data['description'],
        'subcategory':request.data['subcategory'],
        'newprice':request.data['newprice'],
        'oldprice':request.data['oldprice'],
        'image':request.data['image'],
        'name': request.data['name']
        }

        serializer=ProductSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
        product = Product.objects.get(pk = list(serializer.data.values())[0])
        colors =request.data['colors']
        colors= colors.replace(',','')
        for col in colors:
            color = Color.objects.get(pk=col)
            product_color = ProductColor()
            product_color.products = product
            product_color.colors = color
            product_color.save()


        sizes =request.data['sizes']
        sizes= sizes.replace(',','')
        for siz in sizes:
            size = Size.objects.get(pk=siz)
            product_size = ProductSize()
            product_size.products = product
            product_size.sizes = size
            product_size.save()

        return HttpResponse({
            'text':'post',
            'data' : 'pp'
        })
    


class MessageListCreateView(generics.ListCreateAPIView):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer