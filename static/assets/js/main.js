$(document).ready(function () {
  // sticky header
  // var mainHeader = document.querySelector('.main-header');
  // if(mainHeader){
  //   var stickyOffset = $(mainHeader).offset().top;
  // }
  // $(window).scroll(function(){
  //   var sticky = $('.main-header'),
  //       scroll = $(window).scrollTop();

  //   if (scroll >= stickyOffset) sticky.addClass('fixed');
  //   else sticky.removeClass('fixed');
  // });

  // slider
  $(".hero-slider").owlCarousel({
    items: 1,
    loop: true,
    autoplay: true,
    autoplayHoverPause: true,
    nav: true,
    navText: ['<i class="flaticon-next"></i>', '<i class="flaticon-next"></i>'],
    responsive: {
      0: {
        items: 1,
        nav: false,
      },
      600: {
        items: 1,
      },
      1000: {
        items: 1,
        nav: true,
        navText: ['<i class="flaticon-next"></i>', '<i class="flaticon-next"></i>'],
      },
    },
  });
  $(".products-slider").owlCarousel({
    margin: 24,
    loop: true,
    autoplay: true,
    autoplayHoverPause: true,
    dots: false,
    nav: true,
    navText: ['<i class="flaticon-next"></i>', '<i class="flaticon-next"></i>'],
    responsive: {
      0: {
        items: 1,
        nav: false,
      },
      600: {
        items: 2,
      },
      1000: {
        items: 3,
        nav: true,
        navText: ['<i class="flaticon-next"></i>', '<i class="flaticon-next"></i>'],
      },
    },
  });
  $(".alert").alert();
});
// hamburger menu
$(document).ready(function () {
  $(".hamburger-icon").on("click", function (e) {
    $(".hemburger-menu-block").addClass("show");
    e.stopPropagation();
  });
  $(".close-icon").on("click", function () {
    $(".hemburger-menu-block").removeClass("show");
  });
  $(document).on("click", function (e) {
    if ($(e.target).is(".hemburger-menu-block") === true) {
      $(".hemburger-menu-block").removeClass("show");
    }
  });

  $(".h-menu-ul li.dropdown").on("click", function () {
    $(this).toggleClass("show");
  });
});
// Products Filter menu
$(document).ready(function () {
  $(".filter_by_link").on("click", function (e) {
    $(".products-filter-menu-block").addClass("open");
    e.stopPropagation();
  });
  $(".pf-head  .close-icon").on("click", function () {
    $(".products-filter-menu-block").removeClass("open");
  });
  $(document).on("click", function (e) {
    if ($(e.target).is(".products-filter-menu-block") === true) {
      $(".products-filter-menu-block").removeClass("open");
    }
  });
});

// Cart Popup
$(document).ready(function () {
  $(".cart-icon a").on("click", function (e) {
    $(".cart-popup-block").addClass("open");
    e.stopPropagation();
  });
  $(".pf-head  .close-icon").on("click", function () {
    $(".cart-popup-block").removeClass("open");
  });
  $(document).on("click", function (e) {
    if ($(e.target).is(".cart-popup-block") === true) {
      $(".cart-popup-block").removeClass("open");
    }
  });
});
//Products Details Gallery
$(document).ready(function () {
  $(".product-gallery-block").owlCarousel({
    items: 1,
    loop: true,
    autoplay: true,
    thumbs: true,
    thumbsPrerendered: true,
  });
});
// product quantity button
$(document).ready(function () {
  var input = $("#quantity");
  $(".plus").on("click", function () {
    let inputValue = input.val();
    input.val(parseInt(inputValue) + 1);
  });
  $(".minus").on("click", function () {
    let inputValue = input.val();
    if (inputValue > 1) {
      input.val(parseInt(inputValue) - 1);
    }
  });
});
// country code dropdown
var input = document.querySelector("#validationPhnumber");
if (input) {
  window.intlTelInput(input);
}

// Example starter JavaScript for disabling form submissions if there are invalid fields
(function () {
  "use strict";

  // Fetch all the forms we want to apply custom Bootstrap validation styles to
  var forms = document.querySelectorAll(".needs-validation");

  // Loop over them and prevent submission
  Array.prototype.slice.call(forms).forEach(function (form) {
    form.addEventListener(
      "submit",
      function (event) {
        if (!form.checkValidity()) {
          event.preventDefault();
          event.stopPropagation();
        }
        form.classList.add("was-validated");
      },
      false
    );
  });
})();

// Scrool To Top
let backToBtn = document.getElementById("back-to-top-btn");
let headerSticky = document.getElementById("header");
window.onscroll = function () {
  scrollFunction();
};

function scrollFunction() {
  if (document.body.scrollTop > 20 || document.documentElement.scrollTop > 20) {
    backToBtn.style.display = "block";
    headerSticky.classList.add("fixed");
  } else {
    backToBtn.style.display = "none";
    headerSticky.classList.remove("fixed");
  }
}
function backToTop() {
  document.body.scrollTop = 0;
  document.documentElement.scrollTop = 0;
}
backToBtn.addEventListener("click", backToTop);

// chocolat lightbox
Chocolat(document.querySelectorAll(".chocolat-image"));
