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


// ajax
$(document).ready(function(){
    checkUserName();
});
//验证用户名是否存在
function checkUserName(){
    $("#username").blur(function(){
        var username = $(this).val();
        //此处替换你自己的jsp路径，jsp返回值：存在输出1，不存在输出0
        var changeUrl = "check.php?username=" + username;
        $.get(changeUrl,function(str){
            if(str == '1'){
                $("#tips").html("<font color=\"red\">您输入的用户名存在！请重新输入！</font>");
            }else{
                $("#tips").html("<font color=\"green\">恭喜您，可以注册！</font>");
            }
        });
        return false;
    })
}


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
