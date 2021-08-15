from django.urls import path
from .views import *
from rest_framework.routers import SimpleRouter

urlpatterns = [
    path('village/<str:name>/', GetAllData.as_view(), name = 'village'),
    path('village/add_photos/<str:name>', AddPhotos.as_view(), name = 'add_photo'),
    path('village/chart/<str:name>/', ChartView.as_view(), name = "add_comment")
]

#  DRF-API-URLS
router = SimpleRouter()
router.register('api/villages', VillageViewSet)
router.register('api/village_images', VillagePicturesViewSet)
router.register('api/village_news', VillageNewsViewSet)

urlpatterns += router.urls