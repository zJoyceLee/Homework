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
