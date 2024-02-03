# django builtin model forom
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms
from .models import teacherModel

class RegisterForm(UserCreationForm):
    subject = forms.CharField(max_length=150)
    age = forms.IntegerField()
    class Meta:
        model = User
        
        fields = ['username', 'first_name', 'last_name', 'email', 'subject', 'age']
        
    def save(self, commit= True):
        user =  super().save(commit=False)
        if commit == True:
            user.save() # user model a data save hobe

            subject = self.cleaned_data.get('subject')
            age = self.cleaned_data.get('age')
            
            
            # UserBankAccountModel model a data save hobe
            teacherModel.objects.create(
                user = user,
                subject = subject,
                age = age,
            )
            
        return user