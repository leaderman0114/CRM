from functools import total_ordering
from django.shortcuts import render
from .models import Customer, Order, Products


def home(request):
    orders = Order.objects.all()
    customers = Customer.objects.all()
    total_customers = customers.count()
    total_orders = orders.count()
    delivered = orders.filter(status='Delivered').count()
    pending = orders.filter(status='Pending').count()

    context = {
        'orders': orders,
        'customers': customers,
        'total_customers': total_customers,
        'total_orders': total_orders,
        'delivered': delivered,
        'pending': pending
    }
    return render(request, 'accounts/dashboard.html', context)

def products(request):
    products = Products.objects.all()
    return render(request, 'accounts/products.html', {'products': products})

def customers(request, pk):
    customer = Customer.objects.get(id=pk)
    orders = customer.order_set.all()
    order_count = orders.count()
    context = {
        'customer': customer,
        'orders': orders,
        'order_count': order_count,
    }
    return render(request, 'accounts/customers.html',context)