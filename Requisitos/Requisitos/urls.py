from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from DjangoDat.views import DatosViewSet, CiudadViewSet


router = DefaultRouter()
router.register(r'datos', DatosViewSet)
router.register(r'ciudad', CiudadViewSet)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/',include(router.urls))
]
