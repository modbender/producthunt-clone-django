from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from django.contrib import auth
from .models import Product

def home(request):
    products = Product.objects.all
    return render(request, 'products/home.html',{'products':products})

@login_required
def add(request):
    if request.method == 'POST':
        if request.POST['title'] and request.POST['desc'] and request.POST['desc'] and request.POST['url'] and request.POST['slug'] and request.FILES['image'] and request.FILES['icon']:
            product = Product()
            product.title = request.POST['title']
            product.desc = request.POST['desc']
            product.url = request.POST['url']
            product.image = request.FILES['image']
            product.icon = request.FILES['icon']
            product.product_date = timezone.datetime.now()
            product.votes = 1
            product.hunter = request.user
            product.voter = request.user
            prs = Product.objects.get(slug = request.POST['slug'])
            if prs is not None:
                return render(request, 'products/add.html',{'error':'Slug already used'})
            else:
                product.slug = request.POST['slug']
            product.save()
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
    if request.method == 'POST':
        product.votes += 1
        product.voting_user = request.user
        product.save()
        return redirect('/product/' + product.slug)
    else:
        return render(request, 'products/info.html',{'product':product,'error':'You need to be logged in to use this function'})

@login_required
def hupvote(request, title):
    product = get_object_or_404(Product, slug=request.POST['slug'])
    if request.method == 'POST':
        product.votes += 1
        product.voting_user = request.user
        product.save()
    return redirect('home')
