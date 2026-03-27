/* Preloader: se esconde apenas el DOM está listo (garantizado) */
setTimeout(function () { $('.preloader').fadeOut(600); }, 800);
$(window).on('load', function () { $('.preloader').fadeOut(400); });

$(document).ready(function () {

  /* =====================================================
     VEGAS SLIDESHOW (hero background) — API Vegas 2.x
  ===================================================== */
  if (typeof $.fn.vegas !== 'undefined') {
    $('body').vegas({
      slides: [
        { src: 'images/hero-bg1.svg' },
        { src: 'images/hero-bg2.svg' },
        { src: 'images/hero-bg3.svg' },
        { src: 'images/hero-bg4.svg' }
      ],
      delay:              5000,
      transition:         'fade',
      transitionDuration: 1000,
      overlay:            true
    });
  }

  /* =====================================================
     OWL CAROUSEL
  ===================================================== */
  if ($('.owl-carousel').length) {
    $('.owl-carousel').owlCarousel({
      loop:               true,
      margin:             20,
      autoplay:           true,
      autoplayTimeout:    4000,
      autoplayHoverPause: true,
      nav:                true,
      dots:               true,
      responsive: {
        0:   { items: 1 },
        600: { items: 2 },
        992: { items: 3 }
      }
    });
  }

  /* =====================================================
     WOW ANIMATIONS
  ===================================================== */
  try { new WOW().init(); } catch(e) {}

  /* =====================================================
     SMOOTH SCROLL
  ===================================================== */
  $('.smoothScroll').on('click', function (e) {
    var target = this.hash;
    if (!target || target === '#') return;
    var $target = $(target);
    if ($target.length) {
      e.preventDefault();
      $('html, body').animate(
        { scrollTop: $target.offset().top - 56 },
        700,
        'swing'
      );
    }
  });

  /* =====================================================
     NAVBAR ACTIVE STATE ON SCROLL
  ===================================================== */
  $(window).on('scroll', function () {
    var scrollPos = $(document).scrollTop();

    $('.nav a.smoothScroll').each(function () {
      var currLink   = $(this);
      var refElement = $(currLink.attr('href'));
      if (refElement.length &&
          refElement.position().top <= scrollPos + 70 &&
          refElement.position().top + refElement.height() > scrollPos + 70) {
        $('.nav li').removeClass('active');
        currLink.parent().addClass('active');
      }
    });

    /* GO-TOP button visibility */
    if (scrollPos > 300) {
      $('.go-top').addClass('visible');
    } else {
      $('.go-top').removeClass('visible');
    }
  });

  /* =====================================================
     NAVBAR COLLAPSE ON MOBILE LINK CLICK
  ===================================================== */
  $('.navbar-nav a').on('click', function () {
    if ($('.navbar-collapse').hasClass('in')) {
      $('.navbar-collapse').collapse('hide');
    }
  });

  /* =====================================================
     MODAL TALLER — envío por mailto
  ===================================================== */
  $('#formTaller').on('submit', function (e) {
    e.preventDefault();

    var nombre  = $('#ft-nombre').val().trim();
    var email   = $('#ft-email').val().trim();
    var pais    = $('#ft-pais').val().trim();
    var version = $('#ft-version').val();
    var mensaje = $('#ft-mensaje').val().trim();

    if (!nombre || !email) return;

    var versionTexto = version === 'si'
      ? 'Sí, tengo versión anterior (solicito 50% dto.)'
      : 'No, es mi primera vez';

    var cuerpo = [
      'Nombre: ' + nombre,
      'Email: ' + email,
      'País/Ciudad: ' + (pais || 'No especificado'),
      'Versión anterior: ' + versionTexto,
      '',
      'Mensaje:',
      mensaje || '(sin mensaje adicional)'
    ].join('\n');

    var mailto = 'mailto:acordatemidire@gmail.com'
      + '?subject=' + encodeURIComponent('Consulta taller CALLADO BT — ' + nombre)
      + '&body='    + encodeURIComponent(cuerpo);

    $('#ft-success').show();

    setTimeout(function () {
      window.location.href = mailto;
    }, 800);
  });

});
