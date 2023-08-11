$(document).ready(function () {

    if(('#result') != null ){
        Read();
    }
    $('#create').on('click', function () {
        $firstname = $('#firstname').val();
        $lastname = $('#lastname').val();
        if ($firstname == "" || $lastname == "") {
            alert("please input")
        }
        else {
            $.ajax({
                url:'create/',
                type:'POST',
                data: {
                    firstname: $firstname,
                    lastname: $lastname,
                    csrfmiddlewaretoken: $('input[name=csrfmiddlewaretoken]').val()
                },
                success: function(){
                    Read();
                    $('#firstname').val('');
                    $('#lastname').val('');
                    alert("added")
                }
            })
        }
    });

    $(document).on('click','.edit',function(){
        $id=$(this).attr('name');
        window.location="edit/"+$id;
    });

    $(document).on('click','.delete',function(){
        $id=$(this).attr('name');
        $.ajax({
            url:'delete/'+ $id,
            type:'POST',
            data: {
                csrfmiddlewaretoken: $('input[name=csrfmiddlewaretoken]').val()
            },
            success: function(){
                Read();
                alert("deleted");
            }
        })
        
    });

    

});

$('#update').on('click',function(){
    $firstname = $('#firstname').val();
    $lastname = $('#lastname').val();
    if ($firstname == "" || $lastname == "") {
        alert("please input")
    }
    else{
        $id=$('#member_id').val();
        $.ajax({
            url:'update/'+ $id,
            type:'POST',
            data: {
                firstname: $firstname,
                lastname: $lastname,
                csrfmiddlewaretoken: $('input[name=csrfmiddlewaretoken]').val()
            },
            success: function(){
                window.location='/';
                alert("updated");
            }
        })
    }
});

function Read(){
    $.ajax({
        url:'read/',
        type:'POST',
        async:false,
        data:{
            res:1,
            csrfmiddlewaretoken:$('input[name=csrfmiddlewaretoken]').val()
        },
        success: function(response){
            $('#result').html(response);
        }
    })
}