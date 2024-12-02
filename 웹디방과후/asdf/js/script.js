$(document).ready(function(){

    $(".main").hover(function(){
        $(".sub").stop().slideDown();
    },function(){
        $(".sub").stop().slideUp();
    });

    var i = 4;

    setInterval(function(){
        i--;
        if(i==3) $(".b img").css("left","0")
        $(".b img").eq(i).animate({"left":"1200px"},500);
        console.log(i);
    if(i<=1) i=4;
    },2000);



});