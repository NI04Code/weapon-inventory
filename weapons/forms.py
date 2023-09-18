from django.forms import ModelForm
from weapons.models import Weapon

class WeaponForm(ModelForm):
    class Meta:
        model = Weapon
        fields = ["name", "amount", "atk", "critdmg", "critrate", "description"]