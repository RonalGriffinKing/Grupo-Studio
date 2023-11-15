function toggleFlotante() {
    var scrollTop = $(window).scrollTop();
  
    // Muestra u oculta el botón según la posición del desplazamiento
    if (scrollTop > 200) {
      $('.flotante').fadeIn();
    } else {
      $('.flotante').fadeOut();
    }
  }
  
  // Función para desplazarse hacia arriba
  function scrollToTop() {
    $('body, html').animate({
      scrollTop: 0
    }, 300);
  }
  
  // Configuración inicial y eventos
  $(document).ready(function() {
    // Mostrar u ocultar el elemento flotante al cargar la página
    toggleFlotante();
  
    // Mostrar u ocultar el elemento flotante al desplazarse
    $(window).scroll(function() {
      toggleFlotante();
    });
  });