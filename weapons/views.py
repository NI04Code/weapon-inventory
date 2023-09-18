from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from weapons.forms import WeaponForm
from django.urls import reverse
from weapons.models import Weapon
from django.core import serializers

# Create your views here.
def show_weapons(request):
    weapons = Weapon.objects.all()

    context = {
        'name': 'Naufal Ichsan',
        'kelas': 'PBP F',
        'npm': '2206082013',
        'weapons': weapons,
        'weapons_total': weapons.count(),
    }

    return render(request, 'weapons.html', context)

def add_weapons(request):
    form = WeaponForm(request.POST or None)

    if form.is_valid() and request.method == "POST":
        form.save()
        return HttpResponseRedirect(reverse('weapons:show_weapons'))

    context = {'form': form}
    return render(request, "add_weapons.html", context)

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


