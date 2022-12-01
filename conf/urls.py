from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static
from administracion import views
from django.conf import settings
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home,name='home'),
    path('loginbus/',views.data_form_buses,name="data_create_buses"),
    path('listabus/',views.data_read_buses,name="data_read_buses"),
]

urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
