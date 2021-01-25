//alert("Hello, World!");

document.getElementById("para").innerHTML = "this is javascript from dir"
toggl = document.getElementById("tmp")


function makeRed(element, color) {
    element.style.color = color
}

function toggle() {
    if (toggl.style.display === "none") {
        toggl.style.display = "block";
    } else {
        toggl.style.display = "none";
    }
}