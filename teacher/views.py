from django.shortcuts import render, redirect
from django.views.generic import FormView, View
from django.contrib.auth.views import LoginView
from django.contrib.auth import login, logout
from django.urls import reverse_lazy
from .forms import RegisterForm
from . import models
from django.contrib.auth.decorators import login_required
# Create your views here.

from django.views.generic import TemplateView

# Create your views here.

class Teacher_dashbord(TemplateView):
    template_name = 'teacher_dashbord.html'

class RegistrationViews(FormView):
    template_name = 'registration.html'
    form_class = RegisterForm
    success_url =reverse_lazy('add_teacher')
    
    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return super().form_valid(form) # form_valid functions call hobe jodi sob thik thake

class Userloginviews(LoginView):
    template_name = 'login.html'
    
    def get_success_url(self):
        return reverse_lazy('home')

class userlogoutview(View):
    def get(self, request):
        logout(request)
        return redirect('home')



@login_required
def profile(request):
    teacher = models.teacherModel.objects.get(user=request.user)
    print(teacher)
    return render(request, 'profile.html', {'data' : teacher})


