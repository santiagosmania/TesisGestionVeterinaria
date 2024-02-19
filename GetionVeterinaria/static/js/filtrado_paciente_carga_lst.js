$(document).ready(function() {
    // Deshabilitar y vaciar la lista desplegable idespecie al cargar la página
    $("#idespecie").empty().prop('enabled', true);

    // Manejar el evento de cambio en la lista desplegable idraza
    $("#idraza").change(function() {
      var selectedRaza = $(this).val();
      // Verificar si se seleccionó una raza antes de realizar la solicitud AJAX
      if (selectedRaza) {
        // Hacer una solicitud AJAX para obtener las especies asociadas a la raza seleccionada
        $.ajax({
          url: "{% url 'obtener_especies_por_raza' %}",  // Reemplaza esto con tu URL de vista para obtener especies por raza
          data: { 'raza': selectedRaza },
          dataType: 'json',
          success: function(data) {
            // Limpiar y habilitar la lista desplegable idespecie
            $("#idespecie").empty().prop('disabled', false);
            // Llenar la lista desplegable idespecie con las nuevas opciones
            $.each(data, function(index, especie) {
              $("#idespecie").append('<option value="' + especie.idespecie + '">' + especie.especie + '</option>');
            });
          },
          error: function(xhr, textStatus, errorThrown) {
            console.error("Error al obtener especies:", errorThrown);
            // Manejar el error según tus necesidades
          }
        });
      } else {
        // Si no se selecciona ninguna raza, dejar la lista desplegable idespecie vacía y deshabilitada
        $("#idespecie").empty().prop('disabled', true);
      }
    });
});
