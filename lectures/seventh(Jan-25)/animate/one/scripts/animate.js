
var turns = 1
var blueCircleAnimation = null

function animateBlueCircle() {
    var circle = document.getElementById("circle-blue")
    var ww = window.innerWidth
    var pos = turns * 5
    var cw = circle.scrollWidth
    circle.style.left = pos + "px"
    if (pos + cw < ww) {
        blueCircleAnimation = requestAnimationFrame(animateBlueCircle)
    } else {
        cancelAnimationFrame(blueCircleAnimation)
    }
    ++turns
}

function animate() {
    animateBlueCircle()
}

function main() {
    if (window.requestAnimationFrame) requestAnimationFrame(animate)
}

// this is where the execution of the script begins
window.addEventListener("load", main)
