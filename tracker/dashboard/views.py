from django.shortcuts import render
from assignments.models import Assignment
from django.contrib.auth.decorators import login_required

@login_required
def dashboard(request):

    total = Assignment.objects.filter(user=request.user).count()
    completed = Assignment.objects.filter(user=request.user, completed=True).count()
    pending = Assignment.objects.filter(user=request.user, completed=False).count()

    context = {
        'total': total,
        'completed': completed,
        'pending': pending
    }

    return render(request, 'dashboard/index.html', context)