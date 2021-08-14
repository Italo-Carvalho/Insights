from django.urls import path
from .views import Home

app_name = "web"

urlpatterns = [ 
    path('', Home, name='home')
]
