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
    path('loginchofer/',views.data_form_choferes,name="data_create_choferes"),
    path('listachofer/',views.data_read_choferes,name="data_read_choferes"),
    path('loginatractivo/',views.data_form_atractivos,name="data_create_atractivos"),
    path('listaatractivo/',views.data_read_atractivos,name="data_read_atractivos"),
    path('listaatractivo/eliminarAtractivo/<nombre>',views.eliminarAtractivo,name="data_delete_atractivos"),
    path('viaje/listaviaje/', views.renderViajes, name="viajes"),
    path("viaje/<int:post_id>", views.viajes_detail, name="viajes_detail"),
    path('viaje/loginviaje/',views.data_form_viajes,name="data_create_viajes"),
    path('viaje/listaviaje/eliminarViaje/<nombre>',views.eliminarViaje,name="data_delete_viaje"),
    path('loginrecorrido/',views.data_form_recorridos,name="data_create_recorridos"),
]


urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
