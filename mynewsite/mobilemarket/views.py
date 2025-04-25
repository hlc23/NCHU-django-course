from django.shortcuts import render
from django.http import Http404

from .models import Product, PPhoto
# Create your views here.

def index(request):
    products = Product.objects.all()
    return render(request, 'mobile/index.html', locals())

def detail(request, id):
    try: 
        product = Product.objects.get(id=id)
        images = PPhoto.objects.filter(product=product)
        return render(request, 'mobile/detail.html', locals())
    except Product.DoesNotExist:
        raise Http404("Product does not exist")