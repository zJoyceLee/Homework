$(function(){
	  $('#score_table').footable({
        "filtering": {
			      "enabled": true,
            "filters": [{
				        "name": "filter course",
				        "query": $('#pCourse').html(),
				        "columns": [3]
			      }]
		    },
        "paging": {
			      "enabled": true
		    }
    });
});
