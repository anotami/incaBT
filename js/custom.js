$(document).ready(function () {

  /* =====================================================
     VEGAS SLIDESHOW (hero background)
  ===================================================== */
  $.vegas('slideshow', {
    backgrounds: [
      { src: 'images/hero-bg1.svg' },
      { src: 'images/hero-bg2.svg' },
      { src: 'images/hero-bg3.svg' },
      { src: 'images/hero-bg4.svg' }
    ],
    delay:    5000,
    transition: 'fade',
    transitionDuration: 1000
  })('overlay', {
    src: 'https://cdnjs.cloudflare.com/ajax/libs/vegas/2.5.4/overlays/07.png'
  });

  /* =====================================================
     OWL CAROUSEL
  ===================================================== */
  $('.owl-carousel').owlCarousel({
    loop:      true,
    margin:    20,
    autoplay:  true,
    autoplayTimeout:  4000,
    autoplayHoverPause: true,
    nav:       true,
    dots:      true,
    responsive: {
      0:   { items: 1 },
      600: { items: 2 },
      992: { items: 3 }
    }
  });

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

  // Fallback: hide preloader after 3s even if load event fires late
  setTimeout(function () {
    $('.preloader').fadeOut(600);
  }, 3000);

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
      var currLink  = $(this);
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

});
