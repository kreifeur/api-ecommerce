# urls.py
from django.urls import path
from .views import ProductListCreateView, OrderListCreateView, ProductDetailView ,SubView,ColorListView,SizeListView,ColorDetailView,SizeDetailView , MessageListCreateView
from .views import OrderListCreateView, OrderDetailView ,add


urlpatterns = [
    path('products/', ProductListCreateView.as_view(), name='product-list-create'),
    path('products/<int:pk>/', ProductDetailView.as_view(), name='product-detail-api'),
    path('orders/', OrderListCreateView.as_view(), name='order-list-create-api'),
    path('orders/<int:pk>/', OrderDetailView.as_view(), name='order-detail-api'),
    path('category/', SubView.as_view(), name='sub'),
    path('colors/', ColorListView.as_view(), name='color-list-api'),
    path('colors/<int:pk>/', ColorDetailView.as_view(), name='color-detail-api'),
    path('sizes/', SizeListView.as_view(), name='size-list-api'),
    path('sizes/<int:pk>/', SizeDetailView.as_view(), name='size-detail-api'),
    path('messages/', MessageListCreateView.as_view(), name='message-list-api'),
    path('add/', add, name='adminadd-api'), 
]
