$(document).ready(function() {
    //load existing list 
    $.ajax({
        url: '/api/lists.json',
        type: 'GET',
    }).done(function(data){
        var listgroups = $('#listgroups');
        listgroups.empty();
        //console.log(data);
        $.each(data, function(k, v){
            $('<li data-item-id="'+v.id+'">' +v.title+ '</li>').appendTo(listgroups);
        });
    });

    //create button listener / add new items to the list
    $('#btnlistinput').on('click', function(){
        var listiteminput = $('#listinput').val();
        console.log(listiteminput);
        if (listiteminput) {
            $.ajax({
                url: '/api/lists.json',
                type: 'POST',
                data: {title: listiteminput},
                //CSRF
                beforeSend: function (xhr, settings) {
                    if (!csrfSafeMethod(settings.type) && sameOrigin(settings.url)) {
                        xhr.setRequestHeader('X-CSRFToken', $.cookie('csrftoken'));
                    }
                },
            }).done(function(){
                $.ajax({
                    url: '/api/lists.json',
                    type: 'GET',
                }).done(function(data){
                    var listgroups = $('#listgroups');
                    listgroups.empty();
                    //console.log(data);
                    $.each(data, function(k, v){
                        $('<li>'+v.title+'</li>').appendTo(listgroups);
                    });
                });
            });
        }
    });

    //Delete on item click event
    $('#listgroups').on('click', 'li', function() {
        //console.log($(this).attr('data-item-id'));
        var listgroupId = $(this).attr('data-item-id');
        $.ajax({
            url: '/api/lists/' +listgroupId + '.json',
            type: 'DELETE',
            beforeSend: function (xhr, settings) {
                if (!csrfSafeMethod(settings.type) && sameOrigin(settings.url)) {
                    xhr.setRequestHeader('X-CSRFToken', $.cookie('csrftoken'));
                }
            },
        }).done(function(){
            $.ajax({
                url: '/api/lists.json',
                type: 'GET',
            }).done(function(data){
                var listgroups = $('#listgroups');
                listgroups.empty();
                //console.log(data);
                $.each(data, function(k, v){
                    $('<li>'+v.title+'</li>').appendTo(listgroups);
                });
            });
        });
    })
});