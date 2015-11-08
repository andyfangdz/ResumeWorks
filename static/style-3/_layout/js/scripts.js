(function($) {
	
	"use strict";
	
/* ==========================================================================
   ieViewportFix - fixes viewport problem in IE 10 SnapMode and IE Mobile 10
   ========================================================================== */
   
	function ieViewportFix() {
	
		var msViewportStyle = document.createElement("style");
		
		msViewportStyle.appendChild(
			document.createTextNode(
				"@-ms-viewport { width: device-width; }"
			)
		);

		if (navigator.userAgent.match(/IEMobile\/10\.0/)) {
			
			msViewportStyle.appendChild(
				document.createTextNode(
					"@-ms-viewport { width: auto !important; }"
				)
			);
		}
		
		document.getElementsByTagName("head")[0].
			appendChild(msViewportStyle);

	}

/* ==========================================================================
   exists - Check if an element exists
   ========================================================================== */		
	
	function exists(e) {
		return $(e).length > 0;
	}

/* ==========================================================================
   isTouchDevice - return true if it is a touch device
   ========================================================================== */

	function isTouchDevice() {
		return !!('ontouchstart' in window) || ( !! ('onmsgesturechange' in window) && !! window.navigator.maxTouchPoints);
	}

/* ==========================================================================
   setDimensionsPieCharts
   ========================================================================== */
	
	function setDimensionsPieCharts() {

		$(".pie-chart").each(function() {

			var $t = $(this);
			var n = $t.parent().width();
			var r = $t.attr("data-barSize");
			
			if (n < r) {
				r = n;
			}
			
			$t.css("height", r);
			$t.css("width", r);
			$t.css("line-height", r + "px");
			
			$t.find("i").css({
				"line-height": r + "px",
				"font-size": r / 3
			});
			
		});

	}

/* ==========================================================================
   animatePieCharts
   ========================================================================== */

	function animatePieCharts() {

		if(typeof $.fn.easyPieChart != 'undefined'){

			$(".pie-chart:in-viewport").each(function() {
	
				var $t = $(this);
				var n = $t.parent().width();
				var r = $t.attr("data-barSize");
				
				if (n < r) {
					r = n;
				}
				
				$t.easyPieChart({
					animate: 1300,
					lineCap: "square",
					lineWidth: $t.attr("data-lineWidth"),
					size: r,
					barColor: $t.attr("data-barColor"),
					trackColor: $t.attr("data-trackColor"),
					scaleColor: "transparent",
					onStep: function(from, to, percent) {
						$(this.el).find('.pie-chart-percent span').text(Math.round(percent));
					}
	
				});
				
			});
			
		}

	}

/* ==========================================================================
   animateMilestones
   ========================================================================== */

	function animateMilestones() {

		$(".milestone:in-viewport").each(function() {
			
			var $t = $(this);
			var	n = $t.find(".milestone-value").attr("data-stop");
			var	r = parseInt($t.find(".milestone-value").attr("data-speed"));
				
			if (!$t.hasClass("already-animated")) {
				$t.addClass("already-animated");
				$({
					countNum: $t.find(".milestone-value").text()
				}).animate({
					countNum: n
				}, {
					duration: r,
					easing: "linear",
					step: function() {
						$t.find(".milestone-value").text(Math.floor(this.countNum));
					},
					complete: function() {
						$t.find(".milestone-value").text(this.countNum);
					}
				});
			}
			
		});

	}

/* ==========================================================================
   animateProgressBars
   ========================================================================== */

	function animateProgressBars() {

		$(".progress-bar .progress-bar-outer:in-viewport").each(function() {
			
			var $t = $(this);
			
			if (!$t.hasClass("already-animated")) {
				$t.addClass("already-animated");
				$t.animate({
					width: $t.attr("data-width") + "%"
				}, 2000);
			}
			
		});

	}

/* ==========================================================================
   enableParallax
   ========================================================================== */

	function enableParallax() {

		if(typeof $.fn.parallax != 'undefined'){
			
			$('.parallax').each(function() {
	
				var $t = $(this);
				$t.addClass("parallax-enabled");
				$t.parallax("49%", 0.3, false);
	
			});
			
		}

	}

/* ==========================================================================
   handleContactForm - validate and ajax submit contat form
   ========================================================================== */

	function handleContactForm() {
	
		if(typeof $.fn.validate != 'undefined'){
			
			$('#contact-form').validate({
				errorClass: 'validation-error', // so that it doesn't conflict with the error class of alert boxes
				rules: {
					name: {
						required: true
					},
					email: {
						required: true,
						email: true
					},
					subject: {
						required: true
					},
					message: {
						required: true
					}
				},
				messages: {
					name: {
						required: "Field is required!"
					},
					email: {
						required: "Field is required!",
						email: "Please enter a valid email address"
					},
					subject: {
						required: "Field is required!"
					},
					message: {
						required: "Field is required!"
					}
				},
				submitHandler: function(form) {
					var result;
					$(form).ajaxSubmit({
						type: "POST",
						data: $(form).serialize(),
						url: "_layout/php/send.php",
						success: function(msg) {
							
							if (msg == 'OK') {
								result = '<div class="alert success"><i class="fa fa-check-circle-o"></i>The message has been sent!</div>';
								$('#contact-form').clearForm();
							} else {
								result = '<div class="alert error"><i class="fa fa-times-circle"></i>' + msg + '</div>';
							}
							$("#formstatus").html(result);
		
						},
						error: function() {
		
							result = '<div class="alert error"><i class="fa fa-times-circle"></i>There was an error sending the message!</div>';
							$("#formstatus").html(result);
		
						}
					});
				}
			});
			
		}
		
	}


/* ==========================================================================
   handleMobileMenu 
   ========================================================================== */		

	var MOBILEBREAKPOINT = 979;

	function handleMobileMenu() {

		if ($(window).width() > MOBILEBREAKPOINT) {
			
			$("#mobile-menu").hide();
			$("#mobile-menu-trigger").removeClass("mobile-menu-opened").addClass("mobile-menu-closed");
		
		} else {
			
			if (!exists("#mobile-menu")) {
				
				$("#menu").clone().attr({
					id: "mobile-menu",
					"class": "fixed"
				}).insertAfter("#header");
				
				$("#mobile-menu > li > a, #mobile-menu > li > ul > li > a").each(function() {
					var $t = $(this);
					if ($t.next().hasClass('sub-menu') || $t.next().is('ul')) {
						$t.append('<span class="fa fa-angle-down mobile-menu-submenu-arrow mobile-menu-submenu-closed"></span>');
					}
				});
			
				$(".mobile-menu-submenu-arrow").click(function(event) {
					var $t = $(this);
					if ($t.hasClass("mobile-menu-submenu-closed")) {
						$t.parent().siblings("ul").slideDown(300);
						$t.removeClass("mobile-menu-submenu-closed fa-angle-down").addClass("mobile-menu-submenu-opened fa-angle-up");
					} else {
						$t.parent().siblings("ul").slideUp(300);
						$t.removeClass("mobile-menu-submenu-opened fa-angle-up").addClass("mobile-menu-submenu-closed fa-angle-down");
					}
					event.preventDefault();
				});
				
				$("#mobile-menu li, #mobile-menu li a, #mobile-menu ul").attr("style", "");
				
			}
			
		}

	}

/* ==========================================================================
   showHideMobileMenu
   ========================================================================== */

	function showHideMobileMenu() {
		
		$("#mobile-menu-trigger").click(function(event) {
			
			var $t = $(this);
			var $n = $("#mobile-menu");
			
			if ($t.hasClass("mobile-menu-opened")) {
				$t.removeClass("mobile-menu-opened").addClass("mobile-menu-closed");
				$n.slideUp(300);
			} else {
				$t.removeClass("mobile-menu-closed").addClass("mobile-menu-opened");
				$n.slideDown(300);
			}
			event.preventDefault();
			
		});
		
	}
	
/* ==========================================================================
   handleAccordionsAndToogles
   ========================================================================== */
   
   function handleAccordionsAndToogles() {
	   
		// accordeon
		
		$('.accordion a.accordion-item-toggle').click(function (e) { 
			var dropDown = $(this).closest('.accordion-item').find('.accordion-item-content');

			$(this).closest('.accordion').find('.accordion-item-content').not(dropDown).slideUp();

			if ($(this).hasClass('active')) { 
				$(this).removeClass('active');
			} else { 
				$(this).closest('.accordion').find('.accordion-item-toggle.active').removeClass('active');
				$(this).addClass('active');
			}

			dropDown.stop(false, true).slideToggle();

			e.preventDefault();
		});
		
		// toggle
		
		$('.toggle a.toggle-item-toggle').click(function (e) { 
			var dropDown = $(this).closest('.toggle-item').find('.toggle-item-content');

			if ($(this).hasClass('active')) { 
				$(this).removeClass('active');
			} else { 
				$(this).addClass('active');
			}

			dropDown.stop(false, true).slideToggle();

			e.preventDefault();
		});
   
   }   
   
/* ==========================================================================
   handleBackToTop
   ========================================================================== */
   
   function handleBackToTop() {
	   
		$('#back-to-top').click(function(){
			$('html, body').animate({scrollTop:0}, 'slow');
			return false;
		});
   
   }

// -------------------------------------------------------------------------------------------------------
//  handleFullScreenDiv
// -------------------------------------------------------------------------------------------------------
	
	function handleFullScreenDiv() {
	
		var x = $(window).height();
		
		$('.full-screen').css("min-height", x + "px");
		
	}

// -------------------------------------------------------------------------------------------------------
//  handleSmoothScrolling
// -------------------------------------------------------------------------------------------------------
	
	function handleSmoothScrolling() {
	
		$('a[href*=#]:not([href=#])').click(function() {
			if (location.pathname.replace(/^\//,'') == this.pathname.replace(/^\//,'') && location.hostname == this.hostname) {
			  var target = $(this.hash);
			  target = target.length ? target : $('[name=' + this.hash.slice(1) +']');
			  if (target.length) {
				$('html,body').animate({
				  scrollTop: target.offset().top
				}, 700);
				return false;
			  }
			}
		});
	}


/* ==========================================================================
   When document is ready, do
   ========================================================================== */
   
	$(document).ready(function() {			   
		
		ieViewportFix();
		
		setDimensionsPieCharts();
		
		animatePieCharts();
		animateMilestones();
		animateProgressBars();

		if (!isTouchDevice()) {
			enableParallax();
		}

		handleContactForm();
		
		handleMobileMenu();
		showHideMobileMenu();
		
		handleAccordionsAndToogles();
		
		handleBackToTop();
		
		handleFullScreenDiv();
		
		handleSmoothScrolling();
		
	});

/* ==========================================================================
   When the window is scrolled, do
   ========================================================================== */
   
	$(window).scroll(function() {				   
		
		animateMilestones();
		animatePieCharts();
		animateProgressBars();

	});

/* ==========================================================================
   When the window is resized, do
   ========================================================================== */
   
	$(window).resize(function() {
		
		handleMobileMenu();
		
		handleFullScreenDiv();
		
	});
	

})(window.jQuery);

// non jQuery scripts below