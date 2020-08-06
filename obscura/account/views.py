from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import loader

from django.contrib.auth.forms import UserCreationForm
from .forms import CreateUserForm
from django.contrib import messages


from django.contrib.auth import authenticate, login, logout
from .decorators import unauthenticated_user


# register view
@unauthenticated_user
def registerPage(request):
    form = CreateUserForm()
    context = { 
        "form": form 
    }
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
            messages.success(request, "Account was created for {}".format(user))
            return redirect('account:login')
    return render(request, 'account/register.html', context)


# login view
@unauthenticated_user
def loginPage(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('face:list')
        else:
            messages.info(request, 'Username OR password is incorrect')
            return redirect('account:login')
    context = {}
    return render(request, 'account/login.html', context)



def logoutUser(request):
    logout(request)
    return redirect('account:login')