//custom.js

$(".open").click(function(){
	$("div.overlay").fadeOut();
	var item = $(this).attr('href');
    $(item).fadeIn();
    return false;
    
	
});
$('.close').on("click", function () {
    $(this).parents('div').fadeOut();
});

$(document).keyup(function(e) {

  if (e.keyCode == 27) { 
							$("div.overlay").fadeOut();
						}   
});
