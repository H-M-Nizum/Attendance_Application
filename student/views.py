from django.shortcuts import render, redirect, get_object_or_404, reverse
from . import forms
from .import models 
from attendance.models import AttendanceModel
from django.contrib.auth.decorators import login_required
from django.views.generic import CreateView
from django.urls import reverse_lazy
# for class base view login required
from django.http import HttpResponseRedirect

from django.utils.decorators import method_decorator
from datetime import datetime

# Create your views here.


@method_decorator(login_required, name='dispatch')
class Addstudent(CreateView):
    model = models.StudentModel
    form_class = forms.StudentForm
    template_name = 'add_student.html'

    success_url = reverse_lazy('add_student')


def showstudent(request, class_slug = None):
    data = models.StudentModel.objects.all()
    
        
        
    if class_slug is not None:
        cl_name = models.SchoolclassModel.objects.get(slug = class_slug)
        data = models.StudentModel.objects.filter(cl_name = cl_name)
    
    classnames = models.SchoolclassModel.objects.all()
    
    return render(request, 'showstudent.html', {'data': data, 'classname': classnames})


def teacher_attendance_view(request):
    return render(request,'teacher_attendance.html')

def attendance1(request, id):
    student = get_object_or_404(models.StudentModel, pk=id)
    # print(student)
    print(student.fullname)
    print(student.age)
    return redirect("class_slug_student")

def present(request, id):
    std = get_object_or_404(models.StudentModel, pk=id)
    print(std)
    cls = std.cl_name.all().first()
    attandenc = AttendanceModel(student = std, cl_name = cls, attendanceStatse = True)
    attandenc.save()

    class_name = cls  # Change this according to your actual model field

    # Generate the URL for students_in_class view with the class_name parameter
    url = reverse('students_in_class', kwargs={'class_name': class_name})

    # Redirect to the generated URL
    return HttpResponseRedirect(url)
    # return HttpResponseRedirect(reverse('students_in_class'))
def apsent(request, id):
    std = get_object_or_404(models.StudentModel, pk=id)
    print(std)
    cls = std.cl_name.all().first()
    attandenc = AttendanceModel(student = std, cl_name = cls)
    attandenc.save()
    class_name = cls  # Change this according to your actual model field

    # Generate the URL for students_in_class view with the class_name parameter
    url = reverse('students_in_class', kwargs={'class_name': class_name})

    # Redirect to the generated URL
    return HttpResponseRedirect(url)

    # return HttpResponseRedirect(reverse('students_in_class'))


def students_in_class(request, class_name):
    students = models.StudentModel.objects.filter(cl_name__name=class_name)
    
    context = {
        'class_name': class_name,
        'students': students,
    }

    return render(request, 'students_in_class.html', context)





# def teacher_take_attendance_view(request,cl_name):
#     students=models.StudentModel.objects.all().filter(cl_name='five')
#     aform=forms.AttendanceForm()
#     if request.method=='POST':
#         form=forms.AttendanceForm(request.POST)
#         if form.is_valid():
#             Attendances=request.POST.getlist('attendanceStatse')
#             date=form.cleaned_data['date']
#             for i in range(len(Attendances)):
#                 AttendanceModel=models.AttendanceModel()
#                 AttendanceModel.cl_name=cl_name
#                 AttendanceModel.date=date
#                 AttendanceModel.attendanceStatse=Attendances[i]
#                 AttendanceModel.student=students[i].student
#                 AttendanceModel.save()
#             return redirect('teacher-attendance')
#         else:
#             print('form invalid')
#     return render(request,'teacher_take_attendance.html',{'students':students,'aform':aform})
    


from django.shortcuts import get_object_or_404, reverse
from django.http import HttpResponseRedirect
from .models import StudentModel

def apsent111(request, id):
    std = get_object_or_404(StudentModel, pk=id)
    cls = std.cl_name.all().first()

    # Assuming you have a roll field in StudentModel
    student_roll = std.roll  # Replace 'roll' with the actual field name in your model

    # Filter students based on cl_name and student roll
    filtered_students = StudentModel.objects.filter(cl_name=cls, roll=student_roll)

    print(filtered_students)
    return redirect()


def calculate_present_days(student_id):
    # Get the student based on the student_id (assuming it's the primary key)
    student = models.StudentModel.objects.get(pk=student_id)

    # Filter the attendance records for the specific student where attendanceStatse is True
    present_days = AttendanceModel.objects.filter(student=student, attendanceStatse=True).count()

    return present_days
def calculate_apsent_days(student_id):
    # Get the student based on the student_id (assuming it's the primary key)
    student = models.StudentModel.objects.get(pk=student_id)

    # Filter the attendance records for the specific student where attendanceStatse is True
    apsent_days = AttendanceModel.objects.filter(student=student, attendanceStatse=False).count()

    return apsent_days


def student_profile(request, student_id):
    student = StudentModel.objects.get(pk=student_id)
    present_days = calculate_present_days(student_id)
    apsent_days = calculate_apsent_days(student_id)
    if (present_days+apsent_days) == 0:
        parcentage = 0.0
    else:        
        parcentage = (present_days/(present_days+apsent_days))*100

    context = {
        'student': student,
        'present_days': present_days,
        'apsent_days' : apsent_days,
        'parcentage': parcentage,
    }

    return render(request, 'student_profile.html', context)