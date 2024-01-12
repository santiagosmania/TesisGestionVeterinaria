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
#from app.views import CreateEventView
from app.views import PruebaFecha

import app.views
from django.conf import settings
from django.conf.urls.static import static



urlpatterns = [
    path('admin/', admin.site.urls),
    path('', app.views.index, name="index"),
    path('registro-clientes/', app.views.Registro_Clientes, name="registro_clientes"),
    path('modificar/', app.views.Modificar_Clientes, name="modificar_clientes"),
    path('registro-pacientes/', app.views.Registro_Pacientes, name="registro_pacientes"),
    path('modificar-pacientes/', app.views.Modificar_Pacientes, name="modificar_pacientes"),
    path('verificar_dni/', app.views.verificar_dni, name='verificar_dni'),
    path('verificar_turno/', app.views.reservar_turno, name='reservar_turno'),
    path('historial-clinico/', app.views.Historial_clinico, name="historial_clinico"),
    path('crear-historialclinico/<int:idpaciente>/', app.views.Crear_Historial_Clinico, name='crear_historialclinico'),
    path('obtener_horas_ocupadas/', app.views.obtener_horas_ocupadas, name='obtener_horas_ocupadas'),
    path('modificar-historialclinico/<int:idhistorial>/<int:idvacuna>/<int:idpeso>/<int:idpaciente>/<int:idespecie>/<int:idraza>/<int:idexamenc>/', app.views.modificar_historialclinico, name="modificar_historialclinico"),
    path('chat/', app.views.chatbot, name="chat_bot"),
    path('turnero/', app.views.Turnero, name="turnero"),
    path('ver-historialclinico/<int:idhistorial>/<int:idvacuna>/<int:idpeso>/<int:idpaciente>/<int:idespecie>/<int:idraza>/<int:idexamenc>/', app.views.Ver_HistorialClinico, name='ver_historialclinico'),
    
   # path('create-event/', CreateEventView.as_view(), name='create_event'),
    path('filtrar-turnos/', PruebaFecha.as_view(), name='filtrar_turnos'),
    path('get_especies_by_raza/<int:idraza>/', app.views.get_especies_by_raza, name='get_especies_by_raza'),
    path('get_pacientes_by_dni/<int:dni>/', app.views.get_pacientes_by_dni, name='get_pacientes_by_dni'),
    path('get_pacientes_by_dni2/<int:dni>/', app.views.get_pacientes_by_dni2, name='get_pacientes_by_dni2'),
    path('get_historial_info/<int:idpaciente>/', app.views.get_historial_info, name='get_historial_info'),
    path('get_historial_by_paciente/<int:idpaciente>/', app.views.get_historial_by_paciente, name='get_historial_by_paciente'),
    
]
    
    #path('reserve/<int:year>/<int:month>/<int:day>/', app.views.reserve_view, name='reserve_view'),


if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    

