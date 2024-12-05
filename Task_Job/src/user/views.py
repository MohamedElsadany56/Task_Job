
from django.shortcuts import render , redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login 
from django.contrib.auth.views import LoginView
from django.urls import reverse

def home(request):
    return render(request, 'user/home.html')

def signup(request):
    if request.method =='POST' : 
        form = UserCreationForm(request.POST)

        if form.is_valid():
            user=form.save()

            login(request , user)

            return redirect('home')
    else :
        form=UserCreationForm()

    return render(request, 'user/signup/signup.html', {'form': form})


class CustomLoginView(LoginView):
    template_name = 'user/login/login.html'
    redirect_authenticated_user = True

    def get_success_url(self):
        return reverse('home')