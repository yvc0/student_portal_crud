from django import forms
from .models import Student

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['student_id', 'name', 'email', 'course']

class SearchForm(forms.Form):
    student_id = forms.CharField(max_length=10, label='Student ID')
