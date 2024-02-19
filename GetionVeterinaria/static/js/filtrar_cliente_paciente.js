document.addEventListener('DOMContentLoaded', function () {
    var idrazaSelect = document.getElementById('idraza');
    var idespecieSelect = document.getElementById('idespecie');

    idrazaSelect.addEventListener('change', function () {
        var selectedRaza = idrazaSelect.value;

        // Realizar una solicitud AJAX para obtener las especies asociadas a la raza seleccionada
        fetch('/get_especies_by_raza/' + selectedRaza + '/')
            .then(response => response.json())
            .then(data => {
                // Limpiar la lista actual de especies
                idespecieSelect.innerHTML = '';

                // Agregar las nuevas opciones de especies
                data.forEach(especie => {
                    var option = document.createElement('option');
                    option.value = especie.idespecie;
                    option.textContent = especie.especie;
                    idespecieSelect.appendChild(option);
                });
            })
            .catch(error => console.error('Error:', error));
    });
});
