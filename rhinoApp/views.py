from django.shortcuts import render, redirect
from django.views.generic.base import TemplateView
from .models import *
from django.http import HttpResponse
from .decorators import authenticated_user, allowed_users, admin_only
from django.contrib.auth.models import Group


# Create your views here.
# def index(request):
#     return render(request, '../templates/index.html')

# @allowed_users(allowed_roles=['admin'])
def home(request):
  

    return render(request, 'index.html')

@authenticated_user
def registerPage(request):
    form = CreateUserForm()
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')

            group = Group.objects.get(name='hw')
            user.groups.add(group)

            return redirect('login')

    context = {'form': form}
    return render(request, 'registration/login.html', context)

# @authenticated_user
def loginPage(request):

    return render(request, 'registration/login.html')

    # if request.method == 'POST':
    #     username = request.POST.get('username')
    #     password = request.POST.get('password')

    #     user = authenticate(request, username=username, password=password)

    #     if user is not None:
    #         login(request, user)
    #         return redirect('home')
    #     else:
    #         messages.info(request, 'Username OR password')

@authenticated_user
def checkLogin(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password=request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')

        else:
            messages.info(request, 'Username OR password')

        if 'next' in request.POST:
            return redirect(request.POST.get('next'))
        else:
            return redirect ('trainings')
        context = {}
        return(request, 'trainings.html')

# @authenticated_user
# def products(request):
#     prod = Trainings.objects.all()
#     return render(request, 'trainings.html', context={"prod": prod})

# @allowed_users(allowed_roles=['admin'])
# @authenticated_user
def training(request):
    trainings = Trainings.objects.all()
    return render(request, 'trainings.html', context={"trainings": trainings})

# def child(request):
#     childs = Child.objects.all()
#     return render(request, 'trainings.html', context={"childs": childs})

# @allowed_users(allowed_roles=['admin'])
# def SymptomsRecord():
#     return redirect('home')
    