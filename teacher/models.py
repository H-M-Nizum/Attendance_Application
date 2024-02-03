from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class teacherModel(models.Model):
    user = models.ForeignKey(User, related_name='builtinuser', on_delete=models.CASCADE)
    subject = models.CharField(max_length=150)
    age = models.IntegerField()
    join_date = models.DateField(auto_now_add=True)
    admin_approve = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.user.first_name} {self.user.last_name}"
    