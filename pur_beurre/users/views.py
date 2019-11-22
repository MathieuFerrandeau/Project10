"""Views management"""
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from catalog.models import Product
from .forms import RegisterForm, ConnexionForm


def register(request):
    """register view"""
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, 'Votre compte a bien été crée')
            return redirect('catalog:index')
    else:
        form = RegisterForm()

    return render(request, 'users/register.html', {'form': form})


def user_login(request):
    """login view"""
    error = False
    if request.method == "POST":
        form = ConnexionForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]
            user = authenticate(username=username, password=password)  # check if the data is correct
            if user:  # if the returned object is not None
                login(request, user)  # connect the user
            else:  # otherwise an error will be displayed
                error = True
    else:
        form = ConnexionForm()

    return render(request, 'users/login.html', locals())


def user_logout(request):
    """logout view"""
    logout(request)
    return render(request, 'users/logout.html')


@login_required
def profile(request):
    """profile view"""
    return render(request, 'users/profile.html')


@login_required
def favorite(request):
    """favorite view"""
    user = request.user
    fav = Product.objects.filter(userfavorite__user_name=user.id)
    if fav:
        product = Product.objects.filter(pk__in=fav)
    else:
        product = []

    return render(request, 'users/favorite.html', {'favorite': product})
