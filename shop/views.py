from django.shortcuts import render, get_object_or_404
from .models import Category, Product
from django.core.paginator import Paginator

def home(request):
    return render(request, 'home.html')


def allProdCat(request, c_slug=None):
    c_page = None;
    products = None;
    if c_slug != None:
        c_page = get_object_or_404(Category, slug=c_slug)
        products = Product.objects.filter(category=c_page, unavailable=False)
    else:
        products = Product.objects.all().filter(unavailable=False)

    paginator = Paginator(products, 4)
    page = request.GET.get('page')
    prodPage = paginator.get_page(page)
    return render(request, 'shop/category.html',{'category':c_page, 'products':products, 'prodPage':prodPage})


def ProdCatDetail(request, c_slug, product_slug):
    try:
        product = Product.objects.get(category__slug=c_slug, slug=product_slug)
    except Exception as e:
        raise e

    return render(request, 'shop/product.html', {'product':product})
