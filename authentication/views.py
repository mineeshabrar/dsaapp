from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User, Group

def login_view(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        heads = Group.objects.get(name="heads").user_set.all()
        students = Group.objects.get(name="students").user_set.all()
        if user is not None:
            if user in heads:
                login(request, user)
                return redirect('head/')
            if user in students:
                login(request, user)
                return redirect('student/')
        else:
            messages.success(request, ("There Was An Error Logging In, Try Again..."))	
            return redirect('login')
    else:
        return render(request, 'base_login_page.html')

def logout_view(request):
    return render(request, 'base_logout_page.html')
