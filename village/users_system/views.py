from django.http.response import HttpResponseRedirect
from django.shortcuts import render
from django.views.generic import View
from .forms import LoginForm,RegistrationForm
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from .services import do_registration



# Create your views here.

class LoginView(View):
    """This class based View is return LoginForm and autheticate user"""
    def get(self, request, *args, **kwargs):
        form = LoginForm(request.POST or None)
        context = {'form':form}
        return render(request, 'users_system/authorisation.html', context)

    def post(self, request, *args, **kwargs):
        form = LoginForm(request.POST or None) 
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']   
            user = authenticate(username = username, password = password)
            if user:
                login(request, user)
                return HttpResponseRedirect('/')
        return render(request, 'users_system/authorisation.html', {'form':form})


def logout_user(request):
    """This funtion is logout autheticated user"""
    logout(request)
    return HttpResponseRedirect('login')


class RegisterUser(View):
    """This class based View is get RegistationForm and registrate user"""
    def get(self, request, *args, **kwargs):
        form = RegistrationForm(request.POST or None)
        context = {'form': form}
        return render(request, 'users_system/registration.html', context)

    def post(self, request, *args, **kwargs):
        form = RegistrationForm(request.POST or None)
        if form.is_valid():
            do_registration(form)
            user = authenticate(username = form.cleaned_data['username'], password = form.cleaned_data['password'])
            return HttpResponseRedirect('/')
        context = {'form': form}
        return render(request, 'users_system/registration.html', context)         
