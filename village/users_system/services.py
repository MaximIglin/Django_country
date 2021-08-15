from .forms import RegistrationForm
from django.contrib.auth import authenticate, login, logout

def do_registration(form) -> None:
    """Thise function is create new iser from RegistrationForm"""
    new_user = form.save(commit = False)
    new_user.username = form.cleaned_data['username']
    new_user.email = form.cleaned_data['email']
    new_user.first_name = form.cleaned_data['first_name']
    new_user.last_name = form.cleaned_data['last_name']
    new_user.save()
    new_user.set_password(form.cleaned_data['password'])
    new_user.save()  
    
    