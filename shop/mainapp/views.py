from django.shortcuts import render
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from .models import Product, ProductCategory

# Create your views here.

def index(request):
    context = {
        'title': 'Geekshop'
    }
    return render(request, template_name='mainapp/index.html', context=context)


def products(request, category_id=None, page=1):
    context = {
        'title': 'GeekShop - Каталог',
        'categories': ProductCategory.objects.all().order_by('name')
    }

    # if category_id:
    #     products = Product.objects.filter(category_id=category_id)
    # else:
    #     products = Product.objects.all()

    products = Product.objects.filter(category_id=category_id) if category_id else Product.objects.all()
    paginator = Paginator(products, per_page=3)
    try:
        products_paginator = paginator.page(page)
    except PageNotAnInteger:
        products_paginator = paginator.page(1)
    except EmptyPage:
        products_paginator = paginator.page(paginator.num_pages)

    context.update({'products': products_paginator})

    return render(request, template_name='mainapp/products.html', context=context)
