from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

app_name = 'user'

urlpatterns = [
    path('', views.home, name='home'),    path('signup/', views.signup, name='signup'),
    path('login/', auth_views.LoginView.as_view(template_name='user/login/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='home'), name='logout'),
    path('login/', views.CustomLoginView.as_view(), name='login'),


]