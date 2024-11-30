
from django.shortcuts import render , redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login 


def frontpage(request):
    return render(request, 'frontpage.html')

def signup(request):
    if request.method =='POST' : 
        form = UserCreationForm(request.POST)

        if form.is_valid():
            user=form.save()

            login(request , user)

            return redirect('frontpage')
    else :
        form=UserCreationForm()

    return render(request, 'user/signup/signup.html', {'form': form})
