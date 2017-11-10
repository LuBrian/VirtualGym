
//hide replay function
// $("#button").click(function() {
//   $("#fn").show();
//   $("#button").hide();
// });

function myFunction(btn) {
    var x = document.getElementById(btn);
    if (x.style.display === "block") {
        x.style.display = "none";
    } else {
        x.style.display = "block";
    }
}
