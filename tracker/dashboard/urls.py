from django.urls import path
from . import views

urlpatterns = [
    path('',views.dashboard,name='dashboard'),
    path('buttons/',views.buttons,name='buttons'),
    path('cards/',views.cards,name='cards'),
    path('utilities_color/',views.utilities_color,name='utilities_color'),
    path('utilities_border/',views.utilities_border,name='utilities_border'),
    path('utilities_animation/',views.utilities_animation,name='utilities_animation'),
    path('utilities_other/',views.utilities_other,name='utilities_other'),
    path('login/',views.login,name='login'),
    path('register/',views.register,name='register'),
    path('forgot_password/',views.forgot_password,name='forgot_password'),
]