$(window).load(function(){
    var jcrop_api = null;
    var $per_box = $('#preview_box');
    var $tar_img = $('#target'),
        img_w = null,
        img_h = null,
    end;
    
    $('#id_avatar_link').change(handleFileSelect);
    //initImg();

    //初始化大预览图的大小
    function initImg(){
        img_w = $tar_img.width();
        img_h = $tar_img.height();
        //控制预览图的大小
        if(img_w > 400 || img_h > 400){
            if(img_w > img_h){
                img_w = '400px';
                img_h = 'auto';
            }else{
                img_w = 'auto';
                img_h = '400px';
            }
        }
        $tar_img.css({
            'width':img_w,
            'height':img_h
        });
        initJcrop();
        
        $('.width input').val($tar_img.width());
        $('.height input').val($tar_img.height());
    };
    
    //初始化jcrop插件
    function initJcrop(){  
        $("#target").Jcrop({ 
            onChange:showPreview,
            onSelect:showPreview,
            aspectRatio:1
        },function(){
            var bounds = this.getBounds();
            jcrop_api = this;
            $per_box.appendTo(jcrop_api.ui.holder);
        });
        
        //重置preview里的图片
        $("#crop_preview").attr('src', $('#target').attr('src'));
    };
    
    //简单的事件处理程序，响应自onChange,onSelect事件，按照上面的Jcrop调用
    function showPreview(coords){
        if(parseInt(coords.w) > 0){
            //计算预览区域图片缩放的比例，通过计算显示区域的宽度(与高度)与剪裁的宽度(与高度)之比得到
            var rx = $("#preview_box").width() / coords.w;
            var ry = $("#preview_box").height() / coords.h;
            //通过比例值控制图片的样式与显示
            
            $("#crop_preview").css({
                //预览图片宽度为计算比例值与原图片宽度的乘积
                width:Math.round(rx * $("#target").width()) + "px",
                //预览图片高度为计算比例值与原图片高度的乘积
                height:Math.round(rx * $("#target").height()) + "px",
                marginLeft:"-" + Math.round(rx * coords.x) + "px",
                marginTop:"-" + Math.round(ry * coords.y) + "px"
            });
            //打印选取框坐标点
            $('.x1 input').val(coords.x);
            $('.y1 input').val(coords.y);
            $('.x2 input').val(coords.x2);
            $('.y2 input').val(coords.y2);
           
        }
        
    };
    
    //input=file按钮响应执行方法
    function handleFileSelect(evt) {
        if (jcrop_api !== null){
            jcrop_api.destroy();
        }

        //重置target里图片的width/height
        $tar_img.css({
            'width':'auto',
            'height':'auto'
        });
        
        var files = evt.target.files;
        for (var i = 0, f; f = files[i]; i++) {

            if (!f.type.match('image.*')) {
                continue;
            }

            var reader = new FileReader();
            reader.onload = (function(theFile) {
                return function(e) {
                    $tar_img.attr('src', e.target.result);
                    initImg();
                };
            })(f);
            reader.readAsDataURL(f);
        }
    };
    
    function nothing(e){
        e.stopPropagation();
        e.preventDefault();
        return false;
    };
});
