from django.http import HttpResponse
from django.shortcuts import render

from .models import Product

# Create your views here.

def homepage(request):
    return render(request, 'index.html')

def about_page(request, id=0):
    content = f"<p>Here is Author No {id}'s about page</p>"
    return HttpResponse(content)

def list_page(request):
    table = "<table border='1'>"
    table += "<tr><th>Product Number</th><th>Product Name</th><th>Price</th><th>Size</th></tr>"
    products = Product.objects.all()
    for product in products:
        table += f"<tr><td>{product.item_number}</td><td>{product.brand_name}</td><td>{product.price}</td><td>{product.size}</td></tr>"
    table += "</table>"
    return HttpResponse(table)

def budget_page(request, id=7112029088, name='xxx', age=15, budget=1000):
    content = f"<h1>大家好, 我是{name}</h1>"
    content += f"<p>我的學號: {id}</p>"
    content += f"<p>我的年齡: {age}</p>"
    content += f"<p>我的預算有: {budget}</p>"
    content += "<hr>"
    table = "<table border='1'>"
    table += "<tr><th>Product Number</th><th>Product Name</th><th>Price</th><th>Size</th></tr>"
    products = Product.objects.all()
    for product in products:
        if product.price <= budget:
            table += f"<tr><td>{product.item_number}</td><td>{product.brand_name}</td><td>{product.price}</td><td>{product.size}</td></tr>"
    table += "</table>"
    return HttpResponse(content + table)