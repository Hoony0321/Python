//ajax token 설정
$.ajaxSetup({
    headers : {'X-CSRFToken' : '{{ csrf_token }}'}
});