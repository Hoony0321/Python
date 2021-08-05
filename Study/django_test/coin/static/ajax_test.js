$(document).ready(function(){

    let sendBtn = $(".btnAjax");

    sendBtn.click(function(){
        let title = $(".title").val();
        let content = $(".content").val();
        let dict123 = {
            'title' : title,
            'content' : content,
        };
        $.ajax({
            url : "reponse/",
            type : 'POST',
            data : JSON.stringify(dict123),
            success:function(data){console.log(data);},
            error:function(){console.log("실패!!")}
        });
    });
});