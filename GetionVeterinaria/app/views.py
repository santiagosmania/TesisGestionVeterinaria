import difflib
from django.core.mail import send_mail
from django.utils import timezone
from django.contrib.auth import authenticate, login
from django.contrib import auth
from django.shortcuts import render, HttpResponse, redirect, HttpResponseRedirect
from .models import Persona, Paciente, Raza, Especie, Sesion, Vacunas, ExamenCli, Peso, Historial
from django.shortcuts import render, get_object_or_404
from datetime import datetime
from datetime import date
from django.views import View
from django.http import JsonResponse
from .models import Event
from django.template.loader import render_to_string
from django.contrib import messages
import calendar
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_GET
from django.views.decorators.csrf import csrf_exempt
from django.http import Http404
import pytz
from decimal import Decimal
from django.views.decorators.http import require_POST
from google.cloud import dialogflow
import uuid
from django.contrib.auth import logout
import json
from google.oauth2 import service_account


def chat(request):
    if request.method == 'POST':
        input_text = request.POST.get('input_text', '')
        project_id = 'veterinaria-vuxd'
        
        # Genera un identificador único para la sesión
        session_id = str(uuid.uuid4())

        response_text = detect_intent(project_id, input_text, session_id)
        return render(request, 'chat.html', {'response_text': response_text})
    return render(request, 'chat.html')
    
  
    
def detect_intent(project_id, text, session_id):
    credentials = service_account.Credentials.from_service_account_file(
        'C:/Users/santi/OneDrive/Escritorio/GestionVeterinaria/GetionVeterinaria/static/veterinaria-vuxd-f21bd360974b.json'
    )

    session_client = dialogflow.SessionsClient(credentials=credentials)
    session = session_client.session_path(project_id, session_id)

    text_input = dialogflow.TextInput(text=text, language_code='es')  # Cambia según el idioma que desees
    query_input = dialogflow.QueryInput(text=text_input)

    response = session_client.detect_intent(request={'session': session, 'query_input': query_input})

    return response.query_result.fulfillment_text



def index(request):
    if request.method == 'POST':
        dni = request.POST.get('DNI')
        contrasena = request.POST.get('contrasena')
        try:
            usuario = Sesion.objects.get(dni=dni)  # Cambia 'username' a 'dni'
            if contrasena == usuario.contrasena:  # Asegúrate de usar el campo correcto para la contraseña
                # Contraseña válida, redirige a una página de inicio
                return redirect('registro_clientes')
            else:
                # Contraseña incorrecta, muestra un mensaje de error o redirige a otra página
                return HttpResponse("Contraseña incorrecta")
        except Sesion.DoesNotExist:
            # El usuario no existe en la base de datos
            return HttpResponse("Usuario no encontrado")

    return render(request, 'index.html')

def Logout(request):
    logout(request)  # Cierra la sesión del usuario
    # Redirige a la página de inicio de sesión o a donde prefieras
    return redirect('index') 

def Registro_Sesion(request):

    error_message = None

    if request.method == 'POST':
        dni = request.POST.get('DNI')

        if len(dni) < 8:
            error_message = 'El DNI debe tener 8 caracteres.'
        elif Sesion.objects.filter(dni=dni).exists():
            error_message = 'Ya existe un registro con este DNI.'
        else:
            contrasena = request.POST.get('contrasena')
      
            sesion = Sesion(
                dni=dni,
                contrasena=contrasena
            )
            messages.success(request, "El cliente se cargo exitosamente")
            sesion.save()

    return render(request, 'crear_sesion.html', {'error_message': error_message})



def Modificar_Sesion(request):
    datos = Sesion.objects.all()
    if request.method == 'POST':
        dni = request.POST.get('DNI')
        contrasena = request.POST.get('contrasena')
        if dni:
            try:
                sesion = Sesion.objects.get(dni=dni)
                sesion.contrasena = contrasena
                sesion.save()
            except Sesion.DoesNotExist:
                    pass

            # Limpia los campos estableciendo persona en None después de actualizar
        

    return render(request, 'modificar_sesion.html', {'datos': datos})




def Registro_Clientes(request):
    error_message = None

    if request.method == 'POST':
        dni = request.POST.get('dni')

        if len(dni) < 8:
            error_message = 'El DNI debe tener 8 caracteres.'
        elif Persona.objects.filter(dni=dni).exists():
            error_message = 'Ya existe un registro con este DNI.'
        else:
            apellido = request.POST.get('apellido')
            nombre = request.POST.get('nombre')
            direccion = request.POST.get('direccion')
            telefono = request.POST.get('telefono')
            email = request.POST.get('email')
            estado = request.POST.get('estado')

            persona = Persona(
                dni=dni,
                apellido=apellido,
                nombre=nombre,
                direccion=direccion,
                telefono=telefono,
                email=email,
                estado=estado
            )
            messages.success(request, "El cliente se cargo exitosamente")
            persona.save()

    return render(request, 'registro_clientes.html', {'error_message': error_message})


def verificar_dni(request):
    dni = request.GET.get('dni', None)

    if dni is not None:
        exists = Persona.objects.filter(dni=dni).exists()
        return JsonResponse({'exists': exists})

    return JsonResponse({'error': 'No se proporcionó un DNI válido.'})


def verificar_dni_nombre(request):
    dni = request.GET.get('dni')
    nombre = request.GET.get('nombre')

    # Verifica si existe un paciente con el mismo DNI y nombre
    exists = Paciente.objects.filter(dni=dni, nombre=nombre).exists()

    # Devuelve la respuesta en formato JSON
    return JsonResponse({'exists': exists})


def reservar_turno(request):
    # Obtiene la fecha seleccionada del formulario
    fecha_seleccionada = request.GET.get('fecha')
    # Consulta la base de datos para obtener las horas registradas para la fecha seleccionada
    horas_registradas = list(Event.objects.filter(
        fecha=fecha_seleccionada).values_list('hora_registrada', flat=True))

    return JsonResponse({'horas_registradas': horas_registradas}, safe=False)


def Modificar_Clientes(request):
    datos = Persona.objects.all()
    persona = None

    if request.method == 'POST':
        dni = request.POST.get('dni')

        # se llama al value y al nombre del boton y si es igual entra al if
        if 'accion' in request.POST and request.POST['accion'] == 'Buscar':
            if dni:
                try:
                    persona = Persona.objects.get(dni=dni)
                except Persona.DoesNotExist:
                    pass
        elif 'accion' in request.POST and request.POST['accion'] == 'Actualizar':
            apellido = request.POST.get('apellido')
            nombre = request.POST.get('nombre')
            direccion = request.POST.get('direccion')
            telefono = request.POST.get('telefono')
            email = request.POST.get('email')
            estado = request.POST.get('estado')

            if dni:
                try:
                    persona = Persona.objects.get(dni=dni)
                    persona.apellido = apellido
                    persona.nombre = nombre
                    persona.direccion = direccion
                    persona.telefono = telefono
                    persona.email = email
                    persona.estado = estado
                    persona.save()
                except Persona.DoesNotExist:
                    pass

            # Limpia los campos estableciendo persona en None después de actualizar
            persona = None

    return render(request, 'modificar.html', {'datos': datos, 'persona': persona})


def Modificar_Pacientes(request):
    datos = Paciente.objects.all()
    datosraza = Raza.objects.all()
    datosespecie = Especie.objects.all()
    paciente = None

    if request.method == 'POST':
        id = request.POST.get('idpaciente')

        if 'accion' in request.POST and request.POST['accion'] == 'Buscar':
            if id:
                try:
                    paciente = Paciente.objects.get(idpaciente=id)
                except Paciente.DoesNotExist:
                    pass
        elif 'accion' in request.POST and request.POST['accion'] == 'Actualizar':
            dni = request.POST.get('dni')
            nombre = request.POST.get('nombre')
            raza_id = request.POST.get('idraza')
            sexo = request.POST.get('sexo')
            estado = request.POST.get('estado')
            seniaspart = request.POST.get('seniaspart')
            chip = request.POST.get('chip')
            especie_id = request.POST.get('idespecie')
            fechana = request.POST.get('fechana')

            fechana_formatted = None
            if fechana:
                try:
                    fechana_formatted = datetime.strptime(
                        fechana, '%d/%m/%Y').strftime('%Y-%m-%d')
                except ValueError:
                    pass

            if id:
                paciente_instance = get_object_or_404(Paciente, idpaciente=id)

                # Buscar o crear una instancia de Persona con el DNI proporcionado
                persona_instance, created = Persona.objects.get_or_create(
                    dni=dni)

                # Buscar la instancia de Raza
                try:
                    raza = Raza.objects.get(pk=raza_id)
                except Raza.DoesNotExist:
                    raza = None

                # Buscar la instancia de Especie
                try:
                    especie = Especie.objects.get(pk=especie_id)
                except Especie.DoesNotExist:
                    especie = None

                if raza and especie:
                    paciente_instance.dni = persona_instance
                    paciente_instance.nombre = nombre
                    paciente_instance.idraza = raza
                    paciente_instance.sexo = sexo
                    paciente_instance.estado = estado
                    paciente_instance.seniaspart = seniaspart
                    paciente_instance.chip = chip
                    paciente_instance.idespecie = especie
                    paciente_instance.fechana = fechana_formatted
                    paciente_instance.save()

            paciente = None

    return render(request, 'modificar_pacientes.html', {'datos': datos, 'paciente': paciente, 'datosraza': datosraza, 'datosespecie': datosespecie})








def Crear_Historial_Clinico(request,idpaciente):
    mensaje_error = None
    datos = Paciente.objects.all()
    datosV = Vacunas.objects.all()
    datosExam = ExamenCli.objects.all()
    datosRaza = Raza.objects.all()
    datosEspecie = Especie.objects.all()

    if request.method == 'POST':
        try:
            
            timezone_argentina = pytz.timezone('America/Argentina/Buenos_Aires')
            fecha_actual_argentina = timezone.now().astimezone(timezone_argentina)
            fecha = fecha_actual_argentina.date()
            print('hola', fecha)
           
            fechadesp = request.POST.get('fechadesp')
            fechacelo = request.POST.get('fechacelo')
            fechapart = request.POST.get('fechapart')
            productodesp = request.POST.get('productodesp')
            lotev = request.POST.get('lotev')
            estirilizado = request.POST.get('estirilizado')
            consulta = request.POST.get('consulta')
            hallazgo = request.POST.get('hallazgo')
            ganglios = request.POST.get('ganglios')
            mucosas = request.POST.get('mucosas')
            temperatura = request.POST.get('temperatura')
            cardiaca = request.POST.get('cardiaca')
            pulso = request.POST.get('pulso')
            respiratoria = request.POST.get('respiratoria')
            peso = request.POST.get('peso')
            idvacuna = request.POST.get('idvacuna')

            paciente = Paciente.objects.get(pk=idpaciente)
            vacuna = Vacunas.objects.get(pk=idvacuna)

            
            paciente = Paciente.objects.get(pk=idpaciente)
           
           

         
            if fechadesp and '/' in fechadesp:
                fechadesp = datetime.strptime(fechadesp, '%d/%m/%Y').strftime('%Y-%m-%d')
            if fechacelo and '/' in fechacelo:
                 fechacelo = datetime.strptime(fechacelo, '%d/%m/%Y').strftime('%Y-%m-%d')
            if fechapart and '/' in fechapart:
                fechapart = datetime.strptime(fechapart, '%d/%m/%Y').strftime('%Y-%m-%d')

            peso_instance = Peso(peso=peso)
            peso_instance.save()

            examenc = ExamenCli(
                ganglios=ganglios,
                mucosas=mucosas,
                temperatura=temperatura,
                cardiaca=cardiaca,
                pulso=pulso,
                respiratoria=respiratoria
            )
            examenc.save()

            historial = Historial(
                idpaciente=paciente,
                fecha=fecha,
                productodesp=productodesp,
                fechadesp=fechadesp,
                idvacuna=vacuna,
                lotev=lotev,
                fechacelo=fechacelo,
                fechapart=fechapart,
                estirilizado=estirilizado,
                consulta=consulta,
                hallazgo=hallazgo,
                idexamenc=examenc,
                idpeso=peso_instance,
            
            )
           
          
            historial.save()

            print("Información del historial insertada correctamente.")
           
            print("Nombre de la Vacuna:", vacuna.vacuna)

        except ValueError as e:
             mensaje_error = f"Error al procesar los datos: {e}"

    return render(request, 'crear_historial_clinico.html', {'mensaje_error': mensaje_error, 'datos': datos, 'datosV': datosV, 'idpaciente': idpaciente, 'datosRaza': datosRaza, 'datosEspecie': datosEspecie})


def Registro_Pacientes(request):
    datos = Persona.objects.all()
    datosraza = Raza.objects.all()
    datosespecie = Especie.objects.all()
    mensaje_error = None

    if request.method == 'POST':
        dni = request.POST.get('dni')
        nombre = request.POST.get('nombre')

        try:
            persona = Persona.objects.get(dni=dni)
        except Persona.DoesNotExist:
            mensaje_error = "La persona con el DNI proporcionado no existe."
        else:
            if not Paciente.objects.filter(dni=persona, nombre=nombre).exists():
                sexo = request.POST.get('sexo')
                estado = request.POST.get('estado')
                seniaspart = request.POST.get('seniaspart')

                # Manejo del campo 'chip'
                # Valor predeterminado de 0 si no se proporciona
                chip = request.POST.get('chip', 0)
                try:
                    chip = int(chip)
                except ValueError:
                    chip = 0  # Otra opción si el valor no es un entero válido

                fechana = request.POST.get('fechana', 0)
                idraza = request.POST.get('idraza')
                raza = Raza.objects.get(pk=idraza)
                idespecie = request.POST.get('idespecie')
                especie = Especie.objects.get(pk=idespecie)

                try:
                    fechana_formatted = datetime.strptime(
                        fechana, '%d/%m/%Y').strftime('%Y-%m-%d')
                except ValueError:
                    fechana_formatted = None

                paciente = Paciente(
                    dni=persona,
                    nombre=nombre,
                    sexo=sexo,
                    estado=estado,
                    seniaspart=seniaspart,
                    chip=chip,
                    idespecie=especie,
                    idraza=raza,
                    fechana=fechana_formatted,
                )

                paciente.save()
            else:
                mensaje_error = "Ya existe un paciente con el mismo DNI y nombre."

    return render(request, 'registro_pacientes.html', {'datos': datos, 'datosraza': datosraza, 'datosespecie': datosespecie, 'mensaje_error': mensaje_error})


def get_historial_info(request, idpaciente):
    # Suponiendo que 'idpaciente' es un campo válido en el modelo 'Historial'
    historial = get_object_or_404(Historial, paciente__idpaciente=idpaciente)
    
    # Suponiendo que 'fecha' es un campo en el modelo 'Historial'
    data = {
        'fecha': historial.fecha,
        # Agrega más campos según sea necesario
    }

    return JsonResponse(data)


def Historial_clinico(request):
    datos = Persona.objects.all()
    datospaciente = Paciente.objects.all()
    datoshistorial = Historial.objects.all()

    clientes = None
    historiales = None
    pacientes = None
    selected_paciente_id = None
    vectoridpacientehist = [1, 2, 3, 4, 5]
    paciente = None  # Initialize paciente variable
    idpaci = None  # Initialize idpaci variable
    idpaciente = None  # Initialize selected_value variable

    if request.POST.get('accion') == 'Agregar':
       idpaciente = request.POST.get('idpaciente')
      
         
       return redirect('crear_historialclinico', idpaciente=idpaciente)

    if request.method == 'POST':
        selected_dni = request.POST.get('dni')
        selected_paciente_id = request.POST.get('idpaciente')
        
        try:
            idpaciente = int(request.POST.get('idpaci'))
            paciente = get_object_or_404(Paciente, pk=idpaciente)
            idpaci = idpaciente  # Pasamos el idpaci al contexto
        except (Paciente.DoesNotExist, ValueError):
            raise Http404("Paciente does not exist or invalid ID")

        

        if selected_dni:
            clientes = Persona.objects.filter(dni=selected_dni)
            pacientes = Paciente.objects.filter(dni__in=clientes)

        if selected_paciente_id:
            historiales = Historial.objects.filter(idpaciente__in=pacientes)
        else:
            historiales = None

    historial_idpaciente = historiales[0].idpaciente if historiales and historiales.exists() else None
    paciente_idpaciente = datospaciente[0].idpaciente if datospaciente and datospaciente.exists() else None

    context = {
        'clientes': clientes,
        'pacientes': pacientes,
        'historiales': historiales,
        'datos': datos,
        'datospaciente': datospaciente,
        'datoshistorial': datoshistorial,
        'paciente': paciente,
        'vectoridpacientehist': vectoridpacientehist,
        'historial_idpaciente': historial_idpaciente,
        'paciente_idpaciente': paciente_idpaciente,
        'idpaci': idpaci,
        'idpaciente': idpaciente,  # Pasamos idpaci al contexto
       
    }

    return render(request, 'historial_clinico.html', context)
    




def get_pacientes_by_dni(request, dni):
    pacientes = Paciente.objects.filter(
        dni=dni).values('idpaciente', 'nombre')
    print('Pacientes:', pacientes)  # Añade esta línea para imprimir los pacientes en la consola
    return JsonResponse(list(pacientes), safe=False)

def get_pacientes_by_dni2(request, dni):
    pacientes = Paciente.objects.filter(
        dni=dni).values('idpaciente', 'nombre')
    print('Pacientes:', pacientes)  # Añade esta línea para imprimir los pacientes en la consola
    return JsonResponse(list(pacientes), safe=False)


def get_historial_by_paciente(request, idpaciente):
    historial = Historial.objects.filter(
        idpaciente=idpaciente).values('idhistorial', 'fecha')
    print('Pacientes:', historial)  # Añade esta línea para imprimir los pacientes en la consola
    return JsonResponse(list(historial), safe=False)



def get_especies_by_raza(request, idraza):
    especies = Especie.objects.filter(
        idraza_id=idraza).values('idespecie', 'especie')
    return JsonResponse(list(especies), safe=False)


def obtener_horas_ocupadas(request):
    if request.method == 'POST':
        fecha_seleccionada = request.POST.get('fecha', None)

        if fecha_seleccionada:
            # Aquí debes reemplazar 'Event' con el modelo de tu aplicación que almacena los eventos
            horas_ocupadas = Event.objects.filter(
                fecha=fecha_seleccionada).values_list('hora', flat=True)

            return JsonResponse({'horas_ocupadas': list(horas_ocupadas)})

    return JsonResponse({'error': 'Invalid request'})


def Turnero(request):
    datos = Event.objects.all()
    error_message = None

    # Vector de horas disponibles
    #horas_disponibles = ['09:00', '09:30', '10:00', '10:30', '11:00', '11:30', '12:00', '12:30',
    #                     '13:00', '15:30', '16:00', '16:30', '17:00', '17:30', '18:00', '18:30']

    fecha_predeterminada = date.today()

    if request.method == 'POST':
        dni = request.POST.get('dni')
        email = request.POST.get('email')
        celular = request.POST.get('celular')
        fecha = request.POST.get('fecha')  # Así es como deberías obtener la fecha del formulario
        tipo = request.POST.get('tipo')
        hora_seleccionada = request.POST.get('hora')

        # Asigna el valor del campo de fecha seleccionada
        fecha_predeterminada = fecha

        # Obtener las horas ocupadas para la fecha seleccionada
        horas_ocupadas = list(Event.objects.filter(
            fecha=fecha).values_list('hora', flat=True))

        # Verifica si la hora seleccionada está disponible
        if hora_seleccionada in horas_ocupadas:
            messages.error(
                request, f"La hora {hora_seleccionada} ya está ocupada. Por favor, elige otra hora.")
        else:
            # Agrega el nuevo evento a la base de datos
            turno = Event(dni=dni, email=email, celular=celular,
                          tipo=tipo, fecha=fecha, hora=hora_seleccionada)
            messages.success(request, "El turno se agendó exitosamente.")
            turno.save()

            # Envía el correo electrónico de confirmación
            subject = 'Veterinaria Full Campo'
            message = f'Su turno ha sido agendado.\nFecha: {fecha}\nHora: {hora_seleccionada}'
            from_email = 'santiago.smania@gmail.com'
            recipient_list = [email]
            send_mail(subject, message, from_email, recipient_list)

    return render(request, 'turnero.html', {
        'error_message': error_message,
        #'horas_disponibles': horas_disponibles,
        'datos': datos,
        'fecha_predeterminada': fecha_predeterminada,  # Pasa el vector al contexto
    })


class PruebaFecha(View):
    def get(self, request, *args, **kwargs):
        fecha_seleccionada = request.GET.get('fecha')
        turnos = Event.objects.filter(fecha=fecha_seleccionada)
        print(turnos)

        # Renderizar solo el HTML de los turnos filtrados como una cadena
        turnos_html = render_to_string('turnero.html', {'turnos': turnos})

        # Devolver los turnos filtrados como una respuesta JSON
        return JsonResponse({'turnero_html': turnos_html})


class PruebaFecha(View):
    def get(self, request, *args, **kwargs):
        fecha_seleccionada = request.GET.get('fecha')
        turnos = Event.objects.filter(fecha=fecha_seleccionada)
        print(turnos)
        # Renderizar solo el HTML de los turnos filtrados como una cadena
        turnos_html = render_to_string('turnero.html', {'turnos': turnos})

        # Devolver los turnos filtrados como una respuesta JSON
        return JsonResponse({'turnero_html': turnos_html})


# chatbot_data = {
#     "Cuales son los horarios de atencion de la veterinaria": "Hola! Nuestros horarios de atencion son de Lunes a Viernes de 09:00 a 13:00 - 15:00 a 19:00 y Sabado de 09:00 a 13:00",
#     "que dias atienden": "Hola! Nuestros horarios de atencion son de Lunes a Viernes de 09:00 a 13:00 - 15:00 a 19:00 y Sabado de 09:00 a 13:00",
#     "Cual es la ubicacion del local": "Hola! nuestra direccion es: Km 9, RP E53, Pajas Blancas, Cordoba Capital",
#     "Como hago para sacar turno": "Hola! Para sacar turno te podes comunicar con nosotros a nuestro telefono 03513143611 o por esta misma web",
#     "Cual es el telefono de la veterinaria": "Nuestro telefono es: 03513143611",
#     "Cual es el telefono del local": "Nuestro telefono es: 03513143611",
#     "Que servicios ofrecen": "Hola! en Full Campo nos especializamos en la atencion y cuidado de animales pequeños y grandes",
#     "Hacen visitas a domicilio": "Hola! ofrecemos visitas a domicilio",
#     "Tengo un caballo como hago para que lo vea un veterinario": "Hola! ofrecemos visitas a domicilio",
#     "Tengo una vaca como hago para que lo vea un veterinario": "Hola! ofrecemos visitas a domicilio",
#     "Tengo un equino como hago para que lo vea un veterinario": "Hola! ofrecemos visitas a domicilio",
#     "Tengo un perro como hago para que lo vea un veterinario": "Hola! Podes acercarte a nuestro local en: Km 9, RP E53, Pajas Blancas, Cordoba Capital u ofrecemos visitas a domicilio",
#     "Tengo un gato como hago para que lo vea un veterinario": "Hola! Podes acercarte a nuestro local en: Km 9, RP E53, Pajas Blancas, Cordoba Capital u ofrecemos visitas a domicilio",
#     "Atienden animales de granja": "Hola! Nos dedicamos a la atencion de pequeños y grandes animales.",
#     "Atienden animales domesticos": "Hola! Nos dedicamos a la atencion de pequeños y grandes animales.",
#     "Atienden perros": "Hola! Nos dedicamos a la atencion de pequeños y grandes animales.",
#     "Atienden animales gatos": "Hola! Nos dedicamos a la atencion de pequeños y grandes animales.",
#     "Atienden vacas": "Hola! Nos dedicamos a la atencion de pequeños y grandes animales.",
#     "Atienden aves": "Hola! No atendemos aves.",
#     "Atienden pajaros": "Hola! No atendemos aves.",
#     "Atienden loros": "Hola! No atendemos aves.",
#     "Atienden tortugas": "Hola! No atendemos reptiles.",
#     "Atienden iguana": "Hola! No atendemos reptiles.",
#     "Atienden viboras": "Hola! No atendemos reptiles.",
#     "Atienden peces": "Hola! No atendemos peces.",
#     "Atienden pirañas": "Hola! No atendemos peces.",
#     "Atienden urgencias 24 hs ": "Hola! Nuestros horarios de atencion son de Lunes a Viernes de 09:00 a 13:00 - 15:00 a 19:00 y Sabado de 09:00 a 13:00",
#     "Hacen peluqueria": "Hola! no ofrecemos servicio de peluqueria aun",
#     "Hacen cirugias": "Hola! no hacemos cirugias aun, solo atencion y cuidados de animales pequeños y grandes",
#     "Venden alimentos": "Hola! Vendemos una amplia gama de alimentos tales como preparados sintéticos para animales domésticos y de granja (balanceado, comida en lata o sobre, aditamentos, etc.).También encontramos alimentos naturales (alfalfa, avena, alpiste, etc.). Te esperamos en nuestro local!",
#     "Venden balanceado": "Hola! Vendemos una amplia gama de alimentos tales como preparados sintéticos para animales domésticos y de granja (balanceado, comida en lata o sobre, aditamentos, etc.).También encontramos alimentos naturales (alfalfa, avena, alpiste, etc.). Te esperamos en nuestro local!",
#     "Venden alfalfa": "Hola! Vendemos una amplia gama de alimentos tales como preparados sintéticos para animales domésticos y de granja (balanceado, comida en lata o sobre, aditamentos, etc.).También encontramos alimentos naturales (alfalfa, avena, alpiste, etc.). Te esperamos en nuestro local!",
#     "Venden avena": "Hola! Vendemos una amplia gama de alimentos tales como preparados sintéticos para animales domésticos y de granja (balanceado, comida en lata o sobre, aditamentos, etc.).También encontramos alimentos naturales (alfalfa, avena, alpiste, etc.). Te esperamos en nuestro local!",
#     "Venden alpiste": "Hola! Vendemos una amplia gama de alimentos tales como preparados sintéticos para animales domésticos y de granja (balanceado, comida en lata o sobre, aditamentos, etc.).También encontramos alimentos naturales (alfalfa, avena, alpiste, etc.). Te esperamos en nuestro local!",
#     "Venden comida en lata": "Hola! Vendemos una amplia gama de alimentos tales como preparados sintéticos para animales domésticos y de granja (balanceado, comida en lata o sobre, aditamentos, etc.).También encontramos alimentos naturales (alfalfa, avena, alpiste, etc.). Te esperamos en nuestro local!",
#     "Venden alimentos de granja": "Hola! Vendemos una amplia gama de alimentos tales como preparados sintéticos para animales domésticos y de granja (balanceado, comida en lata o sobre, aditamentos, etc.). También encontramos alimentos naturales (alfalfa, avena, alpiste, etc.). Te esperamos en nuestro local!",
#     "Venden Shampoo de perros": "Hola! Vendemos una amplia gama de productos estéticos, como ser, shampoo, crema de enjuague, perfumes, corta uñas, cepillos, rasquetas, etc. Te esperamos en nuestro local!",
#     "Venden Shampoo de gatos": "Hola! Vendemos una amplia gama de productos estéticos, como ser, shampoo, crema de enjuague, perfumes, corta uñas, cepillos, rasquetas, etc. Te esperamos en nuestro local!",
#     "Venden crema de enjuague": "Hola! Vendemos una amplia gama de productos estéticos, como ser, shampoo, crema de enjuague, perfumes, corta uñas, cepillos, rasquetas, etc. Te esperamos en nuestro local!",
#     "Venden perfume de perros": "Hola! Vendemos una amplia gama de productos estéticos, como ser, shampoo, crema de enjuague, perfumes, corta uñas, cepillos, rasquetas, etc.Te esperamos en nuestro local!",
#     "Venden perfume de gatos": "Hola! Vendemos una amplia gama de productos estéticos, como ser, shampoo, crema de enjuague, perfumes, corta uñas, cepillos, rasquetas, etc. Te esperamos en nuestro local!",
#     "Venden cepillos": "Hola! Vendemos una amplia gama de productos estéticos, como ser, shampoo, crema de enjuague, perfumes, corta uñas, cepillos, rasquetas, etc. Te esperamos en nuestro local!",
#     "Venden rasquetas": "Hola! Vendemos una amplia gama de productos estéticos, como ser, shampoo, crema de enjuague, perfumes, corta uñas, cepillos, rasquetas, etc.Te esperamos en nuestro local!",
#     "Venden cremas": "Hola! Vendemos una amplia gama de productos farmacéuticos como de medicamentos, cremas, ungüentos, pipetas, inyectables y otros semejantes.Te esperamos en nuestro local!",
#     "Venden ungüentos": "Hola! Vendemos una amplia gama de productos farmacéuticos como de medicamentos, cremas, ungüentos, pipetas, inyectables y otros semejantes.Te esperamos en nuestro local!",
#     "Venden desparasitante": "Hola! Vendemos una amplia gama de productos farmacéuticos como de medicamentos, cremas, ungüentos, pipetas, inyectables y otros semejantes.Te esperamos en nuestro local!",
#     "Venden pipetas": "Hola! Vendemos una amplia gama de productos farmacéuticos como de medicamentos, cremas, ungüentos, pipetas, inyectables y otros semejantes.Te esperamos en nuestro local!",
#     "Venden carretas": "Hola! vendemos una amplia gama de productos para el mantenimiento de los espacios comunes principalmente para animales grandes o de granja, como: rastrillos, carretas, delantales, guantes, baldes, abono, entre otros.Te esperamos en nuestro local!",
#     "Venden delantales": "Hola! vendemos una amplia gama de productos para el mantenimiento de los espacios comunes principalmente para animales grandes o de granja, como: rastrillos, carretas, delantales, guantes, baldes, abono, entre otros.Te esperamos en nuestro local!",
#     "Venden baldes": "Hola! vendemos una amplia gama de productos para el mantenimiento de los espacios comunes principalmente para animales grandes o de granja, como: rastrillos, carretas, delantales, guantes, baldes, abono, entre otros.Te esperamos en nuestro local!",
#     "Venden abono": "Hola! vendemos una amplia gama de productos para el mantenimiento de los espacios comunes principalmente para animales grandes o de granja, como: rastrillos, carretas, delantales, guantes, baldes, abono, entre otros.Te esperamos en nuestro local!",
#     "Como hago para comprar balanceado": "Hola! para comprar balanceado podes acercarte a nuestro local en: Km 9, RP E53, Pajas Blancas, Cordoba Capital o podes comunicarte con nosotros al telefono:03513143611",
#     "Como hago para comprar comida": "Hola! para comprar podes acercarte a nuestro local en: Km 9, RP E53, Pajas Blancas, Cordoba Capital o podes comunicarte con nosotros al telefono:03513143611",
#     "Venden medicamentos para perros": "Hola! vendemos medicamentos para pequeños y grandes animales. Te esperamos en nuestro local!",
#     "Venden correas": "Hola! contamos con una gran variedad de productos de pet-shop. Te esperamos en nuestro local!",
#     "que productos comercializan": "Hola! Ofrecemos una amplia gama de productos, tales como: Farmacos, de mantenimiento, Alimentos,Accesorios,Esteticos entre otros. Te esperamos en nuestro local!",
#     "que productos venden": "Hola! Ofrecemos una amplia gama de productos, tales como: Farmacos, de mantenimiento, Alimentos,Accesorios,Esteticos entre otros. Te esperamos en nuestro local!",
#     "Hacen ventas mayoristas": "Hola! Hacemos ventas minoristas. ",
#     "Se puede realizar encargos de productos especiales": "Hola! Para hacer tu pedido comuncate con nosotros al telefono: 03513143611 ",
#     "Ofrecen servicio de traslado": "Hola! no ofrecemos servicio de traslado. Ofrecemos atencion a domicilio",
#     "Hacen radiografias": "Hola! no ofrecemos ese servicio",
#     "Tienen catalogo de los productos": "Hola no ofrecemos catalogo. Para comprar llamanos al telefono: 03513143611 o veni a visitarnos a la direccion Km 9, RP E53, Pajas Blancas, Cordoba Capital",
# }


# def get_best_match(user_message):
#     match = difflib.get_close_matches(
#         user_message.lower(), chatbot_data.keys(), n=1, cutoff=0.6)
#     return match[0] if match else None


# @csrf_exempt
# def chatbot(request):
#     if request.method == 'POST':
#         user_message = request.POST.get('user_message')
#         bot_response = chatbot_data.get(user_message, None)

#         if bot_response is None:
#             best_match = get_best_match(user_message)
#             if best_match:
#                 bot_response = chatbot_data[best_match]
#             else:
#                 bot_response = "Lo siento, no entiendo esa pregunta."

#         return render(request, 'chat.html', {'bot_response': bot_response})

#     return render(request, 'chat.html')




def modificar_historialclinico(request, idhistorial, idvacuna, idpeso, idpaciente, idespecie, idraza, idexamenc):
    datosVacunas = Vacunas.objects.all()
    
   
    id_historial = int(idhistorial)
    historial = Historial.objects.get(idhistorial=id_historial)
    id_vacuna = int(idvacuna)
    vacunas = Vacunas.objects.get(idvacuna=id_vacuna)
    id_peso = int(idpeso)
    peso = Peso.objects.get(idpeso=id_peso) #*esta es la variable que almacena el objeto
    id_paciente = int(idpaciente)
    paciente = Paciente.objects.get(idpaciente=id_paciente)
    id_especie = int(idespecie)
    especie = Especie.objects.get(idespecie=id_especie)
    id_raza = int(idraza)
    raza = Raza.objects.get(idraza=id_raza)
    id_examenc = int(idexamenc)
    examen = ExamenCli.objects.get(idexamenc=id_examenc)

    if request.method == 'POST':
            # Actualiza los modelos con los datos del formulario

            fechadesp = request.POST.get('fechadesp')
            fechadesp = datetime.strptime(fechadesp, '%d/%m/%Y').strftime('%Y-%m-%d')
            productodesp = request.POST.get('productodesp')
            lotev = request.POST.get('lotev')
            fechacelo = request.POST.get('fechacelo')
            fechacelo = datetime.strptime(fechacelo, '%d/%m/%Y').strftime('%Y-%m-%d')
            fechapart = request.POST.get('fechapart')
            fechapart = datetime.strptime(fechapart, '%d/%m/%Y').strftime('%Y-%m-%d')

            nuevo_peso_str = request.POST.get('peso') #se pone un nombre diferente ya que el codigo puede interpretar que nos referimos a la 
                                                      #peso que almacena el objeto *
            nuevo_peso_str = ''.join(filter(str.isdigit, nuevo_peso_str))
            estirilizado = request.POST.get('estirilizado')
            consulta = request.POST.get('consulta')
            hallazgo = request.POST.get('hallazgo')
            ganglios = request.POST.get('ganglios')
            mucosas = request.POST.get('mucosas')
            temperatura = request.POST.get('temperatura')
            cardiaca = request.POST.get('cardiaca')
            pulso = request.POST.get('pulso')
            respiratoria = request.POST.get('respiratoria')
            idvacuna = request.POST.get('idvacuna')
            vacuna = Vacunas.objects.get(pk=idvacuna)

            nuevo_peso = Decimal(nuevo_peso_str) if nuevo_peso_str else None
            peso.peso = nuevo_peso
            historial.fechadesp = fechadesp
            historial.productodesp = productodesp
            historial.lotev = lotev
            historial.fechacelo = fechacelo
            historial.fechapart = fechapart
            historial.estirilizado = estirilizado
            historial.consulta = consulta
            historial.hallazgo = hallazgo
            examen.ganglios = ganglios
            examen.mucosas = mucosas
            examen.temperatura = temperatura
            examen.cardiaca = cardiaca
            examen.pulso = pulso
            examen.respiratoria = respiratoria
            
            historial.idvacuna = vacuna

           
            # Guarda los cambios
            peso.save()
            historial.save()
            
            paciente.save()
            examen.save()

            

    return render(request, 'modificar_historialclinico.html', {'historial': historial, 'vacunas': vacunas, 'peso': peso, 'paciente': paciente, 'especie': especie, 'raza': raza, 'examen': examen, 'datosVacunas': datosVacunas})
   

def convertir_a_formato_correcto(fecha_str, formato_entrada, formato_salida):
    if fecha_str:
        try:
            fecha = datetime.strptime(fecha_str, formato_entrada).strftime(formato_salida)
            return fecha
        except ValueError:
            pass
    return None



def Ver_HistorialClinico(request, idhistorial, idvacuna, idpeso, idpaciente, idespecie, idraza, idexamenc):
    try:
        id_historial = int(idhistorial)
        historial = Historial.objects.get(idhistorial=id_historial)
        id_vacuna = int(idvacuna)
        vacunas = Vacunas.objects.get(idvacuna=id_vacuna)
        id_peso = int(idpeso)
        peso = Peso.objects.get(idpeso=id_peso)
        id_paciente = int(idpaciente)
        paciente = Paciente.objects.get(idpaciente=id_paciente)
        id_especie = int(idespecie)
        especie = Especie.objects.get(idespecie=id_especie)
        id_raza = int(idraza)
        raza = Raza.objects.get(idraza=id_raza)
        #id_examenc = int(idexamenc)
        #examen = ExamenCli.objects.get(idexamenc=id_examenc)
        id_examenc = int(idexamenc)
        examen = ExamenCli.objects.get(idexamenc=id_examenc)

        print("Datos del historial:", historial.__dict__)
        return render(request, 'ver_historialclinico.html', {'historial': historial, 'vacunas': vacunas, 'peso': peso, 'paciente': paciente, 'especie': especie, 'raza': raza, 'examen':  examen})
    except (ValueError, TypeError, Historial.DoesNotExist):
        return redirect('ver_historialclinico')