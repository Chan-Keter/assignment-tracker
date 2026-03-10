from django.urls import path
from . import views

urlpatterns = [
    path('', views.assignment_list, name='assignment_list'),
    path('add/', views.add_assignment, name='add_assignment'),
]