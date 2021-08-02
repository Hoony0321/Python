$("document").ready(function(){

    $("#clickBtn").click(function(){
        $.ajax("response.html")
        .done(function(json){
            alert("성공!!");
        })
        .fail(function(xhr, status, errorThrown){
            alert("오류 발생 " + status + errorThrown);
        })
        .always(function(xhr, status){
            console.log("요청이 완료되었습니다");
        });
    });


});