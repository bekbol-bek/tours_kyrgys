document.addEventListener('DOMContentLoaded', function () {
    const passwordInput = document.getElementById('id_password');
    const togglePasswordButton = document.getElementById('toggle-password');

    togglePasswordButton.addEventListener('click', function () {
        const type = passwordInput.type === 'password' ? 'text' : 'password';
        passwordInput.type = type;
        togglePasswordButton.textContent = type === 'password' ? 'Показать' : 'Скрыть';
    });
});