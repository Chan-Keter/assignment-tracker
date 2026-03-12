from django.urls import path
from . import views

urlpatterns = [
    path('', views.assignment_list, name='assignment_list'),
    path('add/', views.add_assignment, name='add_assignment'),
    path('complete/<int:id>/', views.complete_assignment, name='complete_assignment'),
    path('assignment/',views.add,name='assignment')
]