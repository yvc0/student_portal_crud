from django.shortcuts import render, redirect
from .models import Student
from .forms import StudentForm, SearchForm
from django.contrib import messages
from django.shortcuts import get_object_or_404

def home(request):
    return render(request, 'lms/home.html')

def add_student(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Student added successfully.")
            return redirect('add_student')
    else:
        form = StudentForm()
    return render(request, 'lms/add_student.html', {'form': form})

def search_student(request):
    student = None
    if request.method == 'POST':
        form = SearchForm(request.POST)
        if form.is_valid():
            student_id = form.cleaned_data['student_id']
            student = Student.objects.filter(student_id=student_id).first()
    else:
        form = SearchForm()
    return render(request, 'lms/search_student.html', {'form': form, 'student': student})

def delete_student(request):
    if request.method == 'POST':
        student_id = request.POST.get('student_id')
        student = Student.objects.filter(student_id=student_id).first()
        if student:
            student.delete()
            messages.success(request, "Student deleted.")
        else:
            messages.error(request, "Student not found.")
    return render(request, 'lms/delete_student.html')
def view_students(request):
    students = Student.objects.all()
    return render(request, 'lms/view_students.html', {'students': students})

def edit_student(request, student_id):
    student = get_object_or_404(Student, pk=student_id)
    if request.method == 'POST':
        form = StudentForm(request.POST, instance=student)
        if form.is_valid():
            form.save()
            messages.success(request, 'Student updated successfully.')
            return redirect('view_students')
    else:
        form = StudentForm(instance=student)
    return render(request, 'lms/edit_student.html', {'form': form})

def delete_student_direct(request, student_id):
    student = get_object_or_404(Student, pk=student_id)
    student.delete()
    messages.success(request, 'Student deleted successfully.')
    return redirect('view_students')
