from django.urls import path
from .views import *

urlpatterns = [
    path('', home, name='home'),
    path('products/', products, name='products'),
    path('customers/<int:pk>/', customers, name='customers'),

    path('create_order/<int:pk>/', create_order, name='create_order'),
    path('update_order/<int:pk>/', update_order, name='update_order'),
    path('delete_order/<int:pk>/', delete_order, name='delete_order'),
]
