$(function(){
    initImg();
    document.getElementById('id_avatar_link').addEventListener('change', handleFileSelect, false);
});

function initImg() {
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

    var files = evt.target.files;
    for (var i = 0, f; f = files[i]; i++) {

        if (!f.type.match('image.*')) {
            continue;
        }

        var reader = new FileReader();
        reader.onload = (function(theFile) {
            return function(e) {
                var $img = $('.jcrop-holder img');
                $img.attr('src', e.target.result);
            };
        })(f);
        reader.readAsDataURL(f);
    }
}

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
