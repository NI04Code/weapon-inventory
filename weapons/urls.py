from django.urls import path
from weapons.views import show_weapons, add_weapons, show_xml, show_json, show_xml_by_id, show_json_by_id

app_name = 'weapons'

urlpatterns = [
    path('', show_weapons, name='show_weapons'),
    path('add_weapons', add_weapons, name='add_weapons'),
    path('xml/', show_xml, name='show_xml'),
    path('json/', show_json, name='show_json'),
    path('xml/<int:id>/', show_xml_by_id, name='show_xml_by_id'),
    path('json/<int:id>/', show_json_by_id, name='show_json_by_id'), 
]