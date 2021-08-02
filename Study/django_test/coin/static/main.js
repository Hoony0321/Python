$(document).ready(function(){

    $("#stopReload_btn").click(function(){
        clearInterval(reload_currencyTable);
    });

    reload_currencyTable = setInterval(function(){
        location.reload();
    },2000);
});