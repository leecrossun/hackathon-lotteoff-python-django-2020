from django.shortcuts import render, get_object_or_404, redirect
from django.core.paginator import Paginator
from .models import DriveThru
from django.http import Http404, HttpResponseRedirect
from django.core.exceptions import PermissionDenied
from shop.models import Product
from cart.models import Cart, CartItem
from django.core.exceptions import ObjectDoesNotExist

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

def new(request):
    cart = Cart.objects.latest('date_added')
    cart_items = CartItem.objects.filter(cart=cart, active=True)
    return render(request, 'new.html', dict(cart_items=cart_items))

def create(request):
    cart = Cart.objects.latest('date_added')
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
