$(document).ready(function(){
    


    //_url : 데이터 보낼 주소
    //todo_name : 수정할 데이터 이름
    //complete : todo item의 complete  설정 
    function completeBtn_ajaxEvent(_url, todo_name, complete){
        $.ajax(
            {
                type : "POST",
                url : _url,
                data : {'complete' : JSON.stringify([todo_name, !complete]) },
                traditional : true,
                success : function(response){
                    console.log("성공");
                },
                error : function(e){
                    alert("데이터 전송 실패!")
                }


            }
        );
    }

    function completeBtn_btnImgChange($btn_img, complete){
        if(complete){ // 
            //button img 변경
            $btn_img.addClass("fa-circle").removeClass("fa-check-circle");
        }
        else{
            //button img 변경
            $btn_img.addClass("fa-check-circle").removeClass("fa-circle");
        }
    }

    function completeBtn_rowItemClassChange($row_item, complete){
        if(complete){
            //row_item에 completed 클래스 제거
            $row_item.removeClass("completed");
            //row_item에 actived 클래스 cnrk
            $row_item.addClass("actived");
        }
        else{
            //row_item에 completed 클래스 추가
            $row_item.addClass("completed");
            //row_item에 actived 클래스 제거
            $row_item.removeClass("actived");
        }   

    }

    function completeBtn_leftTextChange($left_item, complete){
        if($left_item, complete){
            num = complete ? 1 : 0;
            //left_item text 변경
            $left_item.text(Number($left_item.text()) +num);
        }
    }

    function completeBtn_clickEvent($row_item, $button_img, todo_name, complete, url){
        //button img 변경
        completeBtn_btnImgChange($button_img, complete);

        //row Item class 설정
        completeBtn_rowItemClassChange($row_item,complete);

        //ajax Event 설정
        completeBtn_ajaxEvent(url,todo_name,complete);

        //Left Text 객체 text 변경
        completeBtn_leftTextChange($left_item,complete);
    }

    

    //object 변수 할당
    const $row_items = $('.list-group-item');
    const $left_item = $('.left_item');

    const $allBtn = $('.all_btn');
    const $activeBtn = $('.active_btn');
    const $completeBtn = $('.complete_btn');
    const $clearBtn = $('.clear_btn');

    //COMPLTED_BTN FUNCTION SETTING
    $completed_btn = $(".completed_btn");
    $completed_btn.click(function(){
        //url 주소 설정
        url = "http://port-8000.django-eogns0321.codeanyapp.com/todo/"

        //$(this) -> 클릭한 버튼 객체
        $row_item = $(this).closest("li"); //해당 아이템의 row object
        $button_img = $(this).children("i"); //해당 아이템의 button img object
        todo_name = $row_item.children("h4").text(); //해당 아이템의 text 

        
        //***row item의 complete 상태에 따라 버튼 이벤트 설정***//
        complete = $row_item.is(".completed") ? true : false;
        completeBtn_clickEvent($row_item,$button_img,todo_name,complete,url);

    });
    
    //Button settings
    $allBtn.click(function(){
        $completed_items = $('.completed');
        $active_items = $('.actived');

        $completed_items.fadeIn("slow");
        $active_items.fadeIn("slow");
        
        $completeBtn.removeClass("btn-primary");
        $activeBtn.removeClass("btn-primary");
        $(this).addClass("btn-primary");
    });
    $completeBtn.click(function(){
        $completed_items = $('.completed');
        $active_items = $('.actived');

        $active_items.fadeOut("slow", function(){
            $completed_items.fadeIn("slow");
        });
    
        $allBtn.removeClass("btn-primary");
        $activeBtn.removeClass("btn-primary");
        $(this).addClass("btn-primary");
    });
    $activeBtn.click(function(){
        $completed_items = $('.completed');
        $active_items = $('.actived');
        
        $completed_items.fadeOut("slow", function(){
            $active_items.fadeIn("slow");
        });

        $completeBtn.removeClass("btn-primary");
        $allBtn.removeClass("btn-primary");
        $(this).addClass("btn-primary");
        
    });
    $clearBtn.click(function(){
        $completed_items = $('.completed');
        $completed_items.fadeOut("slow", function(){
            $completed_items.remove();
        });
        
        
        completed_name = [];
        for(let i = 0; i < $completed_items.length; i++){
            completed_name.push($.trim($($completed_items[i]).text()));
        }
        //ajax로 complete 된 item 삭제 요청
        $.ajax(
            {
                type : "POST",
                url : "{% url 'todoapp:home' %}",
                data : {'delete' : JSON.stringify(completed_name) },
                success : function(response){
                    console.log("성공");
                },
                error : function(e){
                    alert("데이터 전송 실패!")
                }


            }
        );

    });

});