from django.urls import path
from django.views.generic import TemplateView
from .views import*



urlpatterns = [
    path('login', LoginView.as_view(), name = 'authorisation'),
    path('logout', logout_user, name = 'logout'),
    path('register', RegisterUser.as_view(), name = 'register'),
    
]