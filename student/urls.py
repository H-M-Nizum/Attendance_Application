from django.urls import path
from . import views

urlpatterns = [
    
    path('add/', views.Addstudent.as_view(), name='add_student'),
    path('all/', views.showstudent, name='showstudent'),
    path('present/<int:id>', views.present, name='present'),
    path('apsent/<int:id>', views.apsent, name='apsent'),
    path('classs/<slug:class_slug>/', views.showstudent, name='class_slug_student'),
    path('teacher-attendance', views.teacher_attendance_view,name='teacher_attendance'),
    path('students_in_class/<str:class_name>/', views.students_in_class, name='students_in_class'),
     path('student_profile/<int:student_id>/', views.student_profile, name='student_profile'),
    
]