from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from django.contrib import auth
from accounts.models import UserInput
from .models import Product

def home(request):
    products = Product.objects.all
    return render(request, 'products/home.html',{'products':products})

@login_required
def add(request):
    if request.method == 'POST':
        if request.POST['title'] and request.POST['desc'] and request.POST['desc'] and request.POST['url'] and request.POST['slug'] and request.FILES['image'] and request.FILES['icon']:
            if Product.objects.get(slug = request.POST['slug']).exists():
                return render(request, 'products/add.html',{'error':'Slug already used'})
            product = Product.objects.create(
                title = request.POST['title'],
                desc = request.POST['desc'],
                url = request.POST['url'],
                image = request.FILES['image'],
                icon = request.FILES['icon'],
                hunter = request.user,
                slug = request.POST['slug'],
            )
            return redirect('/product/'+ str(product.gslug()))
        else:
            return render(request, 'products/add.html',{'error':'All fields need to be filled'})
    else:
        return render(request, 'products/add.html')

def info(request, title):
    product = get_object_or_404(Product, slug=title)
    return render(request, 'products/info.html',{'product':product})

@login_required
def upvote(request, title):
    product = get_object_or_404(Product, slug=title)
    ui_obj, unew = UserInput.objects.get_or_create(user=request.user, product=product, upvote=True)
    if not unew:
        ui_obj.upvote = False
        ui_obj.save()
    return redirect(request.GET.get('next'))
