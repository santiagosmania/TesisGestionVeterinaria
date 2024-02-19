$(document).ready(function () {
    $('#datepicker').change(function () {
        var selectedDate = new Date($('#datepicker').val());
        var dayOfWeek = selectedDate.getDay();
        var horas_disponibles = [];
  
        if (dayOfWeek == 5) {  // Si es sábado
            horas_disponibles = ['09:30', '10:00', '10:30', '11:00', '11:30', '12:00'];
        } else if (dayOfWeek != 6) {  // Para otros días que no sean domingo
            horas_disponibles = ['09:00', '09:30', '10:00', '10:30', '11:00', '11:30', '12:00', '12:30',
                                '13:00', '15:30', '16:00', '16:30', '17:00', '17:30', '18:00', '18:30'];
        }
  
        // Limpiar opciones actuales
        $('#timepicker').empty();
  
        // Agregar nuevas opciones
        for (var i = 0; i < horas_disponibles.length; i++) {
            var hora = horas_disponibles[i];
            $('#timepicker').append('<option value="' + hora + '">' + hora + '</option>');
        }
  
        // Desactivar el campo de hora si es domingo
        if (dayOfWeek == 6) {
            alert("No se permiten turnos los domingos. Por favor, seleccione otro día.");
            $('#timepicker').prop('disabled', true);
            $('#btnBuscar').prop('disabled', true);
            // Deshabilitar todos los botones de envío los domingos
            $('input[type="submit"]').prop('disabled', true);
        } else {
            $('#timepicker').prop('disabled', false);
            
            // Habilitar todos los botones de envío en otros días
            $('input[type="submit"]').prop('disabled', false);
            $('#btnBuscar').prop('disabled', false);
        }
    });
});