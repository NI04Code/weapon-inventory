from django.shortcuts import render

# Create your views here.
def show_weapons(request):
    attr = {
        'name': 'Iron Sword',
        'atk': '5',
        'critdmg': '80.3',
        'critrate': '18.9',
        'description': '???',
    }

    return render(request, 'weapons.html', attr)

