$(document).ready(function(){
	var button_text_default = "Map View"
	$('#map').hide();
	var button_text_ = "List View"
	$('a').tooltip();//activate tool tooltip
	$('#toggleView').text(button_text_default);
    $('#toggleView').click(function(){
        var button_text = $('#toggleView').text();
        if(button_text==button_text_default){
        	$('#toggleView').text(button_text_);
        	$('#list-view').hide('slow');
        	$('#map').show('slow');
        }
        else{
        	$('#toggleView').text(button_text_default);
        	$('#list-view').show('slow');
        	$('#map').hide('slow');
        }
    });

});
