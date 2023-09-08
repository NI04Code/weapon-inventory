from django.urls import path
from weapons.views import show_weapons

app_name = 'weapons'

urlpatterns = [
    path('', show_weapons, name='show_weapons'),
]