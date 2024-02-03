from django.db import models
from student.models import StudentModel
# Create your models here.
class AttendanceModel(models.Model):
    student = models.ForeignKey(StudentModel, on_delete=models.CASCADE)
    cl_name= models.CharField(max_length=10)
    date = models.DateField(auto_now_add=True)
    attendanceStatse = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.student}"
    