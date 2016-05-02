function reduce(list, lambda) {
    if (list.length == 0) {
        return null;
    }
    var ret = list[0];
    for (var i = 1; i < list.length; ++i) {
        ret = lambda(ret, list[i]);
    }
    return ret;
}

function showAllMessages() {
    $.get("/cgi-bin/show-all-messages.py", function (data) {
        console.log(data);
	data = JSON.parse(data);
        var message = '';
        for (var i = 0; i < data.length; ++i) {
            var data_row = data[i];
	    message += '<p class="message-head">message ' + i + ':</p>';
	    $.map(['name', 'email', 'gender', 'hobby', 'messageArea'], function(field) {
                message += '<p class="message-body">' + field + ':' + data_row[field] + '</p>';
            });
        }
        $("#all-messages > div").html(message);
    });
}

function formcheck() {
    var check_result = '';

    var name = $('form#form-LeaveMessageForm input[name="name"]').val();
    var email = $('form#form-LeaveMessageForm input[name="email"]').val();
    var gender = $('form#form-LeaveMessageForm input[name="gender"]:checked').val();
    var hobby = $('form#form-LeaveMessageForm input[name="hobby"]:checked').map(function() { return $(this).val(); });
    var messageArea = $('form#form-LeaveMessageForm textarea[name="messageArea"]').val();
    var ret = reduce(
        [[name, 'name'], [email, 'email'], [gender, 'gender'], [hobby, 'hobby'], [messageArea, 'messageArea']].map(
            function(item) {
                if (item[0].length == 0) {
                    check_result += '<p>' + item[1] + ' is empty!</p>';
	            return false;
                }
                return true;
            }),
        function(bool1, bool2) {
            return bool1 && bool2;
        });
    
    if (ret != true) {
        $('#check-result > div').html(check_result);
    } else {
        $('#check-result > div').html('<p>All passed!</p>');
    }
    return ret;
}

function formsubmit() {
    if (formcheck() != true) {
        return;
    }

    console.log("formsubmit!")
    $.post("/cgi-bin/leave-a-message-form.py", $('form#form-LeaveMessageForm').serialize(), function (data) {
        console.log(data);
	data = JSON.parse(data);
        var message = '';
        for (var i = 0; i < data.length; ++i) {
            var data_row = data[i];
	    message += '<p class="message-head">message ' + i + ':</p>';
	    $.map(['name', 'email', 'gender', 'hobby', 'messageArea'], function(field) {
                message += '<p class="message-body">' + field + ':' + data_row[field] + '</p>';
            });
        }
        $("#all-messages > div").html(message);
    });
}

