$(document).ready(function () {

    // makes button change color when mouse enters/leaves
    $("button.search_button").mouseenter(function () { 
        $(this).addClass("search_hover")
    });

    $("button.search_button").mouseleave(function () {
        $(this).removeClass("search_hover")
    
    });

    // makes the heading bigger/smaller when mouse enters/leaves
    $("a.search_heading").mouseenter(function() {
        $(this).addClass('sizeLarger')
    });

    $("a.search_heading").mouseleave(function () {
        $(this).removeClass('sizeLarger')
    });
});