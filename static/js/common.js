$(document).ready(function(){
    //隐藏提示信息
    setTimeout(function(){
        return $('.am-alert').alert('close');
    },500);
    
    //手动修改确认密码placeholder
    $('#id_password2').attr('placeholder','确认密码');
});