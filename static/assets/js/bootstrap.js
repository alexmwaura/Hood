$(document).ready(function(){
    $('.show-form').click(function(){
        $.ajax({
            url: 'create/',
            type: 'get',
            dataType:'json',
            beforeSend: function(){
                $('#modal-book').modal('show');


            },
            success:function(data){
                $('#modal-book , modal-content').htm(data.html_form)
            }
        });
    });
}); 