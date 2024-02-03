from django.db import models

# Create your models here.

class SchoolclassModel(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100, unique=True, null=True, blank=True)
    
    # database a name show korar jonne
    def __str__(self):
        return self.name


class StudentModel(models.Model):
    fullname = models.CharField(max_length=150)
    age = models.IntegerField()
    fatherName = models.CharField(max_length=150)
    motherName = models.CharField(max_length=150)
    roll = models.IntegerField()
    cl_name = models.ManyToManyField(SchoolclassModel)
    def __str__(self):
        return self.fullname

   