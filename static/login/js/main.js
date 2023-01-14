
// (function ($) {
//     "use strict";


    
//     /*==================================================================
//     [ Validate ]*/
//     var input = $('.validate-input .input100');

//     // $('.validate-form').on('submit',function(){
//     //     var check = true;

//     //     for(var i=0; i<input.length; i++) {
//     //         if(validate(input[i]) == false){
//     //             showValidate(input[i]);
//     //             check=false;
//     //         }
//     //     }

//     //     return check;
//     // });


//     $('.validate-form .input100').each(function(){
//         $(this).focus(function(){
//            hideValidate(this);
//         });
//     });

//     function validate (input) {
//         if($(input).attr('type') == 'email' || $(input).attr('name') == 'email') {
//             if($(input).val().trim().match(/^([a-zA-Z0-9_\-\.]+)@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.)|(([a-zA-Z0-9\-]+\.)+))([a-zA-Z]{1,5}|[0-9]{1,3})(\]?)$/) == null) {
//                 return false;
//             }
//         }
//         else {
//             if($(input).val().trim() == ''){
//                 return false;
//             }
//         }
//     }

//     function showValidate(input) {
//         var thisAlert = $(input).parent();

//         $(thisAlert).addClass('alert-validate');
//     }

//     function hideValidate(input) {
//         var thisAlert = $(input).parent();

//         $(thisAlert).removeClass('alert-validate');
//     }
    
    

// })(jQuery);

    var email_input = $('#email')
    var password_input = $('#password')
    var login_button = $('#loginBtn')

    login_button.click(function () {
        var login_payload = {'email': email_input.val(),
                             'password': password_input.val()   
                            }

        $("#login_form").submit(function(e) {
        e.preventDefault();
        });                    

        $.post(
            'http://127.0.0.1:8000/api/v1/accounts/login/',
            login_payload
        )                    
    })
