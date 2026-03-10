from django.urls import path
from . import views

urlpatterns = [
    path('animations/',views.animations,name='animations'),
]