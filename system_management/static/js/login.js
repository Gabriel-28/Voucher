$(document).ready(function () {
    $('#login_form').on('submit', function (event) {
        event.preventDefault();
        $("#loader").show();

        var username = $('#username').val();
        var password = $('#password').val();
        var data = {
            "username": username,
            "password": password,
            "csrfmiddlewaretoken": CSRF_TOKEN
        };
        $.ajax({
            type: 'POST',
            url: LOGIN_URL,
            data: data,
            success: function (response) {

                if (response.status == "success") {
                    $("#loader").hide();

                    // Check if the user is a superuser
                    if (response.is_superuser) {
                        window.location.href = CREATE_VOUCHER;
                    } else {
                        window.location.href = REDEEM_VOUCHER;
                    }

                } else {
                    $("#loader").hide();
                    Swal.fire({
                        icon: 'error',
                        title: 'Invalid Credentials',
                        text: response.message,
                    });
                }
            },
            error: function (response) {
                $("#loader").hide();

                Swal.fire({
                    icon: 'error',
                    title: 'Invalid Credentials',
                    text: response.message,
                });

            }
        });
    });
    $(".toggle-password").click(function() {
        const INPUT_ID = $(this).data("target-input");
        togglePasswordVisibility(INPUT_ID, $(this));
    }); 
});

function togglePasswordVisibility(INPUT_ID, toggleIcon) {
    var password_input = $("#" + INPUT_ID);
    if (password_input.attr("type") === "password") {
        password_input.attr("type", "text");
        toggleIcon.removeClass("fa-eye");
        toggleIcon.addClass("fa-eye-slash");
    } 
    else if (password_input.attr("type") === "text"){
        password_input.attr("type", "password");
        toggleIcon.removeClass("fa-eye-slash");
        toggleIcon.addClass("fa-eye");
    }
}
