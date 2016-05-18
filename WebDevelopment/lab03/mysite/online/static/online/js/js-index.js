'use strict';

var country_lst = ['China', 'United States'];
var city_lst = {
    'China': ['Shanghai', 'Beijing', 'JiLin', 'JiuTai'],
    'United States': ['New York', 'L.A.', 'Boston'],
};

function on_country_changed(value) {
    // remove all options from city selectmenu
    $('#city').find('option').remove().end();
    $('#city').append( new Option('City', 'City') );
    $.each(city_lst[value], function (i, el) {
        $('#city').append( new Option(el, el) );
    });
    // refresh city selectmenu
    $('#city').selectmenu('refresh');
}

// date
$(function() {
  $( "#datepicker" ).datepicker();
  CKEDITOR.replace( 'editor' );
});

// menu
$(function() {
  $('#country').append( new Option('Country', 'Country') );
  $.each(country_lst, function (i, el) { $('#country').append( new Option(el, el) ); });

  $('#city').append( new Option('City', 'City') );
  $('#city').selectmenu({});
	$("#country").selectmenu({
    change: function (event, data) {
      on_coutry_changed(data.item.value);
    }
  });
});

$(function() {
  $.get('/online/get_user_info/', function(data) {
    $("#register_form").find("input[name='username']").val(data['username']);
    $("#register_form").find("input[name='email']").val(data['email']);
    $("#register_form").find("input[name='birthday']").val(data['birthday']);

    var birthplace = data['birthplace'].split(';');
    var birthplace_country = birthplace[0];
    var birthplace_city = birthplace[1];
    $("#country option[value='" + birthplace_country + "']").attr('selected', 'selected');
    $('#country').selectmenu('refresh');
    on_country_changed(birthplace_country);
    $("#city option[value='" + birthplace_city + "']").attr('selected', 'selected');
    $('#city').selectmenu('refresh');

    CKEDITOR.instances.editor.setData(data['info']);
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
  var messageArea = CKEDITOR.instances.editor.getData();
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
    captcha: captcha
  };

  console.log(post_data);
  $.post('/online/update_info/', post_data, function (data) {
    console.log(data);
    window.location = '/online/';
  });

}
