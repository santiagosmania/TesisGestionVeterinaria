$(document).ready(function () {
    // Función para manejar el cambio en la selección de hora
    $('#timepicker').change(function () {
      var selectedHour = $(this).val(); // Obtener la hora seleccionada

      // Si deseas realizar alguna acción basada en la hora seleccionada, puedes hacerlo aquí
      console.log('Hora seleccionada:', selectedHour);
    });
});

document.addEventListener("DOMContentLoaded", function () {
    // Manejar el clic en el botón de filtrar turnos
    document.getElementById("filtrar-turnos").addEventListener("click", function () {
      // Obtener la fecha seleccionada
      const fechaFiltro = document.getElementById("datepicker-filter").value;

      // Realizar una solicitud AJAX al servidor para obtener los turnos filtrados
      fetch(`/turnero.html/?fecha=${fechaFiltro}`, {
        method: "GET"
      })
        .then(response => response.text())
        .then(data => {
          // Actualizar el contenido de la página con los turnos filtrados
          document.getElementById("turnos-filtrados").innerHTML = data;
        })
        .catch(error => console.error(error));
    });
});