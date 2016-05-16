'use strict';

// date
$(function() {
  $( "#datepicker" ).datepicker();
});

// menu
$(function() {
  var country_lst = ['China', 'United States'];
  var city_lst = {
    'China': ['Shanghai', 'Beijing', 'JiLin', 'JiuTai'],
    'United States': ['New York', 'L.A.', 'Boston'],
  };
  $('#country').append( new Option('Country', 'Country') );
  $.each(country_lst, function (i, el) { $('#country').append( new Option(el, el) ); });
  
  $('#city').append( new Option('City', 'City') );
  $('#city').selectmenu({});
	$("#country").selectmenu({
    change: function (event, data) {
      // remove all options from city selectmenu
      $('#city').find('option').remove().end();
      $('#city').append( new Option('City', 'City') );
      $.each(city_lst[data.item.value], function (i, el) { $('#city').append( new Option(el, el) ); });
      // refresh city selectmenu
      $('#city').selectmenu('refresh');
    }
  });
  // console.log($('#country :selected').text(), $('#city :selected'));
});

$(function() {
  $.get('/online/get_user_info/', function(data) {
    // var user = JSON.parse(data);
    // console.log(user);
    // console.log(data);
    // console.log(JSON.parse(data['hobby']));
    $("#register_form").find("input[name='username']").val(data['username']);
    $("#register_form").find("input[name='email']").val(data['email']);
    $("#register_form").find("input[name='birthday']").val(data['birthday']);

    console.log(data['birthplace']);
    var make = "United States"
    $("#country option[value='" + make + "']".attr("selected"));

    $("#register_form").find("textarea").val(data['info']);
  });
});

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
  var messageArea = $("#register_form").find("textarea").val();
  var post_data = {
    username: username,
    password: password,
    email: email,
    birthday: birthday,
    birthplace: birthplace,
    gender: gender,
    hobby: hobby,
    messageArea: messageArea
  };

  console.log(post_data);
  $.post('/online/regist/', post_data, function (data) {
    console.log(data);
    window.location = '/online/';
  });

}
