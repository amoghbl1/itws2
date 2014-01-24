
var turns = 1
var blueCircleAnimation = null
var orangeCircleAnimation = null

function animateOrangeCircle() {
    var circle = document.getElementById("circle-orange")
    var ww = window.innerWidth
    var pos = turns * 4
    var cw = circle.scrollWidth
    circle.style.left = pos + "px"
    if (pos + cw < ww) {
        orangeCircleAnimation = requestAnimationFrame(animateOrangeCircle)
    } else {
        cancelAnimationFrame(orangeCircleAnimation)
    }
    
    turns++
}

function animateBlueCircle() {
    var circle = document.getElementById("circle-blue")
    var ww = window.innerWidth
    var pos = turns * 6
    var cw = circle.scrollWidth
    circle.style.left = pos + "px"
    if (pos + cw < ww) {
        blueCircleAnimation = requestAnimationFrame(animateBlueCircle)
    } else {
        cancelAnimationFrame(blueCircleAnimation)
    }
}

function animate() {
    animateBlueCircle()
    animateOrangeCircle()
}

function main() {
    if (window.requestAnimationFrame) requestAnimationFrame(animate)
}

// this is where the execution of the script begins
window.addEventListener("load", main)
