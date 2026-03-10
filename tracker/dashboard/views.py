from django.shortcuts import render
from assignments.models import Assignment
from django.contrib.auth.decorators import login_required
# Create your views here.
def dashboard(request):

    total = Assignment.objects.filter(user=request.user).count()
    completed = Assignment.objects.filter(user=request.user, completed=True).count()
    pending = Assignment.objects.filter(user=request.user, completed=False).count()

    context = {
        'total': total,
        'completed': completed,
        'pending': pending
    }

    return render(request, 'index.html', context)

def buttons(request):
    return render(request,"buttons.html")

def cards(request):
    return render(request,"cards.html")

def utilities_color(request):
    return render(request,"utilities-color.html")

def utilities_border(request):
    return render(request,"utilities-border.html")

def utilities_animation(request):
    return render(request,"utilities-animation.html")

def utilities_other(request):
    return render(request,"utilities-other.html")

def login(request):
    return render(request,"login.html") 

def register(request):
    return render(request,"register.html") 

def forgot_password(request):
    return render(request,"forgot_password.html") 


def complete_assignment(request, id):
    assignment = Assignment.objects.get(id=id)
    assignment.completed = True
    assignment.save()
    return redirect('assignment_list')
    
@login_required(login_url='login/')
def dashboard(request):
    # Now request.user is guaranteed to be a logged-in user
    total = Assignment.objects.filter(user=request.user).count()
    context = {'total': total}
    return render(request, 'dashboard.html', context)   