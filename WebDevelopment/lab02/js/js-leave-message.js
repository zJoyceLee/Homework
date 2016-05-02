function isEmpty(val) {
	return ((val == '') || (val == null));
}

function formcheck(form) {
	if(isEmpty(form.name.value) || isEmpty(form.email.value)) {
		window.alert("Please fullfill the form!");
		return false;
	}
	return true;
}

function showAllMessages() {
	var xmlhttp = new XMLHttpRequest();

	xmlhttp.onreadystatechange = function() {
		if(xmlhttp.readyState == 4 && xmlhttp.status == 200) {
			document.getElementByIdH("div-allMessages").innerHTML = xmlhttp;
		}
	}

	xmlhttp.open("GET", "../cgi-bin/leave-a-message-form.cgi", true);
	xmlhttp.send();
}

$(document).ready(function() {

});