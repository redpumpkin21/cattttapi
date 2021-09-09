from django.urls import path, include
from rest_framework import routers
from cat.views import CatViewSet


router = routers.DefaultRouter()

router.register(r'cats', CatViewSet) 

print(router)


urlpatterns = [
    path("", include(router.urls))
]