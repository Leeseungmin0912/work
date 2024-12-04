// 메뉴 슬라이드
$('nav > ul > li').mouseover(function(){ //메인 메뉴 마우스를 올리면
    $('.sub-menu').stop().slideDown(); // .sub-menu 슬라이드 다운
}).mouseout(function() { //메인 메뉴에서 마우스를 치우면
    $('.sub-menu').stop().slideUp(); //.sub-menu를 슬라이드 업
})

//탭 메뉴
$('.btn-notice').click(function(){ //.btn-notice를 클릭하면
    $('.notice').show(); //.notice를 보여주고
    $('.gallery').hide(); //.gallery를 숨김
    $(this).addClass('on').removeClass('off');
    $('.btn-gallery').addClass('off').removeClass('on');
})

//.btn-gallery를 클릭하면 ~

//탭 메뉴
$('.btn-gallery').click(function(){ //.btn-gallery를 클릭하면
    $('.notice').hide(); //.gallery를 보여주고
    $('.gallery').show(); //.notice를 숨김
    $(this).addClass('on').removeClass('off');
    $('.btn-notice').addClass('off').removeClass('on');
})

//레이어팝업
$('.notice > ul > li:first-child').click(function(){
    $('.modal').show();
})
$('.popup > button').click(function(){
    $('.modal').hide();
})