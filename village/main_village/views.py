
from django.http.response import  HttpResponseRedirect
from django.shortcuts import render
from django.views.generic import View
from crm.models import village_data
from .models import VillageNews, VillagePictures, VillageChart
from rest_framework import viewsets
from .serializers import VillageNewsSerializer, VillageSerializer, VillagePicturesSerializer
from .forms import ImageForm, ChartForm
from .services import get_village_by_name, add_photos_by_form, add_message_to_chart



class GetAllData(View):
    """ This Class based View is return all information about selected village (on page with us)"""
    def get(self,request,*args,**kwargs):
        context = {
            'village': get_village_by_name(self.kwargs['name'])
        }
        return render(request, 'main_village/villages.html', context)

class AddPhotos(View):
    """This Class based View is get page with AddPhotosForm and add Photos to VillagePhotos model"""
    def get(self,request,*args,**kwargs):
        correct_village = get_village_by_name(self.kwargs['name'])
        form = ImageForm(request.POST or None)
        context = {'add_photo_form':form,
                'village':correct_village
                }
        return render(request,"main_village/villages.html",context)

    def post(self,request,*args,**kwargs):
        form = ImageForm(request.POST,request.FILES)
        context = {'add_photo_form':form}
        if form.is_valid():
            correct_village = get_village_by_name(self.kwargs['name'])
            add_photos_by_form(form = form, correct_village = correct_village)
            return HttpResponseRedirect(f'/village/{correct_village.title}')
        return render(request,"main_village/villages.html",context)


class ChartView(View):
    """This Class based View is get page with chart and add messages to VillagePhotos model"""
    def get(self,request,*args,**kwargs):
        form = ChartForm(request.POST or None)
        correct_village = get_village_by_name(self.kwargs['name'])
        correct_chart = VillageChart.objects.filter(village_id = correct_village)
        context = {
            'chart_form':form,
            'chart':correct_chart,
            'village':correct_village
        }
        return render(request,"main_village/villages.html", context)

    def post(self, request, *args, **kwargs):
        form = ChartForm(request.POST or None)
        correct_village = get_village_by_name(self.kwargs['name'])
        correct_chart = VillageChart.objects.filter(village_id = correct_village)
        context = {
            'chart_form':form,
            'chart':correct_chart,
            'village':correct_village
        }
        if form.is_valid():
            add_message_to_chart(request = request, form = form, correct_village = correct_village)
            return HttpResponseRedirect(f"http://127.0.0.1:8000/village/chart/{correct_village.title}")
        return render(request, "main_village/villages.html", context)




# Viewsets 
class VillageViewSet(viewsets.ModelViewSet):
    """Viewset for village_data model"""
    queryset = village_data.objects.filter()
    serializer_class = VillageSerializer


class VillagePicturesViewSet(viewsets.ModelViewSet):
    """Viewset for VillagePictures model"""    
    queryset = VillagePictures.objects.all()
    serializer_class = VillagePicturesSerializer           

class VillageNewsViewSet(viewsets.ModelViewSet):
    """Viewset for VillageNews model"""    
    queryset = VillageNews.objects.all().order_by("village_name")
    serializer_class = VillageNewsSerializer


   

