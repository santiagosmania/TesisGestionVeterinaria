$(document).ready(function () {
    var obtenerHorasOcupadasURL = "{% url 'obtener_horas_ocupadas' %}";

    $('#datepicker').change(function () {
        var selectedDate = new Date($('#datepicker').val());
        var dayOfWeek = selectedDate.getDay();
        var horas_disponibles = [];

        // Obtener la fecha en formato YYYY-MM-DD para comparar con la base de datos
        var formattedDate = selectedDate.toISOString().split('T')[0];

        if (dayOfWeek == 5) {  // Si es sábado
            horas_disponibles = ['09:30', '10:00', '10:30', '11:00', '11:30', '12:00'];
        } else if (dayOfWeek != 6) {  // Para otros días que no sean domingo
            horas_disponibles = ['09:00', '09:30', '10:00', '10:30', '11:00', '11:30', '12:00', '12:30',
                                 '13:00', '15:30', '16:00', '16:30', '17:00', '17:30', '18:00', '18:30'];
        }

        // Limpiar opciones actuales
        $('#timepicker').empty();

        // Realizar solicitud AJAX para obtener las horas ocupadas
        $.ajax({
            url: obtenerHorasOcupadasURL,
            method: 'POST',
            data: { fecha: formattedDate },
            success: function (data) {
                // Agregar las opciones al elemento select
                for (var i = 0; i < horas_disponibles.length; i++) {
                    var hora = horas_disponibles[i];
                    var option = $('<option value="' + hora + '">' + hora + '</option>');

                    // Resaltar visualmente las horas ocupadas
                    if ($.inArray(hora, data.horas_ocupadas) !== -1) {
                        option.addClass('hora-ocupada');
                    }

                    $('#timepicker').append(option);
                }
            },
            error: function (error) {
                console.log(error);
            }
        });

        // Desactivar el campo de hora si es domingo
        if (dayOfWeek == 6) {
            alert("No se permiten turnos los domingos. Por favor, seleccione otro día.");
            $('#timepicker').prop('disabled', true);
        } else {
            $('#timepicker').prop('disabled', false);
        }
    });
});

// Otro código adicional si lo necesitas
