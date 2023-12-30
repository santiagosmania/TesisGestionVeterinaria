import difflib
from django.core.mail import send_mail
from django.contrib.auth import authenticate, login
from django.contrib import auth
from django.shortcuts import render, HttpResponse, redirect, HttpResponseRedirect
from .models import Persona, Paciente, Raza, Especie, sesion
from django.shortcuts import render, get_object_or_404
from datetime import datetime
from django.views import View
from django.http import JsonResponse
from .models import Event
from django.template.loader import render_to_string
from django.contrib import messages
import calendar
from django.views.decorators.csrf import csrf_exempt


def index(request):
    if request.method == 'POST':
        dni = request.POST.get('DNI')
        contrasena = request.POST.get('contrasena')
        try:
            usuario = sesion.objects.get(dni=dni)  # Cambia 'username' a 'dni'
            if contrasena == usuario.contrasena:  # Asegúrate de usar el campo correcto para la contraseña
                # Contraseña válida, redirige a una página de inicio
                return redirect('registro_clientes')
            else:
                # Contraseña incorrecta, muestra un mensaje de error o redirige a otra página
                return HttpResponse("Contraseña incorrecta")
        except sesion.DoesNotExist:
            # El usuario no existe en la base de datos
            return HttpResponse("Usuario no encontrado")

    return render(request, 'index.html')


# def Gestion_Stock(request):
#    return render(request, 'gestion_stock.html')


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
                chip = request.POST.get('chip', 0)  # Valor predeterminado de 0 si no se proporciona
                try:
                    chip = int(chip)
                except ValueError:
                    chip = 0  # Otra opción si el valor no es un entero válido

                fechana = request.POST.get('fechana',0)
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


def get_horas_registradas(self, request):
    # Obtiene la fecha seleccionada del formulario
    fecha_seleccionada = request.GET.get('fecha')
    # Consulta la base de datos para obtener las horas registradas para la fecha seleccionada
    horas_registradas = list(Event.objects.filter(
        fecha=fecha_seleccionada).values_list('hora', flat=True))

    return JsonResponse({'horas_registradas': horas_registradas}, safe=False)


class CreateEventView(View):
   
    def get(self, request, *args, **kwargs):
       
        datos = Persona.objects.all()
        # Obtener los parámetros de la URL
        fecha_seleccionada = request.GET.get('fecha')
        id_seleccionado = request.POST.get('idturno')

        # Obtener las horas disponibles
        horas_disponibles = ['09:00', '09:30', '10:00', '10:30', '11:00', '11:30', '12:00', '12:30',
                             '13:00', '13:30', '14:00', '14:30', '15:00', '15:30', '16:00', '16:30', '17:00', '17:30', '18:00', '18:30', '19:00']
        # Filtrar los eventos por fecha y ID
        turnos = Event.objects.filter(
            fecha=fecha_seleccionada, idturno=id_seleccionado)

        return render(request, 'turnero.html', {'datos': datos,'horas_disponibles': horas_disponibles, 'turnos': turnos})

    def post(self, request, *args, **kwargs):
        # Obtener los datos del formulario
    

        dni = request.POST.get('dni')
        email = request.POST.get('email')
        celular = request.POST.get('celular')
        fecha = request.POST.get('fecha')
        hora = request.POST.get('hora')
        tipo = request.POST.get('tipo')

        # Crear y guardar el evento en la base de datos
        turno = Event(dni=dni, email=email, celular=celular,
                      tipo=tipo, fecha=fecha, hora=hora)
        turno.save()

        # Enviar un correo electrónico
        subject = 'Veterinaria Full Campo'
        message = f'Su turno ha sido agendado.\nFecha: {fecha}\nHora: {hora}'
        from_email = 'santiago.smania@gmail.com'
        recipient_list = [email]
        send_mail(subject, message, from_email, recipient_list)

        horas_disponibles = ['09:00', '09:30', '10:00', '10:30', '11:00', '11:30', '12:00', '12:30',
                             '13:00', '13:30', '14:00', '14:30', '15:00', '15:30', '16:00', '16:30', '17:00', '17:30', '18:00', '18:30', '19:00']

        return render(request, 'turnero.html', {'success_message': 'Evento creado y correo electrónico enviado', 'horas_disponibles': horas_disponibles})
   

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


chatbot_data = {
    "Cuales son los horarios de atencion de la veterinaria": "Hola! Nuestros horarios de atencion son de Lunes a Viernes de 09:00 a 13:00 - 15:00 a 19:00 y Sabado de 09:00 a 13:00",
    "que dias atienden": "Hola! Nuestros horarios de atencion son de Lunes a Viernes de 09:00 a 13:00 - 15:00 a 19:00 y Sabado de 09:00 a 13:00",
    "Cual es la ubicacion del local": "Hola! nuestra direccion es: Km 9, RP E53, Pajas Blancas, Cordoba Capital",
    "Como hago para sacar turno": "Hola! Para sacar turno te podes comunicar con nosotros a nuestro telefono 03513143611 o por esta misma web",
    "Cual es el telefono de la veterinaria": "Nuestro telefono es: 03513143611",
    "Cual es el telefono del local": "Nuestro telefono es: 03513143611",
    "Que servicios ofrecen": "Hola! en Full Campo nos especializamos en la atencion y cuidado de animales pequeños y grandes",
    "Hacen visitas a domicilio": "Hola! ofrecemos visitas a domicilio",
    "Tengo un caballo como hago para que lo vea un veterinario": "Hola! ofrecemos visitas a domicilio",
    "Tengo una vaca como hago para que lo vea un veterinario": "Hola! ofrecemos visitas a domicilio",
    "Tengo un equino como hago para que lo vea un veterinario": "Hola! ofrecemos visitas a domicilio",
    "Tengo un perro como hago para que lo vea un veterinario": "Hola! Podes acercarte a nuestro local en: Km 9, RP E53, Pajas Blancas, Cordoba Capital u ofrecemos visitas a domicilio",
    "Tengo un gato como hago para que lo vea un veterinario": "Hola! Podes acercarte a nuestro local en: Km 9, RP E53, Pajas Blancas, Cordoba Capital u ofrecemos visitas a domicilio",
    "Atienden animales de granja": "Hola! Nos dedicamos a la atencion de pequeños y grandes animales.",
    "Atienden animales domesticos": "Hola! Nos dedicamos a la atencion de pequeños y grandes animales.",
    "Atienden perros": "Hola! Nos dedicamos a la atencion de pequeños y grandes animales.",
    "Atienden animales gatos": "Hola! Nos dedicamos a la atencion de pequeños y grandes animales.",
    "Atienden vacas": "Hola! Nos dedicamos a la atencion de pequeños y grandes animales.",
    "Atienden aves": "Hola! No atendemos aves.",
    "Atienden pajaros": "Hola! No atendemos aves.",
    "Atienden loros": "Hola! No atendemos aves.",
    "Atienden tortugas": "Hola! No atendemos reptiles.",
    "Atienden iguana": "Hola! No atendemos reptiles.",
    "Atienden viboras": "Hola! No atendemos reptiles.",
    "Atienden peces": "Hola! No atendemos peces.",
    "Atienden pirañas": "Hola! No atendemos peces.",
    "Atienden urgencias 24 hs ": "Hola! Nuestros horarios de atencion son de Lunes a Viernes de 09:00 a 13:00 - 15:00 a 19:00 y Sabado de 09:00 a 13:00",
    "Hacen peluqueria": "Hola! no ofrecemos servicio de peluqueria aun",
    "Hacen cirugias": "Hola! no hacemos cirugias aun, solo atencion y cuidados de animales pequeños y grandes",
    "Venden alimentos": "Hola! Vendemos una amplia gama de alimentos tales como preparados sintéticos para animales domésticos y de granja (balanceado, comida en lata o sobre, aditamentos, etc.).También encontramos alimentos naturales (alfalfa, avena, alpiste, etc.). Te esperamos en nuestro local!",
    "Venden balanceado": "Hola! Vendemos una amplia gama de alimentos tales como preparados sintéticos para animales domésticos y de granja (balanceado, comida en lata o sobre, aditamentos, etc.).También encontramos alimentos naturales (alfalfa, avena, alpiste, etc.). Te esperamos en nuestro local!",
    "Venden alfalfa": "Hola! Vendemos una amplia gama de alimentos tales como preparados sintéticos para animales domésticos y de granja (balanceado, comida en lata o sobre, aditamentos, etc.).También encontramos alimentos naturales (alfalfa, avena, alpiste, etc.). Te esperamos en nuestro local!",
    "Venden avena": "Hola! Vendemos una amplia gama de alimentos tales como preparados sintéticos para animales domésticos y de granja (balanceado, comida en lata o sobre, aditamentos, etc.).También encontramos alimentos naturales (alfalfa, avena, alpiste, etc.). Te esperamos en nuestro local!",
    "Venden alpiste": "Hola! Vendemos una amplia gama de alimentos tales como preparados sintéticos para animales domésticos y de granja (balanceado, comida en lata o sobre, aditamentos, etc.).También encontramos alimentos naturales (alfalfa, avena, alpiste, etc.). Te esperamos en nuestro local!",
    "Venden comida en lata": "Hola! Vendemos una amplia gama de alimentos tales como preparados sintéticos para animales domésticos y de granja (balanceado, comida en lata o sobre, aditamentos, etc.).También encontramos alimentos naturales (alfalfa, avena, alpiste, etc.). Te esperamos en nuestro local!",
    "Venden alimentos de granja": "Hola! Vendemos una amplia gama de alimentos tales como preparados sintéticos para animales domésticos y de granja (balanceado, comida en lata o sobre, aditamentos, etc.). También encontramos alimentos naturales (alfalfa, avena, alpiste, etc.). Te esperamos en nuestro local!",
    "Venden Shampoo de perros": "Hola! Vendemos una amplia gama de productos estéticos, como ser, shampoo, crema de enjuague, perfumes, corta uñas, cepillos, rasquetas, etc. Te esperamos en nuestro local!",
    "Venden Shampoo de gatos": "Hola! Vendemos una amplia gama de productos estéticos, como ser, shampoo, crema de enjuague, perfumes, corta uñas, cepillos, rasquetas, etc. Te esperamos en nuestro local!",
    "Venden crema de enjuague": "Hola! Vendemos una amplia gama de productos estéticos, como ser, shampoo, crema de enjuague, perfumes, corta uñas, cepillos, rasquetas, etc. Te esperamos en nuestro local!",
    "Venden perfume de perros": "Hola! Vendemos una amplia gama de productos estéticos, como ser, shampoo, crema de enjuague, perfumes, corta uñas, cepillos, rasquetas, etc.Te esperamos en nuestro local!",
    "Venden perfume de gatos": "Hola! Vendemos una amplia gama de productos estéticos, como ser, shampoo, crema de enjuague, perfumes, corta uñas, cepillos, rasquetas, etc. Te esperamos en nuestro local!",
    "Venden cepillos": "Hola! Vendemos una amplia gama de productos estéticos, como ser, shampoo, crema de enjuague, perfumes, corta uñas, cepillos, rasquetas, etc. Te esperamos en nuestro local!",
    "Venden rasquetas": "Hola! Vendemos una amplia gama de productos estéticos, como ser, shampoo, crema de enjuague, perfumes, corta uñas, cepillos, rasquetas, etc.Te esperamos en nuestro local!",
    "Venden cremas": "Hola! Vendemos una amplia gama de productos farmacéuticos como de medicamentos, cremas, ungüentos, pipetas, inyectables y otros semejantes.Te esperamos en nuestro local!",
    "Venden ungüentos": "Hola! Vendemos una amplia gama de productos farmacéuticos como de medicamentos, cremas, ungüentos, pipetas, inyectables y otros semejantes.Te esperamos en nuestro local!",
    "Venden desparasitante": "Hola! Vendemos una amplia gama de productos farmacéuticos como de medicamentos, cremas, ungüentos, pipetas, inyectables y otros semejantes.Te esperamos en nuestro local!",
    "Venden pipetas": "Hola! Vendemos una amplia gama de productos farmacéuticos como de medicamentos, cremas, ungüentos, pipetas, inyectables y otros semejantes.Te esperamos en nuestro local!",
    "Venden carretas": "Hola! vendemos una amplia gama de productos para el mantenimiento de los espacios comunes principalmente para animales grandes o de granja, como: rastrillos, carretas, delantales, guantes, baldes, abono, entre otros.Te esperamos en nuestro local!",
    "Venden delantales": "Hola! vendemos una amplia gama de productos para el mantenimiento de los espacios comunes principalmente para animales grandes o de granja, como: rastrillos, carretas, delantales, guantes, baldes, abono, entre otros.Te esperamos en nuestro local!",
    "Venden baldes": "Hola! vendemos una amplia gama de productos para el mantenimiento de los espacios comunes principalmente para animales grandes o de granja, como: rastrillos, carretas, delantales, guantes, baldes, abono, entre otros.Te esperamos en nuestro local!",
    "Venden abono": "Hola! vendemos una amplia gama de productos para el mantenimiento de los espacios comunes principalmente para animales grandes o de granja, como: rastrillos, carretas, delantales, guantes, baldes, abono, entre otros.Te esperamos en nuestro local!",
    "Como hago para comprar balanceado": "Hola! para comprar balanceado podes acercarte a nuestro local en: Km 9, RP E53, Pajas Blancas, Cordoba Capital o podes comunicarte con nosotros al telefono:03513143611",
    "Como hago para comprar comida": "Hola! para comprar podes acercarte a nuestro local en: Km 9, RP E53, Pajas Blancas, Cordoba Capital o podes comunicarte con nosotros al telefono:03513143611",
    "Venden medicamentos para perros": "Hola! vendemos medicamentos para pequeños y grandes animales. Te esperamos en nuestro local!",
    "Venden correas": "Hola! contamos con una gran variedad de productos de pet-shop. Te esperamos en nuestro local!",
    "que productos comercializan": "Hola! Ofrecemos una amplia gama de productos, tales como: Farmacos, de mantenimiento, Alimentos,Accesorios,Esteticos entre otros. Te esperamos en nuestro local!",
    "que productos venden": "Hola! Ofrecemos una amplia gama de productos, tales como: Farmacos, de mantenimiento, Alimentos,Accesorios,Esteticos entre otros. Te esperamos en nuestro local!",
    "Hacen ventas mayoristas": "Hola! Hacemos ventas minoristas. ",
    "Se puede realizar encargos de productos especiales": "Hola! Para hacer tu pedido comuncate con nosotros al telefono: 03513143611 ",
    "Ofrecen servicio de traslado": "Hola! no ofrecemos servicio de traslado. Ofrecemos atencion a domicilio",
    "Hacen radiografias": "Hola! no ofrecemos ese servicio",
    "Tienen catalogo de los productos": "Hola no ofrecemos catalogo. Para comprar llamanos al telefono: 03513143611 o veni a visitarnos a la direccion Km 9, RP E53, Pajas Blancas, Cordoba Capital",
}


def get_best_match(user_message):
    match = difflib.get_close_matches(
        user_message.lower(), chatbot_data.keys(), n=1, cutoff=0.6)
    return match[0] if match else None


@csrf_exempt
def chatbot(request):
    if request.method == 'POST':
        user_message = request.POST.get('user_message')
        bot_response = chatbot_data.get(user_message, None)

        if bot_response is None:
            best_match = get_best_match(user_message)
            if best_match:
                bot_response = chatbot_data[best_match]
            else:
                bot_response = "Lo siento, no entiendo esa pregunta."

        return render(request, 'chat.html', {'bot_response': bot_response})

    return render(request, 'chat.html')


# def modificar_cliente(request):
#     opciones = Opcion.objects.all()
#     return render(request, 'modificar.html', {
#         'opciones': opciones
#         })


# def modificar_cliente(request):
#     table = Clientes(Person.objects.all())

#     return render(request, "modificar_cliente.html", {
#         "table": table
#     })

# def Registro_Clientes(request):
#     if request.method == 'POST':
#         accion = request.POST.get('accion')

#         if accion == 'registrar':
#             dni = request.POST.get('DNI')
#             nombre = request.POST.get('nombre')
#             contraseña = request.POST.get('contraseña')

#             persona = Persona(nombre=nombre, contraseña=contraseña, DNI=dni)
#             persona.save()

#         elif accion == 'modificar':
#             dni_modificar = request.POST.get('dni_modificar')
#             nuevo_nombre = request.POST.get('nuevo_nombre')
#             nueva_contraseña = request.POST.get('nueva_contraseña')

#             # Buscar la persona en la base de datos
#             try:
#                 persona = Persona.objects.get(DNI=dni_modificar)
#                 persona.nombre = nuevo_nombre
#                 persona.contraseña = nueva_contraseña
#                 persona.save()
#                 mensaje = "Datos modificados con éxito."
#             except Persona.DoesNotExist:
#                 mensaje = "La persona con ese DNI no existe."

#             # Agregar el mensaje a la respuesta para mostrarlo en la plantilla
#             context = {'mensaje': mensaje}
#             return render(request, 'registro_clientes.html', context)

#     return render(request, 'registro_clientes.html')


def crear_historialclinico(request):
    return render(request, 'crear_historialclinico.html')


def modificar_historialclinico(request):
    return render(request, 'modificar_historialclinico.html')


def Historial_Clinico(request):
    return render(request, 'historial_clinico.html')
