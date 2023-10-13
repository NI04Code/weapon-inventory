from django.urls import path
from weapons.views import *

app_name = 'weapons'

urlpatterns = [
    path('', show_weapons, name='show_weapons'),
    path('add_weapons', add_weapons, name='add_weapons'),
    path('register/', register, name='register'),
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'),
    path('xml/', show_xml, name='show_xml'),
    path('json/', show_json, name='show_json'),
    path('xml/<int:id>/', show_xml_by_id, name='show_xml_by_id'),
    path('json/<int:id>/', show_json_by_id, name='show_json_by_id'), 
    path('get-weapons/', get_weapons_json, name='get_weapon_json'),
    path('create-weapon-ajax/', add_weapon_ajax, name='add_weapon_ajax'),
]