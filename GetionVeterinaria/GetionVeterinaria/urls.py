"""
URL configuration for GetionVeterinaria project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from app.views import CreateEventView
from app.views import PruebaFecha

import app.views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', app.views.index, name="index"),
 
    #path('gestion-stock/', app.views.Gestion_Stock, name="gestion_stock"),
    #path('Iniciar-Sesion/', app.views.IniciarSesion, name="Iniciar_Sesion"),
    path('registro-clientes/', app.views.Registro_Clientes, name="registro_clientes"),
    path('modificar/', app.views.Modificar_Clientes, name="modificar_clientes"),
    path('registro-pacientes/', app.views.Registro_Pacientes, name="registro_pacientes"),
    path('modificar-pacientes/', app.views.Modificar_Pacientes, name="modificar_pacientes"),
    path('verificar_dni/', app.views.verificar_dni, name='verificar_dni'),
    path('verificar_turno/', app.views.reservar_turno, name='reservar_turno'),
    #path('verificar_turno/', app.views.reservar_turno, name='reservar_turno'),
    path('historial-clinico/', app.views.Historial_Clinico, name="historial_clinico"),
    path('crear-historialclinico/', app.views.crear_historialclinico, name="crear_historialclinico"),
    path('modificar-historialclinico/', app.views.modificar_historialclinico, name="modificar_historialclinico"),
    path('chat/', app.views.chatbot, name="chat_bot"),
    path('create-event/', CreateEventView.as_view(), name='create_event'),
    path('filtrar-turnos/', PruebaFecha.as_view(), name='filtrar_turnos'),
    #path('reserve/<int:year>/<int:month>/<int:day>/', app.views.reserve_view, name='reserve_view'),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    

