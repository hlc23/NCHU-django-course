import datetime
from django.http import HttpResponse
from django.shortcuts import render

from .models import Product

# Create your views here.


def homepage(request):
    return render(request, "index.html")


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


def budget_page(request, id=7112029088, name="xxx", age=15, budget=1000):
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


def index(req, tvno=0):
    tv_list = [
        {"name": "三立", "tvcode": "IBSOYl8GP2Q"},
        {"name": "中視", "tvcode": "TCnaIE_SAtM"},
        {"name": "中天", "tvcode": "vr3XyVCR4T0"},
        {"name": "民視", "tvcode": "ylYJSBUgaMA"},
    ]

    now = datetime.datetime.now()
    tv = tv_list[tvno]

    return render(req, "index.html", locals())


def carlist(req, maker=0):
    tv_list = [
        {"name": "三立", "tvcode": "IBSOYl8GP2Q"},
        {"name": "中視", "tvcode": "TCnaIE_SAtM"},
        {"name": "中天", "tvcode": "vr3XyVCR4T0"},
        {"name": "民視", "tvcode": "ylYJSBUgaMA"},
    ]
    car_maker = ["SAAB", "Ford", "Honda", "Mazda", "Nissan", "Toyota"]
    car_list = [
        [],
        ["Fiesta", "Focus", "Modeo", "EcoSport", "Kuga", "Mustang"],
        ["Fit", "Odyssey", "CR-V", "City", "NSX"],
        ["Mazda3", "Mazda5", "Mazda6", "CX-3", "CX-5", "MX-5"],
        ["Tida", "March", "Livina", "Sentra", "Teana", "X-Trail", "Juke", "Murano"],
        ["Camry", "Altis", "Yaris", "86", "Prius", "Vios", "RAV4", "Wish"],
    ]

    maker_name = car_maker[maker]
    cars = car_list[maker]
    return render(req, "carlist.html", locals())