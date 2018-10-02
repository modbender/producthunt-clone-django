from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import auth

def login(request):
    if request.method == 'POST':
        user = auth.authenticate(username=request.POST['uname'],password=request.POST['pass'])
        if user is not None:
            auth.login(request, user)
            return redirect('home')
        else:
            return render(request, 'acc/login.html', {'error':'User not found'})
    else:
        return render(request, 'acc/login.html')

def signup(request):
    if request.method == 'POST':
        if request.POST['pass'] == request.POST['pass2']:
            try:
                User.objects.get(username=request.POST['uname'])
                return render(request, 'acc/signup.html', {'error': 'Username already used'})
            except User.DoesNotExist:
                user = User.objects.create_user(request.POST['uname'],password=request.POST['pass'])
                return redirect('home')
        else:
            return render(request, 'acc/signup.html', {'error': 'Passwords Not Matching'})
    else:
        return render(request, 'acc/signup.html')

def logout(request):
    if request.method == 'POST':
        auth.logout(request)
        return redirect('home')
    return render(request, 'acc/signup.html')
