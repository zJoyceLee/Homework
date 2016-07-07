function validate_required(field,alerttxt) {
  with (field) {
    if (value==null||value=="") {
      alert(alerttxt);return false
    } else {
      return true
    }
  }
}

function validate_email(field,alerttxt) {
  with (field) {
    apos=value.indexOf("@")
    dotpos=value.lastIndexOf(".")
    if (apos<1||dotpos-apos<2){
      alert(alerttxt);
      return false;
    } else {
      return true;
    }
  }
}

function validate_form(thisform) {
  with (thisform) {
    if (validate_required(username, "UserName must be filled out!")==false) {
      username.focus();
      return false;
    }
    if (validate_required(password, "Password must be filled out!")==false) {
      password.focus();
      return false;
    }
    if (validate_required(confirm_password, "Password must be filled out!")==false) {
      confirm_password.focus();
      return false;
    }
    var password_val = $('#register_form').find("input[name='password']").val();
    var confirm_password_val = $('#register_form').find("input[name='confirm_password']").val();
    if (password_val !== confirm_password_val) {
      alert('password and confirm_password should be same');
      return false;
    }
    if (validate_required(email,"Email must be filled out!")==false) {
      email.focus();
      return false;
    }
    if (validate_email(email, "Format wrong.")==false) {
      email.focus();
      return false;
    }    
  }
}
