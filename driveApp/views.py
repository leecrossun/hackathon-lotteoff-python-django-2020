from django.shortcuts import render, get_object_or_404, redirect
from django.core.paginator import Paginator
from .models import DriveThru
from django.http import Http404, HttpResponseRedirect
from django.core.exceptions import PermissionDenied


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
    return render(request, 'new.html')

def delete (request, pk):
    blog = get_object_or_404(DriveThru, pk = pk)
    blog.delete()
    return redirect('driveThru')