var indexPage = (function() {
    var show = true,
    end;
    
    function onFun(){
        $('.register').on('click', function(){
            $(this).addClass('active');
            $('.login').removeClass('active');
            $('.form-register').css('display','block');
            $('.form-login').css('display','none');
        });
        $('.login').on('click', function(){
            $(this).addClass('active');
            $('.register').removeClass('active')
            $('.form-login').css('display','block');
            $('.form-register').css('display','none');
        });
        $('.login-btn').on('click', function(){
            //location.href="/simpleBlog/2015/03/08/courses.html";
        })
    };
    
    function showCursor() {
        if(show){
            $(".console-panel span").css("color","#fff");
            show = false;
        }else{
            $(".console-panel span").css("color","#000");
            show = true;
        }
        setTimeout(showCursor, 500);
    };
    
    onFun();
    showCursor();
    
    return {};
})();