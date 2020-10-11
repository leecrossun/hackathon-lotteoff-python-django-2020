from django.shortcuts import render, get_object_or_404, redirect
from django.core.paginator import Paginator
from .models import DriveThru
from django.http import Http404, HttpResponseRedirect
from django.core.exceptions import PermissionDenied
from shop.models import Product
from cart.models import Cart, CartItem
from django.core.exceptions import ObjectDoesNotExist

def _cart_id(request):
    cart = request.session.session_key
    if not cart:
        cart = request.session.create()
    return cart

def home(request):
    return render(request, 'home.html')

def loginWarning(request):
    return render(request, 'loginWarning.html')

def driveThru(request):
    if not request.user.is_authenticated:
        return redirect('loginWarning')

    form = DriveThru.objects
    forms = DriveThru.objects.filter(author=request.user)
    paginator = Paginator(forms,3)
    page = request.GET.get('page')
    posts = paginator.get_page(page)
    return render(request, 'driveThru.html', {'form':form, 'posts':posts})

def new(request, total=0, counter=0):
    # cart = Cart.objects.latest('date_added')
    cart = Cart.objects.get(cart_id=_cart_id(request))
    cart_items = CartItem.objects.filter(cart=cart, active=True)
    for cart_item in cart_items:
        total += (cart_item.product.price * cart_item.quantity)
        counter += cart_item.quantity
    return render(request, 'new.html', dict(cart_items=cart_items, total=total, counter=counter))

def create(request):
    # cart = Cart.objects.latest('date_added')     
    cart = Cart.objects.get(cart_id=_cart_id(request))
    cart_items = CartItem.objects.filter(cart=cart, active=True)
    item = CartItem.objects.filter(cart=cart, pk=1)
    drive = DriveThru()
    drive.author = request.user
    drive.shop = request.POST['shop']
    drive.pick_date = request.POST['time']
    drive.pick_day = request.POST['date']
    drive.save()
    return redirect('driveThru')

def delete (request, pk):
    blog = get_object_or_404(DriveThru, pk = pk)
    blog.delete()
    return redirect('driveThru')
