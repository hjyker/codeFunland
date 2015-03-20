$(function(){
    var jcrop_api;
    var $preview = $('#preview_box');
    
    $("#id_avatar_link").change(handleFileSelect);
    
    initJcrop(); 

    function initJcrop(){
        //jcrop_api = $.Jcrop("#target");  
        $("#target").Jcrop({ 
            onChange:showPreview,
            onSelect:showPreview,
            aspectRatio:1
        },function(){
            var bounds = this.getBounds();
            jcrop_api = this;
            $preview.appendTo(jcrop_api.ui.holder);
        });
        $("#crop_preview").attr('src', $('#target').attr('src'));
    };
    
    //简单的事件处理程序，响应自onChange,onSelect事件，按照上面的Jcrop调用
    function showPreview(coords){
        if(parseInt(coords.w) > 0){
            //计算预览区域图片缩放的比例，通过计算显示区域的宽度(与高度)与剪裁的宽度(与高度)之比得到
            var rx = $("#preview_box").width() / coords.w;
            var ry = $("#preview_box").height() / coords.h;
            //通过比例值控制图片的样式与显示
            
            console.log($("#target").width(),$("#target").height());
            
            $("#crop_preview").css({
                //预览图片宽度为计算比例值与原图片宽度的乘积
                width:Math.round(rx * $("#target").width()) + "px",
                //预览图片高度为计算比例值与原图片高度的乘积
                height:Math.round(rx * $("#target").height()) + "px",
                marginLeft:"-" + Math.round(rx * coords.x) + "px",
                marginTop:"-" + Math.round(ry * coords.y) + "px"
            });
        }
    };
    
    function handleFileSelect(evt) {
        //方案一：jcrop_api.destroy()，重置target,但是不能设置crop_preview的图
        //方案二：直接重置jcrop_holder里的两张图(否定了)
        jcrop_api.destroy();
        /* if($('.crop_preview')){
            
        } */
        console.log("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!");
        var    $tar_img = $('#target'),
            $crop_img = $('#crop_preview'),
            $jcrop_holder = $('.jcrop-holder img');
        
        //重置target里图片的width/height
        $tar_img.css({
            'width':'auto',
            'height':'auto'
        });
        
        console.log("fdfdf : "+$tar_img.width(), $tar_img.height());
        
        $('.jcrop-holder').css({
            'width':$tar_img.width() + "px",
            'height':$tar_img.height() + "px"
        });
        
        //重置jcrop_holder里的图片的width/height
        $jcrop_holder.css({
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
                    /* $jcrop_holder.attr('src', e.target.result); */
                    initJcrop();
                    if($crop_img){
                        $crop_img.attr('src', e.target.result);
                    }
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
/**
$(function(){
    initImg();
    document.getElementById('id_avatar_link').addEventListener('change', handleFileSelect, false);
});

function initImg() {
    console.log(1);
    var $img = $('#target'),
        img_w = $img.width(),
        img_h = $img.height(),
        end;
    if(img_w > 400 || img_h > 400){
        w = img_w > img_h ? '400px' : 'auto';
        h = img_w > img_h ? 'auto' : '400px';
    } else {
        w = img_w;
        h = img_h;
    }
    $img.css({
        'width':w,
        'height':h
    });
}

function handleFileSelect(evt) {
    var $img = $('.jcrop-holder img'),
        $tar_img = $('#target');

    
    var files = evt.target.files;
    for (var i = 0, f; f = files[i]; i++) {

        if (!f.type.match('image.*')) {
            continue;
        }

        var reader = new FileReader();
        reader.onload = (function(theFile) {
            return function(e) {
                $img.attr('src', e.target.result);
                $tar_img.attr('src', e.target.result);
            };
        })(f);
        reader.readAsDataURL(f);
    }
}

$(document).ready(function(){
    var $preview = $('#preview_box');
    $("#target").Jcrop({ 
        onChange:showPreview,
        onSelect:showPreview,
        aspectRatio:1
    },function(){
        var bounds = this.getBounds();
        jcrop_api = this;
        $preview.appendTo(jcrop_api.ui.holder);
    });
    //简单的事件处理程序，响应自onChange,onSelect事件，按照上面的Jcrop调用
    function showPreview(coords){
        if(parseInt(coords.w) > 0){
            //计算预览区域图片缩放的比例，通过计算显示区域的宽度(与高度)与剪裁的宽度(与高度)之比得到
            var rx = $("#preview_box").width() / coords.w;
            var ry = $("#preview_box").height() / coords.h;
            //通过比例值控制图片的样式与显示
            console.log($("#target").width(),$("#target").height());
            $("#crop_preview").css({
                //预览图片宽度为计算比例值与原图片宽度的乘积
                width:Math.round(rx * $("#target").width()) + "px",
                //预览图片高度为计算比例值与原图片高度的乘积
                height:Math.round(rx * $("#target").height()) + "px",
                marginLeft:"-" + Math.round(rx * coords.x) + "px",
                marginTop:"-" + Math.round(ry * coords.y) + "px"
            });
        }
    }
});


//jcrop
jQuery(function($){

    // Create variables (in this scope) to hold the API and image size
    var jcrop_api,
        boundx,
        boundy,

        // Grab some information about the preview pane
        $preview = $('#preview-pane'),
        $pcnt = $('#preview-pane .preview-container'),
        $pimg = $('#preview-pane .preview-container img'),

        xsize = $pcnt.width(),
        ysize = $pcnt.height();
    
    console.log('init',[xsize,ysize]);
    $('#target').Jcrop({
      onChange: updatePreview,
      onSelect: updatePreview,
      aspectRatio: xsize / ysize
    },function(){
      // Use the API to get the real image size
      var bounds = this.getBounds();
      boundx = bounds[0];
      boundy = bounds[1];
      // Store the API in the jcrop_api variable
      jcrop_api = this;

      // Move the preview into the jcrop container for css positioning
      $preview.appendTo(jcrop_api.ui.holder);
    });

    function updatePreview(c)
    {
      if (parseInt(c.w) > 0)
      {
        var rx = xsize / c.w;
        var ry = ysize / c.h;

        $pimg.css({
          width: Math.round(rx * boundx) + 'px',
          height: Math.round(ry * boundy) + 'px',
          marginLeft: '-' + Math.round(rx * c.x) + 'px',
          marginTop: '-' + Math.round(ry * c.y) + 'px'
        });
        
        //console
        $('.x1 input').val(c.x);
        $('.y1 input').val(c.y);
        $('.width input').val(c.w);
        $('.height input').val(c.h);
        $('.x2 input').val(c.x2);
        $('.y2 input').val(c.y2);
      }
    };
});
**/