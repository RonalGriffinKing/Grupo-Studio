// script.js

// Asegúrate de que el DOM ha cargado completamente
document.addEventListener('DOMContentLoaded', function() {
    // Obtén el botón por su ID
    let btn = document.getElementById("Enviar");
    
    // Añade un evento de clic al botón
    btn.addEventListener("click", function() {
        // Utiliza SweetAlert2 para mostrar una alerta
        Swal.fire({
            title: '¡Hola!',
            text: 'Esto es una alerta de SweetAlert2',
            icon: 'success',
            confirmButtonText: 'Aceptar'
        });
    });
});
