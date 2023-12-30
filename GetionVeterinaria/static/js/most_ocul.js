const showPasswordCheckbox = document.getElementById('showPassword');
const passwordField = document.getElementById('password');

showPasswordCheckbox.addEventListener('change', function () {
    passwordField.type = showPasswordCheckbox.checked ? 'text' : 'password';
});