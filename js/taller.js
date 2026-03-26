$(document).ready(function () {

  /* =====================================================
     WOW ANIMATIONS
  ===================================================== */
  new WOW().init();

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
