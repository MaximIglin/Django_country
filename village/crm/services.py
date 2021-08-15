from .models import layout_data, village_data



def get_pages_data(title: str) -> dict:
    """ Function is get title of the page and return correct context"""    
    data_object = layout_data.objects.get(title = title)
    data = {
        'title': data_object.title,
        'main_consistion' : data_object.main_consistion,
        'list_of_links' : data_object.data['link'][:3],
        'main_consistion_2' : data_object.main_consistion_2,
        'list_of_links_2' : data_object.data['link'][3:]
    }
    return data

def save_village_by_form(form) -> None :
    """ Function is creare new village-data object, cleaned data of form's fields and save object to db """
    new_village = village_data()
    new_village.title = form.cleaned_data['title']
    new_village.region = form.cleaned_data['region']
    new_village.short_information = form.cleaned_data['short_information']
    new_village.village_avatar_link = form.cleaned_data['village_avatar_link']
    new_village.all_information = form.cleaned_data['all_information']
    new_village.historical_informaion = form.cleaned_data['historical_informaion']
    new_village.at_the_moment = form.cleaned_data['at_the_moment']
    new_village.possibilities = form.cleaned_data['possibilities']
    new_village.save()

