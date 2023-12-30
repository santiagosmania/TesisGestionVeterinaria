const dniInput = document.querySelector('input[name="dni"]');
const nombreInput = document.querySelector('input[name="nombre"]');
const dniError = document.getElementById('dni-error');
const nombreExistError = document.getElementById('nombre-exist');

dniInput.addEventListener('input', function () {
    if (dniInput.value.length < 8) {
        dniError.textContent = 'El DNI debe tener más de 8 caracteres.';
    } else {
        dniError.textContent = '';
        nombreExistError.textContent = '';
    }
});

document.querySelector('form').addEventListener('submit', async function (event) {
    if (dniInput.value.length === 8) {
        event.preventDefault(); // Evita que el formulario se envíe por ahora

        try {
            // Realiza una llamada AJAX para verificar si ya existe un paciente con el mismo DNI y nombre
            const dni = dniInput.value;
            const nombre = nombreInput.value;

            const response = await fetch(`/verificar_dni_nombre/?dni=${dni}&nombre=${nombre}`);
            const data = await response.json();

            if (data.exists) {
                nombreExistError.textContent = 'Este DNI ya está registrado con el mismo nombre.';
            } else {
                // Si no existe, continúa con el envío del formulario
                this.submit();
            }
        } catch (error) {
            console.error('Error en la llamada AJAX:', error);
        }
    }
});
