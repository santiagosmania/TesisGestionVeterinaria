document.addEventListener('DOMContentLoaded', function () {
    var dniSelect = document.getElementById('dni');
    var pacienteSelect = document.getElementById('paciente');

    dniSelect.addEventListener('change', function () {
        var selectedDNI = dniSelect.value;

        // Realizar una solicitud AJAX para obtener los pacientes asociados al DNI seleccionado
        fetch('/get_pacientes_by_dni/' + selectedDNI + '/')
            .then(response => response.json())
            .then(data => {
                // Limpiar la lista actual de pacientes
                pacienteSelect.innerHTML = '';

                // Agregar las nuevas opciones de pacientes
                data.forEach(paciente => {
                    var option = document.createElement('option');
                    option.value = paciente.idpaciente;
                    option.textContent = paciente.nombreCompleto; // Ajusta esto según la estructura de tus datos
                    pacienteSelect.appendChild(option);
                });
            })
            .catch(error => console.error('Error:', error));
    });
});
