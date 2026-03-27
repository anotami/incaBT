$(document).ready(function () {

  /* =====================================================
     WOW ANIMATIONS
  ===================================================== */
  try { new WOW().init(); } catch(e) {}

  /* =====================================================
     PRELOADER
  ===================================================== */
  $(window).on('load', function () {
    $('.preloader').fadeOut(600);
  });
  setTimeout(function () {
    $('.preloader').fadeOut(600);
  }, 3000);

  /* =====================================================
     GO-TOP button
  ===================================================== */
  $(window).on('scroll', function () {
    if ($(document).scrollTop() > 300) {
      $('.go-top').addClass('visible');
    } else {
      $('.go-top').removeClass('visible');
    }
  });

  $('.go-top').on('click', function (e) {
    e.preventDefault();
    $('html, body').animate({ scrollTop: 0 }, 700);
  });

  /* =====================================================
     SMOOTH SCROLL
  ===================================================== */
  $('.smoothScroll').on('click', function (e) {
    var target = this.hash;
    if (!target || target === '#') return;
    var $target = $(target);
    if ($target.length) {
      e.preventDefault();
      $('html, body').animate({ scrollTop: $target.offset().top - 56 }, 700, 'swing');
    }
  });

  /* =====================================================
     FORMULARIO INSCRIPCIÓN TALLER
  ===================================================== */
  $('#formTallerPage').on('submit', function (e) {
    e.preventDefault();

    var nombre  = $('#tfp-nombre').val().trim();
    var email   = $('#tfp-email').val().trim();
    var pais    = $('#tfp-pais').val().trim();
    var version = $('#tfp-version').val();
    var mensaje = $('#tfp-mensaje').val().trim();

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
      + '?subject=' + encodeURIComponent('Inscripción taller CALLADO BT — ' + nombre)
      + '&body='    + encodeURIComponent(cuerpo);

    $('#taller-form-success').show();

    setTimeout(function () {
      var a = document.createElement('a');
      a.href = mailto;
      document.body.appendChild(a);
      a.click();
      document.body.removeChild(a);
    }, 800);
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
     STICKY NAVBAR OPACITY
  ===================================================== */
  $(window).on('scroll', function () {
    var scrollTop = $(this).scrollTop();
    if (scrollTop > 80) {
      $('.navbar-default').css('background-color', 'rgba(26,37,47,0.98)');
    } else {
      $('.navbar-default').css('background-color', 'rgba(26,37,47,0.92)');
    }
  });

});
