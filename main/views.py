from django.shortcuts import render
from .models import Product
from .models import Category_products

# Create your views here.

def view_product(request):
    list_product = Product.objects.all()
    list_product_active =list_product.filter(Pr_active=True)
    list_active = {'product': list_product_active, "active": ['active', '', '', '', '']}
    return render (request, 'homepage/shop.html',  list_active )


def view_category(request):
    product_raucu = Product.objects.filter(Pr_category= Category_products.objects.get(Cpr_name="Rau củ"))
    print("test", product_raucu)
    context = {'product': product_raucu,  "active": ['', 'active', '', '', '']}
    return render (request, 'homepage/shop.html', context)


def view_category1(request):
    product_traicay = Product.objects.filter(Pr_category= Category_products.objects.get(Cpr_name="Trái cây"))
    context = {'product': product_traicay,  "active": ['', '', 'active', '', '']}
    return render (request, 'homepage/shop.html', context)

def view_category2(request):
    product_nuocep = Product.objects.filter(Pr_category= Category_products.objects.get(Cpr_name="Nước ép"))
    context = {'product': product_nuocep,  "active": ['', '', '', 'active', '']}
    return render (request, 'homepage/shop.html', context)


def view_category3(request):
    product_cacloaihat = Product.objects.filter(Pr_category= Category_products.objects.get(Cpr_name="Các loại hạt"))
    context = {'product': product_cacloaihat,  "active": ['', '', '', '', 'active']}
    return render (request, 'homepage/shop.html', context)

def detailproduct(request, id):
    detailproduct = Product.objects.get(Pr_id=id)
    context = {'detail': detailproduct}
    return render (request, 'homepage/product-single.html', context)

def view_index(request):
    view_index = Product.objects.filter(Pr_sale=True)
    context = {'view_index': view_index}    
    return render (request, 'homepage/index.html', context)