from django.shortcuts import render, get_object_or_404, redirect
from .models import NewProduct
from .forms import ApplyForm
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required

def newProduct(request):
    data = NewProduct.objects
    datas= NewProduct.objects.all()
    paginator = Paginator(datas, 3)
    page = request.GET.get('page')
    posts = paginator.get_page(page)
    return render(request, "newProduct.html", {'news':datas, 'posts':posts})

def newDetail(request, new_id):
    post = get_object_or_404(NewProduct, pk=new_id)
    apply_form = ApplyForm()
    return render(request, 'newDetail.html', {'post':post, 'apply_form':apply_form,})

@login_required
def createApply(request, new_id):
    apply_form = ApplyForm(request.POST)
    if apply_form.is_valid():
        apply = apply_form.save(commit = False)
        apply.author = request.user
        apply.newProduct = NewProduct.objects.get(pk = new_id)
        apply.save()
        return redirect('newDetail', new_id)

@login_required
def deleteApply(request, new_id, apply_id):
    apply = Apply.objects.get(pk = apply_id)
    if request.user == apply.author:
        apply.delete()
        return redirect('newDetail', new_id)
    else:
        raise PermissionDenied