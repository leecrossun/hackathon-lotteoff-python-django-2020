from django.shortcuts import render, redirect, get_object_or_404
from shop.models import Product, Region
from django.core.paginator import Paginator

def select(request):

    return render(request, 'select.html')

def regionFilter(request, region):
    regionPost = Region.objects.filter(region=region)
    store = regionPost.first()
    return render(request, 'select.html', {"regionPost":regionPost, "store":store})

def storeFilter(request, storeName):
    storePost = Product.objects.filter(storeName=storeName)
    paginator = Paginator(storePost, 4)
    page = request.GET.get('page')
    storePage = paginator.get_page(page)
    
    return render(request, 'detail_store.html', {"storePost":storePage, "storeName": storeName})

def detail_product(request, product_id):
    store = get_object_or_404(Product, pk=product_id)
    return render(request, 'detail_product.html', {'store':store})
