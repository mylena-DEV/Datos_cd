from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from DjangoDat.views import DatosViewSet

router = DefaultRouter()
router.register(r'datos', DatosViewSet)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/',include(router.urls))
]
