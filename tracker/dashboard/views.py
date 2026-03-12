from django.shortcuts import render,redirect
from assignments.models import Assignment
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from django.contrib import messages
from datetime import timedelta

@login_required
def dashboard(request):

    total = Assignment.objects.filter(user=request.user).count()
    completed = Assignment.objects.filter(user=request.user, completed=True).count()
    pending = Assignment.objects.filter(user=request.user, completed=False).count()

    now = timezone.now()
    warning_time = now + timedelta(days=2)

    near_due = Assignment.objects.filter(
        user=request.user,
        completed=False,
        deadline__lte=warning_time,
        deadline__gte=now
    )

    overdue = Assignment.objects.filter(
        user=request.user,
        completed=False,
        deadline__lt=now
    )

    alerts_count = near_due.count() + overdue.count()

    context = {
        'total': total,
        'completed': completed,
        'pending': pending,
        'near_due': near_due,
        'overdue': overdue,
        'alerts_count': alerts_count
    }

    return render(request, 'dashboard/index.html', context)

@login_required
def profile_view(request):
    user = request.user

    # Recent assignments (e.g., last 5)
    recent_assignments = Assignment.objects.filter(user=user).order_by('-deadline')[:5]

    context = {
        'user': user,
        'recent_assignments': recent_assignments,
        'today': timezone.now().date(),  # for overdue calculation in template
    }
    return render(request, 'dashboard/profile.html', context)

@login_required
def edit_profile_view(request):
    if request.method == "POST":
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')

        user = request.user
        user.first_name = first_name
        user.last_name = last_name
        user.email = email
        user.save()

        messages.success(request, "Profile updated successfully!")
        return redirect('profile')

    return render(request, 'dashboard/edit_profile.html', {'user': request.user})