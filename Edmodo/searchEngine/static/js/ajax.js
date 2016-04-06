function searchSucccess(data){
	//alert("success")
	$('#tableData').html(data);
}

function errorF(Exception){
	alert('Exception : '+Exception)
}

$(function(){
	$('#button_1').on('click',function() {
		$(".loading-gif").removeClass("hide");
		$.ajax({
			type : "POST",
			url : "search_titles/",
			data : {
				'query' : $('#search').val(),
				'csrfmiddlewaretoken' : $("input[name=csrfmiddlewaretoken]").val()
			},
			success : searchSucccess,
			error :  errorF,
			dataType : 'html'
		}).complete( function(){
			$(".loading-gif").addClass("hide");
		});

	});

	$('#search').keyup(function(ev){
		ev.preventDefault();
		if(ev.keyCode == 13)
    	{
		$('#button_1').click();
		}
	});

	$('body').on('click', "#save", function() {

		var saveButton = $(this);
		var formValues = $("#flagged-values").serialize();
		$(".loading-gif").removeClass("hide");
		saveButton.attr("disabled", "disabled");
		$.ajax({
			type : "POST",
			url : "flag_values/",
			data : formValues + '&csrfmiddlewaretoken=' + $("input[name=csrfmiddlewaretoken]").val(),
			success : function( data){
				if( data == 1){
					$(".alert-success").removeClass("hide");

				}

				//update table entries as well.
				if( $('#inappropriate').is(":checked"))
					$("#" + $("#flagged-values").find("#product-id").val() ).parent().parent().find(".entry-inappropriate").html(1);
				else
					$("#" + $("#flagged-values").find("#product-id").val() ).parent().parent().find(".entry-inappropriate").html(0);

				if( $('#not_helpful').is(":checked"))
					$("#" + $("#flagged-values").find("#product-id").val() ).parent().parent().find(".entry-not_helpful").html(1);
				else
					$("#" + $("#flagged-values").find("#product-id").val() ).parent().parent().find(".entry-not_helpful").html(0);

				if( $('#wrong_tags').is(":checked"))
					$("#" + $("#flagged-values").find("#product-id").val() ).parent().parent().find(".entry-wrong_tags").html(1);
				else
					$("#" + $("#flagged-values").find("#product-id").val() ).parent().parent().find(".entry-wrong_tags").html(0);

				if( $('#spam').is(":checked"))
					$("#" + $("#flagged-values").find("#product-id").val() ).parent().parent().find(".entry-spam").html(1);
				else
					$("#" + $("#flagged-values").find("#product-id").val() ).parent().parent().find(".entry-spam").html(0);

				
			},
			error :  errorF
		}).complete( function(){
			$(".loading-gif").addClass("hide");
			setTimeout( function(){
					$(".alert-success").addClass("hide");
			}, 4000);
			saveButton.removeAttr("disabled");

		});
	});
});

