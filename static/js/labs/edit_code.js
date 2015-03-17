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