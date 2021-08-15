from django.db import models
from django.db.models.fields.json import JSONField


class layout_data(models.Model):
    """That model is contain data for static-pages('about' and 'for_businessmen')"""
    title = models.CharField('Заголовок', max_length=30)
    main_consistion = models.TextField('Содержимое выше фото')
    main_consistion_2 = models.TextField('Содержимое ниже фото', default= "", null = True, blank = True)
    data = JSONField()

    class Meta:
        verbose_name = "Данные для статических страниц"
        ordering = ["title"]
    def __str__(self):
        return self.title


class Regions(models.Model):
    """ That model is contain data of Regions """
    name = models.CharField("Регион", max_length=100)
    
    class Meta:
        verbose_name = "Регионы"
        ordering = ['name']
    def __str__(self):
        return self.name
    

class village_data(models.Model):
    """ That model is contain data of every village """
    title = models.CharField('Название населённого пункта', max_length=50)
    short_information = models.TextField('Краткое описание')
    village_avatar_link = models.CharField('Ссылка на аватар', max_length = 300)
    region = models.ForeignKey(Regions,null=True, on_delete=models.SET_NULL, default="")
    all_information = models.TextField('Подробная информация')
    historical_informaion = models.TextField('Историческая справка', blank = True)
    at_the_moment = models.TextField('Ситуация на данный момент', blank = True)
    possibilities = models.TextField('Возможности для предпринимателей', blank = True)

    class Meta:
        verbose_name = "Данные о деревнях"
        ordering = ["region"]
    def __str__(self):
        return f"{self.title} : {self.id}"





