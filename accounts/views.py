from django.shortcuts import render, redirect
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_http_methods
from django.contrib.auth.forms import AuthenticationForm
from .forms import CustomUserCreationForm
# Create your views here.


@require_http_methods(['POST','GET'])
def login(request):
    if request.user.is_authenticated:
        return redirect('movies:index')
    
    # POST
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            auth_login(request, form.get_user())
            return redirect('movies:index')

    else:
        form = AuthenticationForm()
    context = {
        'form':form,
    }
    return render(request, 'accounts/login.html', context)


@login_required
@require_http_methods(['POST',])
def logout(request):
        auth_logout(request.user)
        return redirect('movies:index')


@require_http_methods(['POST','GET'])
def signup(request):
    if request.user.is_authenticated:
        return redirect('movies:index')
    
    # POST
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request, user)
            return redirect('movies:index')

    else:
        form = CustomUserCreationForm()
    context = {
        'form':form,
    }
    return render(request, 'accounts/signup.html', context)


@require_http_methods(['GET','POST',])
def update(request):
    if request.method=='POST':
        form = CustomUserCreationForm(request.POST,instance = request.user)
        if form.is_valid():
            user=form.save()
            auth_login(request,user)
            return redirect('movies:index')
    else:
        form = CustomUserCreationForm(instance=request.user)
    context = {
        'form':form,
    }
    return render(request,'accounts/update.html',context)


@require_http_methods(['POST',])
def delete(request):
    request.user.delete()
    # auth_logout(request.user)
    return redirect("movies:index")


def change_password(request):
    pass


def profile(request):
    pass


def follow(request):
    pass