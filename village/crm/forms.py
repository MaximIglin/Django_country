from django.core.exceptions import ValidationError
from . models import village_data
from django import forms
from django.forms import widgets


class AddVillageForm(forms.ModelForm):
    """ That form is allow add data about new_village """
    def clean(self):
        village_name = self.cleaned_data['title']
        region = self.cleaned_data['region']
        if village_data.objects.filter(title = village_name, region = region).exists():
            raise ValidationError (f"Деревня {village_name} уже зарегистрированна во вкладке 'С нами' ")
  
    def clean_short_information(self):
        short_information = self.cleaned_data['short_information']
        if len(short_information)<150:
            raise forms.ValidationError("Напишите чуть больше (рекомендумая длина краткого описания: 190 символов)")
        elif len(short_information)>300:
            raise forms.ValidationError("Слишком много информации в кратком описании, сократите объем до рекомендуемых 190-220 символов")
        return short_information

    def clean_all_information(self):
        all_information = self.cleaned_data['all_information']
        if len(all_information)<400:
            raise forms.ValidationError("Добавте больше информации о деревне")
        return all_information   

    class Meta:
        model = village_data
        fields = ['title', 'region', 'short_information', 'village_avatar_link', 'all_information', 'historical_informaion', 'at_the_moment', 'possibilities']
        widgets = {
            "title": widgets.TextInput(attrs={
                'class':'title_form add_form_hover'
            }),
            'short_information':widgets.Textarea(attrs={
                'class':'short_information_form add_form_hover ',
                'id':"exampleFormControlTextarea1"
            }),
            "village_avatar_link": widgets.TextInput(attrs={
                'class':'village_avatar_link_form add_form_hover'
            }),
            "region": widgets.Select(attrs={
                'class':'region_form add_form_hover'
                
            }),
            'all_information': widgets.Textarea(attrs={
                'class':'all_information_form add_form_hover'
            }),
            'historical_informaion': widgets.Textarea(attrs={
                'class':'historical_informaion_form add_form_hover'
            }),
            'at_the_moment': widgets.Textarea(attrs={
                'class':'at_the_moment_form add_form_hover'
            }),
            'possibilities': widgets.Textarea(attrs={
                'class':'possibilities_form add_form_hover'
            })
        }
        labels = {
            'region':"Регион"
        }