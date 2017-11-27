
//function for hide replay
function hideFunction(btn) {
    var x = document.getElementById(btn);
    if (x.style.display == "block") {
        x.style.display = "none";
    } else {
        x.style.display = "block";
    }
}

//clear data when use click data
function clearThis(target){
    target.value= "";
}

//hide commet button, only show when user want to user
$("form textarea[id='id_comment']").click(function () {
    // Handle the click event here
    var x = document.getElementById('submitComment');
    x.style.display = "block";
});
