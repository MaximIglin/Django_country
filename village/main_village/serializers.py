from crm.models import village_data
from .models import VillagePictures, VillageNews
from rest_framework import serializers


class VillageSerializer(serializers.ModelSerializer):
    """Serializer for village_data model"""
    class Meta:
        model = village_data
        fields = ['id', 'title', 'all_information', 'historical_informaion', 'at_the_moment', 'possibilities']




class VillagePicturesSerializer(serializers.ModelSerializer):
    """Serializer for VillagePicture model"""
    class Meta:
        model = VillagePictures
        fields = ['village_name', 'image', 'add_date']


class VillageNewsSerializer(serializers.ModelSerializer):
    """Serializer for VillageNews model"""
    class Meta:
        model = VillageNews
        fields = ["village_name", "title", "short_text_of_news", "text_of_news", "date", "images"]       