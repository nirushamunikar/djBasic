from django.shortcuts import render, redirect
from .models import Laptops
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required(login_url = 'user_login')
def index(request):
    print(request.user)
    laptop_list = Laptops.objects.all()
    laptops={
        'laptops':laptop_list
    }
    return render(request, 'function_based/laptop-list.htm', laptops)


@login_required(login_url = 'user_login')
def create(request):
    if request.method == "POST":
        model = request.POST['model']
        manufacturer = request.POST['manufacturer']
        cpu = request.POST['cpu']
        gpu = request.POST['gpu']
        ram = request.POST['ram']
        price = request.POST['price']

        laptop = Laptops(name=model,manufacturer=manufacturer,cpu=cpu,gpu=gpu,ram=ram,price=price)
        laptop.save()
        return redirect('index')
    else:
        return render(request, 'function_based/laptop-create.htm')


@login_required(login_url = 'user_login')
def delete(request, id):
    print(request.user)
    del_obj = Laptops.objects.get(id=id)
    del_obj.delete()
    return redirect('index')


@login_required(login_url = 'user_login')
def update(request, id):
    obj = Laptops.objects.get(id=id)
    queryset={
        'queryset':obj
    }
    if request.method == "POST":
        model = request.POST['model']
        manufacturer = request.POST['manufacturer']
        cpu = request.POST['cpu']
        gpu = request.POST['gpu']
        ram = request.POST['ram']
        price = request.POST['price']

        obj.name=model
        obj.manufacturer=manufacturer
        obj.cpu=cpu
        obj.gpu=gpu
        obj.ram=ram
        obj.price=price
        obj.save()
        return redirect('index')
    else:
        return render(request,'function_based/laptop-update.htm', queryset)