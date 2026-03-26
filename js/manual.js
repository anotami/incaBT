$(document).ready(function () {

  new WOW().init();

  /* Preloader */
  $(window).on('load', function () { $('.preloader').fadeOut(600); });
  setTimeout(function () { $('.preloader').fadeOut(600); }, 3000);

  /* Go-top */
  $(window).on('scroll', function () {
    $(document).scrollTop() > 300
      ? $('.go-top').addClass('visible')
      : $('.go-top').removeClass('visible');
  });
  $('.go-top').on('click', function (e) {
    e.preventDefault();
    $('html, body').animate({ scrollTop: 0 }, 700);
  });

  /* Navbar collapse mobile */
  $('.navbar-nav a').on('click', function () {
    if ($('.navbar-collapse').hasClass('in')) {
      $('.navbar-collapse').collapse('hide');
    }
  });

  /* Active nav link on scroll */
  $(window).on('scroll', function () {
    var scrollPos = $(document).scrollTop() + 100;
    $('.manual-section').each(function () {
      var id = $(this).attr('id');
      var top = $(this).offset().top;
      var bottom = top + $(this).outerHeight();
      if (scrollPos >= top && scrollPos < bottom) {
        $('.manual-nav-link').removeClass('active');
        $('.manual-nav-link[href="#' + id + '"]').addClass('active');
      }
    });
  });

  /* Smooth scroll for sidebar links */
  $('.manual-nav-link').on('click', function (e) {
    var target = $(this).attr('href');
    if ($(target).length) {
      e.preventDefault();
      $('html, body').animate({ scrollTop: $(target).offset().top - 80 }, 600);
    }
  });

});
