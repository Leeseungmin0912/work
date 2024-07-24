$('nav > ul > li').mouseover(function(){
    $('.sub-menu').stop().slideDown();
}).mouseout(function(){
    $('.sub-menu').stop().slideUp();
})