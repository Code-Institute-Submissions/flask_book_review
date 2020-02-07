$(document).ready(function () {

    // makes button change color when mouse enters/leaves
    $("button.search_button").mouseenter(function () { 
        $(this).addClass("search_hover")
    });

    $("button.search_button").mouseleave(function () {
        $(this).removeClass("search_hover")
    
    });

});

// Function that pops an alert on the browser with a confirmation before a book is deleted 
function deleteConfirm(id) {
    var message;
    form = document.getElementById("deleteForm" + id);
    
    if (confirm("Are you sure you want to delete? Press okay if you're sure")) {
        message = "Book has been deleted!";
        form.submit();
        
    } else {
        message = "It won't be deleted!";
    }
    document.getElementById("demo").innerHTML = message;
}

