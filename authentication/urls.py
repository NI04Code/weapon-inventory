from django.urls import path
from authentication.views import login, logout, register, show_json

app_name = 'authentication'

urlpatterns = [
    path('login/', login, name='login'),
    path('logout/', logout, name='logout'),
    path('register/', register, name='register'),
    path('json/', show_json, name="show_json"),
]