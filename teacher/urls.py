from django.urls import path
from . import views

urlpatterns = [
    
    path('add/', views.RegistrationViews.as_view(), name='add_teacher'),
    path('login/', views.Userloginviews.as_view(), name='login'),
    path('logout/',  views.userlogoutview.as_view(), name='logout'),
    path('teacher_dashbord/',  views.Teacher_dashbord.as_view(), name='teacher_dashbord'),
    path('profile/', views.profile, name='profile')

    
    
]