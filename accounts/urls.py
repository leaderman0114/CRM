from django.urls import path
from .views import *

urlpatterns = [
    path('', home),
    path('products/', products, name='products'),
    path('customers/', customers, name='customers'),
]
