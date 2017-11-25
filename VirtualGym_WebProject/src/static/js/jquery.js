
//function for hide replay
function myFunction() {
    var x = document.getElementById('Search');
    if (x.style.display == "block") {
        x.style.display = "none";
    } else {
        x.style.display = "block";
    }
}
//<button id="button" style="float: right;" type="button" class="btn btn-info btn-sm" onclick="myFunction({{obj.questionID}})">
