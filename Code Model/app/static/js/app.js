$(function(){
	$('#btnSignUp').click(function(){
		var name = $('#inputName').val();
		var email = $('#inputEmail').val();
        var pass = $('#inputPassword').val();
		$.ajax({
			url: '/api/v1/users/',
			data: $('form').serialize(),
			type: 'POST',
			success: function(response){
				console.log(response);
			},
			error: function(error){
				console.log(error);
			}
		});
	});
});	
