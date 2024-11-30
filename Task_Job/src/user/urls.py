from django.urls import path
from . import views
from django.contrib.auth import views
from .views import signup

app_name = 'user'

urlpatterns = [
    path('signup/', views.signup, name='signup'),
    path('login/', views.LoginView.as_view(template_name='login.html'), name='login'),
]