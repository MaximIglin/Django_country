from django.http.response import HttpResponseRedirect
from django.shortcuts import render
from django.views.generic.base import View
from .models import  village_data
from django.views.generic import ListView
from .forms import AddVillageForm
from .services import get_pages_data, save_village_by_form


def get_home_page(request):
    """ Thise function is return home-page """
    return render(request, 'crm/index.html')


def about_page(request):
    """ Thise function is return about-page """
    return render(request, 'crm/layout.html', get_pages_data('О проекте'))


def for_businessmen(request):
    """ Thise function is return businessmans-page """
    return render(request, 'crm/layout.html', get_pages_data('Предпринимателям'))   


class GetPageWithView(ListView):
    """ This Class Based View is return page 'with_us' """
    model = village_data         
    template_name = "crm/with_us.html"  
    context_object_name = "villages"  

    def get_queryset(self) :
        return village_data.objects.order_by('title')



class AddVillageView(View):
    """ This Class based Views is get AddVillageForm-page and post new village """
    def get(self, request, *args, **kwargs) :
        form = AddVillageForm(request.POST or None)
        context = {
            'form': form
        }
        return render(request, 'crm/with_us.html', context)

    def post(self, request, *args, **kwargs):
        form = AddVillageForm(request.POST or None)
        context = {
            'form': form
        }
        if form.is_valid():
            save_village_by_form(form = form)
            return HttpResponseRedirect('with_us')
        return render(request,'crm/with_us.html',context)    




  
    