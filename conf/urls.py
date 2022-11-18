from django.contrib import admin
from django.urls import path
from administracion.views import lal

urlpatterns = [
    path('admin/', admin.site.urls),
    path('first/', lal),
]

