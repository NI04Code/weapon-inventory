import datetime
from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect, HttpResponse
from weapons.forms import WeaponForm
from django.urls import reverse
from weapons.models import Weapon
from django.core import serializers
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages 
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
# Create your views here.

@login_required(login_url='/login')
def show_weapons(request):
    weapons = Weapon.objects.all()

    context = {
        'name': request.user.username,
        'kelas': 'PBP F',
        'npm': '2206082013',
        'weapons': weapons,
        'weapons_total': weapons.count(),
        'last_login': request.COOKIES['last_login'],
    }

    return render(request, 'weapons.html', context)

def add_weapons(request):
    form = WeaponForm(request.POST or None)

    if form.is_valid() and request.method == "POST":
        weapons = form.save(commit=False)
        weapons.user = request.user
        weapons.save()
        return HttpResponseRedirect(reverse('weapons:show_weapons'))

    context = {'form': form}
    return render(request, "add_weapons.html", context)



def register(request):
    form = UserCreationForm()

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your account has been successfully created!')
            return redirect('weapons:login')
    context = {'form':form}
    return render(request, 'register.html', context)

def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            response = HttpResponseRedirect(reverse("weapons:show_weapons")) 
            response.set_cookie('last_login', str(datetime.datetime.now()))
            return response
        else:
            messages.info(request, 'Sorry, incorrect username or password. Please try again.')
    context = {}
    return render(request, 'login.html', context)

def logout_user(request):
    logout(request)
    response = HttpResponseRedirect(reverse('weapons:login'))
    response.delete_cookie('last_login')
    return response


def show_xml(request):
    data = Weapon.objects.all()
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json(request):
    data = Weapon.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

def show_xml_by_id(request, id):
    data = Weapon.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json_by_id(request, id):
    data = Weapon.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")


