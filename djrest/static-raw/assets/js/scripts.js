$(document).ready(function() { 
    $.ajax({
        url: '/api/lists.json',
        type: 'GET',
    }).done(function(data){
        var listgroups = $('#listgroups');
        listgroups.empty();
        console.log(data);
    })
});