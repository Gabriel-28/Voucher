$(document).ready(function() {
    $('#registrationForm').submit(function(e) {
        e.preventDefault();
        var first_name = $("#first_name").val();
        var last_name = $("#last_name").val();
        var email = $("#email").val();
        var phone_number = $("#phone_number").val();
        var password = $("#password").val();

        var data = {
            'first_name': first_name,
            'last_name': last_name,
            'email': email,
            'password': password,
            'phone_number': phone_number,
            "csrfmiddlewaretoken": CSRF_TOKEN,
        };

        $.ajax({
            type: 'POST',
            url: REGISTER_URL,
            data: data,
            success: function (response) {
                if (response.status == "success") {
                    Swal.fire({
                        icon: 'success',
                        title: 'Successfully registered',
                        timer: 1500
                    }).then(function() {
                        // Redirect to the desired page
                        window.location.href = LOGIN_URL; // Change '/dashboard' to the desired URL
                    });
                }
            },
            error: function (error) {
                Swal.fire({
                    icon: 'error',
                    title: 'Unsuccessful',
                    timer: 1500
                });
            }
        });
    });
    $('#generationForm').submit(function(e){
        e.preventDefault();
        var code = generateRandomString(8);
        var max_redemptions = $("#max_redemptions").val();
        var expiry_date = $("#expiry_date").val();
        var redemption_type = $("#redemption_type").val();
        var x_times = $('#x_times').val();
        if (redemption_type == "single"){
            max_redemptions=1
        }else if (redemption_type=="multiple"){
            max_redemptions=3
        }
        else if (redemption_type=="xtimes"){
            max_redemptions=10
        }
        else if (redemption_type=="beforeTime"){
            max_redemptions=-1
        }
        var data = {
            'code': code,
            'max_redemptions': max_redemptions,
            'expiry_date': expiry_date,
            'redemption_type': redemption_type,
            "csrfmiddlewaretoken": CSRF_TOKEN,
        };
        console.log("datas ",data)

        $.ajax({
            type: 'POST',
            url: CREATE_VOUCHER,
            data: data,
            success: function (response) {
                if (response.status == "success") {
                    Swal.fire({
                        icon: 'success',
                        title: 'Successfully created',
                        timer: 1500
                    }).then(function() {
                        // Redirect to the desired page
                    });
                }
            },
            error: function (error) {
                Swal.fire({
                    icon: 'error',
                    title: 'Unsuccessful',
                    timer: 1500
                });
            }
        });
    })
});
function generateRandomString(length) {
    var characters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789';
    var result = '';
    for (var i = 0; i < length; i++) {
        result += characters.charAt(Math.floor(Math.random() * characters.length));
    }
    return result;
}

function displayVouchers() {
    var tableBody = $("#voucherTableBody");
    var voucherDetails = $("#voucherDetails");

    // Clear existing table rows
    tableBody.empty();

    // Make an AJAX request to the server
    $.ajax({
        url: "/redeem_voucher/",
        type: "GET",
        success: function (data) {
            var vouchers = data.vouchers;

            // Check if vouchers exist
            if (vouchers && vouchers.length > 0) {
                // Add rows for each voucher
                vouchers.forEach(function (voucher) {
                    var row = $("<tr>");
                    row.append($("<td>").text(voucher.code));
                    row.append($("<td>").text(voucher.expirationDate));
                    tableBody.append(row);
                });

                // Show the voucher details
                voucherDetails.show();
            } else {
                console.log("No vouchers found.");
            }
        },
        error: function () {

            console.error("Error fetching voucher data.");
        }
    });
}

