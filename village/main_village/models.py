from django.db import models
from django.contrib.auth.models import User
from crm.models import village_data


class VillagePictures(models.Model):
    """ That model is contain photos of every villages """
    village_name = models.ForeignKey(village_data, null = True, on_delete = models.CASCADE, blank = True)
    image = models.ImageField()
    add_date = models.DateField(auto_now = True, null = True, blank = True)

    class Meta:
        verbose_name = "Фото деревень"
        ordering = ["village_name__title"]
    def __str__(self):
        return f"{self.village_name.title}-{self.id}: {self.add_date}"

class VillageNews(models.Model):
    """ That model is contain news of every village """
    village_name = models.ForeignKey(village_data, null = True, blank = True, on_delete = models.CASCADE)
    title = models.CharField("Заголовок новсти", max_length = 150, default="Заголовок")
    short_text_of_news = models.TextField("Краткое описание", default = "Краткое описание", max_length = 250)
    text_of_news = models.TextField("Содержание новости", default  = "Новость:")
    date = models.DateField(auto_now = True)
    images = models.JSONField()
    
    class Meta:
        verbose_name = "Новости"
        ordering = ["date"]

    def __str__(self):
        return (f"Новость: в деревне {self.village_name.title} от {self.date}")    



class VillageChart(models.Model):
    """ That model is contain all chart's massages """
    village_id = models.ForeignKey(village_data, null = True, default = True, on_delete = models.CASCADE, blank = True)
    user_id = models.ForeignKey(User, null = True, default = "Некий пользователь", on_delete = models.SET_DEFAULT, blank = True)
    text_of_comment = models.TextField("Напишите сообщение", null = True)
    date = models.DateField(auto_now = True)

    class Meta:
        verbose_name = "Чат населённого пункта"
        ordering = ["id"]
    def __str__(self):
        return f"{self.user_id}: {self.text_of_comment}"    


