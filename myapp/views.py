from django.shortcuts import render
from django.http import HttpResponse
from .models import Product

# Create your views here.

def fetch_products(request):
    products_list = Product.objects.all()

    context = {'products': products_list}

    return render(request, 'index.html', context)

def home(request):
    obj = Product(
        code = '001', 
        name = 'Product 1', 
        price = 100, 
        quantity = 10, 
        description = 'This is a product'
        )
    obj.save()
    return render(request, 'index.html')

def contact(request):
    return render(request, 'contact.html')


def about(request):
    return render(request, 'about.html')

def test(request):
    obj = Product(
        code = '001', 
        name = 'Product 1', 
        price = 100, 
        quantity = 10, 
        description = 'This is a product'
        )
    obj.save()
    return HttpResponse("Hello, test. You're at the Test page.")

