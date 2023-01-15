$(document).ready(function() {
    console.log('ready')
})



$('#register_button').click(
    function () {
        var email = $('#email').val()
        var password1 = $('#password1').val()
        var password2 = $('#password2').val()

        payload = {
            'email': email,
            'password1': password1,
            'password2': password2
        }

        $.ajax(
            {
                type: 'POST',
                url: 'http://127.0.0.1:8000/api/v1/accounts/register/',
                async: false,
                data: payload,
                success: function(response) {
                    console.log(response)
                }
            }
        )
    }
)