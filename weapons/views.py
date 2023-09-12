from django.shortcuts import render

# Create your views here.
def show_weapons(request):
    context = {
        'name': 'Iron Sword',
        'amount': '1',
        'atk': '5',
        'critdmg': '80.3',
        'critrate': '18.9',
        'description': 'Basic sword made of iron',
    }

    return render(request, 'weapons.html', context)

