from django.urls import path
from . import views
from .views import GetPageWithView, AddVillageView


urlpatterns = [
    path('', views.get_home_page, name = 'home'),
    path('about', views.about_page, name = 'about'),
    path('for_businessmen', views.for_businessmen, name = 'for_businessmen'),
    path('with_us', GetPageWithView.as_view(), name = 'with_us'),
    path('add_village',AddVillageView.as_view(), name = "add_village")
]