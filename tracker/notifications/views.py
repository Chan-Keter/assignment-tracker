from django.shortcuts import render

# Create your views here.
def animations(request):
    return render (request , 'utilities-animation.html')