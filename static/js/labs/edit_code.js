$(function(){
	init();
	onFun();
});

function init(){
	var editorHeight = $(window).height() - 51;
	$('.doc-content').css('height', editorHeight);
	$('.doc-text').css('height', editorHeight - 60);
	$('.editor-content').css('height', editorHeight);
	$('#editor').css('height', editorHeight - 50);
    $('.console').css('height', editorHeight - 50);
}

function onFun(){
	$(window).resize(function(){
		var editorHeight = $(window).height() - 51;
		$('.doc-content').css('height', editorHeight);
		$('.doc-text').css('height', editorHeight - 60);
		$('.editor-content').css('height', editorHeight);
		$('#editor').css('height', editorHeight - 50);
        $('.console').css('height', editorHeight - 50);
		console.log($(window).height());
	})
}

/* $(".btn-save").click(function(){
    var val = editor.getValue();
    var result = null;
    
    var Arr = val.split(/\n/g);
    var html = "";
    for(var i = 0; Arr[i]; i++){
        try {
            result = eval(Arr[i]);
        } catch(exception) {
           result = exception;
        }
        html += "<div>JavaScripy>&nbsp;"+ Arr[i] +"</div>"+
                "<div>>&nbsp;"+ result +"</div>";
    }
    $('.console-content').html("").append(html);
}) */
