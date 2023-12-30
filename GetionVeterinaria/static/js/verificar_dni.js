const dniInput = document.querySelector('input[name="dni"]');
const dniError = document.getElementById('dni-error');
const dniExistError = document.getElementById('dni-exist');

dniInput.addEventListener('input', function () {
    if (dniInput.value.length < 8) {
        dniError.textContent = 'El DNI debe tener más de 8 caracteres.';
    } else {
        dniError.textContent = '';
        dniExistError.textContent = '';
    }
});
document.querySelector('form').addEventListener('submit', async function (event) {
    if (dniInput.value.length === 8) {
        event.preventDefault(); // Evita que el formulario se envíe por ahora

        try {
            // Realiza una llamada AJAX a tu backend para verificar la existencia del DNI
            const response = await fetch(`/verificar_dni/?dni=${dniInput.value}`);
            const data = await response.json();

            if (data.exists) {
                dniExistError.textContent = 'Este DNI ya está registrado.';
            } else {
                // Si no existe, continúa con el envío del formulario
                this.submit();
            }
        } catch (error) {
            console.error('Error en la llamada AJAX:', error);
        }
    }
});
