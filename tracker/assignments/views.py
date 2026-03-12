from django.shortcuts import render, redirect
from .models import Assignment
from .forms import AssignmentForm
from django.contrib.auth.decorators import login_required


@login_required
def assignment_list(request):
    assignments = Assignment.objects.filter(user=request.user)
    return render(request, 'assignments/list.html', {'assignments': assignments})


@login_required
def add_assignment(request):
    if request.method == "POST":
        form = AssignmentForm(request.POST)
        if form.is_valid():
            assignment = form.save(commit=False)
            assignment.user = request.user
            assignment.save()
            return redirect('assignment_list')
    else:
        form = AssignmentForm()

    return render(request, 'assignments/add.html', {'form': form})

def complete_assignment(request, id):
    assignment = Assignment.objects.get(id=id)
    assignment.completed = True
    assignment.save()
    return redirect('assignment_list')

def add(request):
    return render(request,'add.html')