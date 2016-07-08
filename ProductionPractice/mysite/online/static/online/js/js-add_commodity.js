'use strict';
$(function() {
    $( "#datepicker" ).datepicker();
    CKEDITOR.replace( 'editor' );
});

function submit_onclick_commodity(event) {
  console.log('submit_onclick_commodity');

  var id = $("#add_commodity_form").find("input[name='commodity_id']").val();
  var name = $("#add_commodity_form").find("input[name='commodity_name']").val();
  var price = $("#add_commodity_form").find("input[name='commodity_price']").val();
  var store = $("#add_commodity_form").find("input[name='commodity_store']").val();
  var messageArea = CKEDITOR.instances.editor.getData();

  var post_data = {
    id: id,
    name: name,
    price: price,
    store: store,
    messageArea: messageArea
  };

  $.post('/online/add_commodity/', post_data, function (data) {
    if (data['code'] !== 0) {
      alert(data['msg']);
      return;
    }
    window.location = '/online/commodity/';
  });
}
