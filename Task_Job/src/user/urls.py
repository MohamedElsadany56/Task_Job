from django.urls import path
from . import views
<<<<<<< HEAD
from django.contrib.auth import views as auth_views
=======
from django.contrib.auth import views
from .views import signup
>>>>>>> Elsadany

app_name = 'user'

urlpatterns = [
<<<<<<< HEAD
    path('', views.home, name='home'),    path('signup/', views.signup, name='signup'),
    path('login/', auth_views.LoginView.as_view(template_name='user/login/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='home'), name='logout'),
    path('login/', views.CustomLoginView.as_view(), name='login'),


=======
    path('signup/', views.signup, name='signup'),
    path('login/', views.LoginView.as_view(template_name='login.html'), name='login'),
>>>>>>> Elsadany
]