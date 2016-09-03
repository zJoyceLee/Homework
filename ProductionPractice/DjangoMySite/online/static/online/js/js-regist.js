'use strict';

function submit_onclick(event) {
  console.log('submit_onclick');
  if (validate_form($("#register_form")[0]) === false) {
    event.preventDefault();
    return false;
  }

  var username = $("#register_form").find("input[name='username']").val();
  var password = $("#register_form").find("input[name='password']").val();
  var phone = $("#register_form").find("input[name='phone']").val();
  var email = $("#register_form").find("input[name='email']").val();
  var addr = $("#register_form").find("input[name='addr']").val();
  var captcha = $("#register_form").find("input[name='captcha']").val();
  var post_data = {
    username: username,
    password: password,
    phone: phone,
    email: email,
    addr: addr,
    captcha: captcha
  };

  $.post('/online/regist/', post_data, function (data) {
    if (data['code'] !== 0) {
      alert(data['msg']);
      return;
    }
    window.location = 'http://localhost:8080/shopping/html/index.jsp';
  });
}
