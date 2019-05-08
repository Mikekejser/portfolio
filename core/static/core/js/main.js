$(document).ready(function(){
	$(".col-md-6, .col-lg-4").on({
		mouseenter: function(){
			// $("this").addClass("description-overlay");
			$("this").css("opacity", "0.5");
		},
		mouseleave: function(){
			// $("this").removeClass("opacity", "1");
			$("this").css("opacity", "1");
		}
	});
	$("#email-icon, #tlf-icon").on("click", function(){
		$(this).hide();
		$(this > 'p').show();
	})
})