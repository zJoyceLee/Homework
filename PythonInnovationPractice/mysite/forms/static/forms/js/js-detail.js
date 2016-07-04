'use strict';

function submit_onclick(event) {
  console.log('submit_onclick');
  if (validate_form($("#register_form")[0]) === false) {
    event.preventDefault();
    return false;
  }

  var username = $("#register_form").find("input[name='username']").val();
  var password = $("#register_form").find("input[name='password']").val();
  var email = $("#register_form").find("input[name='email']").val();
  var birthday = $("#register_form").find("input[name='birthday']").datepicker().val();

  var birthplace_country = $('#country :selected').text();
  var birthplace_city = $('#city :selected').text();
  var birthplace = birthplace_country + ';' + birthplace_city;

  var gender = $("#register_form").find("input[name='gender']:checked").val();
  var hobby = [];
  $("#register_form").find("input[name='hobby']:checked").each(function () { hobby.push($(this).val()); });
  var messageArea = CKEDITOR.instances.editor.getData();
  var photo_path = '@TODO';
  var captcha = $("#register_form").find("input[name='captcha']").val();
  var post_data = {
    username: username,
    password: password,
    email: email,
    birthday: birthday,
    birthplace: birthplace,
    gender: gender,
    hobby: hobby,
    messageArea: messageArea,
    photo_path: photo_path,
    captcha: captcha
  };

  $.post('/online/regist/', post_data, function (data) {
    if (data['code'] !== 0) {
      alert(data['msg']);
      return;
    }
    window.location = '/online/';
  });
}
