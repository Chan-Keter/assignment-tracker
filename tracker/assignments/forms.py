from django import forms
from .models import Assignment

class AssignmentForm(forms.ModelForm):
    class Meta:
        model = Assignment
        fields = ['subject', 'title', 'description', 'deadline']
        widgets = {
            'subject': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter the subject name'
            }),
            'title': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter the title'
            }),
            'description': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Enter the description'
            }),
            'deadline': forms.DateInput(attrs={
                'class': 'form-control',
                'type': 'date'
            }),
        }