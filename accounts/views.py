from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import auth
from django.contrib.auth import authenticate
from .forms import UserLoginForm, UserRegistrationForm

# Create your views here.
def login(request):
    if request.method == "POST":
        u=request.POST['username']
        p=request.POST['password']
        user = authenticate(u='username', p='password')

        if user is not None:
            auth.login(request, user)
            return redirect("/")
        else:
            return HttpResponse("The user or password is incorrect!")
    else:
        login_form = UserLoginForm()
        return render(request, 'accounts/login.html', {"form": login_form})

def register(request):
    if request.method=="POST":
        registration_form = UserRegistrationForm(request.POST)
        if registration_form.is_valid():
            registration_form.save()
            
            u = registration_form.cleaned_data['username']
            p = registration_form.cleaned_data['password1']
            user = authenticate(username=u, password=p)
            
            if user is not None:
                auth.login(request, user)
                return redirect("/")
            else:
                registration_form.add_error(None, "Can't log in now, try later.")
    else:
        registration_form = UserRegistrationForm()
    
    
    return render(request, 'accounts/register.html', {'form': registration_form})
    
def profile(request):

    
    return render(request, 'accounts/profile.html')



  
# def register(request):
#     registration_form = UserRegistrationForm()
#     return render(request, "accounts/login.html",{"form":registration_form})
    
def logout(request):
    auth.logout(request)
    return redirect("/")