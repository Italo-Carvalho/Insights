from django.urls import path
from .views import Home, NewCard

app_name = "web"

urlpatterns = [ 
    path('', Home, name='home'),
    path('new/', NewCard, name='new_card')
]
