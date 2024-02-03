from django import forms
from .models import StudentModel

class StudentForm(forms.ModelForm):
    class Meta:
        model = StudentModel
        fields = '__all__'

#for Attendance related form
presence_choices=(('Present','Present'),('Absent','Absent'))
class AttendanceForm(forms.Form):
    attendanceStatse=forms.ChoiceField( choices=presence_choices)
    date=forms.DateField()