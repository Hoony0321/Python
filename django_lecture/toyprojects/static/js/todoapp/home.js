//==========FUNCTION DEFINED==========//


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
        num = complete ? 1 : -1;
        //left_item text 변경
        $left_item.text(Number($left_item.text()) +num);
}

function completeBtn_clickEvent($row_item, $button_img, $left_item, todo_name, complete, url){
    //button img 변경
    completeBtn_btnImgChange($button_img, complete);

    //row Item class 설정
    completeBtn_rowItemClassChange($row_item,complete);

    //ajax Event 설정
    completeBtn_ajaxEvent(url,todo_name,complete);

    //Left Text 객체 text 변경
    completeBtn_leftTextChange($left_item,complete);
}

function bottomBtn_setObjects(){
    $completed_items = $('.completed');
    $active_items = $('.actived');
}

function fadeInOut_items($thisBtn, $completed_items, $active_items){
    let selector = $thisBtn.selector;
    if(selector == ".all_btn"){ //All BTN CLICKED
        $completed_items.fadeIn("slow");
        $active_items.fadeIn("slow");
    }
    else if(selector == ".complete_btn"){ //COMPLETE BTN CLICKED
        $active_items.fadeOut("slow", function(){
            $completed_items.fadeIn("slow");
        });
        
    }
    else{ //ACTIVE BTN CLICKED
        $completed_items.fadeOut("slow", function(){
            $active_items.fadeIn("slow");
        });
        
    }
}

function setClass_btns($thisBtn, $otherBtn1, $otherBtn2){

    $otherBtn1.removeClass("btn-primary");
    $otherBtn2.removeClass("btn-primary");
    $thisBtn.addClass("btn-primary");

}

function bottomBtn_clickEvent($thisBtn, $otherBtn1, $otherBtn2){
    $completed_items = null
    $active_items = null

    //Set Object
    bottomBtn_setObjects();

    fadeInOut_items($thisBtn, $completed_items, $active_items);

    setClass_btns($thisBtn,$otherBtn1,$otherBtn2);

}


//url 변수는 이미 설정되어 있음.
$(document).ready(function(){

    //object 변수 할당
    const $row_items = $('.list-group-item');
    const $left_item = $('.left_item');

    const $allBtn = $('.all_btn');
    const $activeBtn = $('.active_btn');
    const $completeBtn = $('.complete_btn');
    const $clearBtn = $('.clear_btn');

    //complete_btn variable set
    $completed_btn = $(".completed_btn");

    //complete_btn click event setting
    $completed_btn.click(function(){

        //$(this) -> 클릭한 버튼 객체
        $row_item = $(this).closest("li"); //해당 아이템의 row object
        $button_img = $(this).children("i"); //해당 아이템의 button img object
        todo_name = $row_item.children("h4").text(); //해당 아이템의 text 

        
        //***row item의 complete 상태에 따라 버튼 이벤트 설정***//
        complete = $row_item.is(".completed") ? true : false;
        console.log(complete);
        completeBtn_clickEvent($row_item,$button_img,$left_item,todo_name,complete,url);

    });
    

    //=====bottomBtn click Event setting=====//
    let $bottomBtns = [$allBtn, $activeBtn, $completeBtn];

    for(let i =0; i < $bottomBtns.length; i++){
        $bottomBtns[i].click(function(){
            bottomBtn_clickEvent($bottomBtns[i],$bottomBtns[(i+1)%3],$bottomBtns[(i+2)%3]);
        });
    }

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
                url : url,
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