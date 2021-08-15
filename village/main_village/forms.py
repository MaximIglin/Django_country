from django import forms
from django.forms import  widgets
from .models import VillagePictures, VillageChart


class ImageForm(forms.ModelForm):
    """This form for VillagePicture model"""
    class Meta:
        model = VillagePictures
        fields = ['image']

        widgets = {
            "image": widgets.FileInput(attrs={
                'class':'form-control-file'
            })    
        }
        labels = {
            'image':""
        }
        


class ChartForm(forms.ModelForm):
    """That form to add message in chart"""

    def clean(self):
        """Validaation params of field 'text_of_commment'"""
        message = self.cleaned_data['text_of_comment']
        if len(message) > 400:
            raise forms.ValidationError("Слишком длинное сообщение")

    class Meta:
        model = VillageChart
        fields = ['text_of_comment']

        widgets = {
            "text_of_comment":widgets.Textarea(attrs={
                'class':'chart_input_form'
            })
        }

        