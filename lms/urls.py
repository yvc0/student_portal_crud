from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('add/', views.add_student, name='add_student'),
    path('students/edit/<int:student_id>/', views.edit_student, name='edit_student'),
    path('students/delete/<int:student_id>/', views.delete_student_direct, name='delete_student_direct'),
    path('search/', views.search_student, name='search_student'),
    path('delete/', views.delete_student, name='delete_student'),
    path('students/', views.view_students, name='view_students'),
]
