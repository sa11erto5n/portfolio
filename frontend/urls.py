
from django.urls import path,include
from . import views

app_name = 'frontend'

urlpatterns = [
    path('',views.home,name='home'),
]

