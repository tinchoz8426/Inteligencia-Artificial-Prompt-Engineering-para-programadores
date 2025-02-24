// Obtener los elementos del DOM
const form = document.getElementById('login-form');
const emailInput = document.getElementById('email');
const passwordInput = document.getElementById('password');
const errorMessage = document.getElementById('error-message');

// Función para validar el formulario
form.addEventListener('submit', function(event) {
    event.preventDefault(); // Evitar el envío del formulario

    // Obtener los valores ingresados
    const email = emailInput.value;
    const password = passwordInput.value;

    // Validar que no estén vacíos
    if (email === '' || password === '') {
        errorMessage.textContent = 'Por favor, completa todos los campos.';
        errorMessage.style.display = 'block';
        return;
    }

    // Simular validación de credenciales
    if (email === 'usuario@example.com' && password === 'password123') {
        alert('Inicio de sesión exitoso.');
        errorMessage.style.display = 'none';
        // Aquí podrías redirigir a otra página o continuar el flujo
    } else {
        errorMessage.textContent = 'Credenciales incorrectas. Inténtalo nuevamente.';
        errorMessage.style.display = 'block';
    }
});
