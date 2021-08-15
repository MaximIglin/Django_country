from crm.models import village_data
from . models import VillageChart
from django.contrib import auth

def get_village_by_name(name: str) -> village_data:
    """ This function is get name of village and return correct village_data_object """
    return village_data.objects.get(title = name)


def add_photos_by_form(form, correct_village) -> None :
    """ Function is creare new village-data object, cleaned data of form's fields and save object to db """   
    image = form.save(commit=False)
    image.image = form.cleaned_data['image']
    image.village_name = correct_village
    image.save() 


def add_message_to_chart(request, form, correct_village) -> None:
    """ Function is create new message and post that """
    comment = VillageChart()
    comment.village_id = correct_village
    comment.user_id = auth.get_user(request)
    comment.text_of_comment = form.cleaned_data['text_of_comment']
    comment.save()
