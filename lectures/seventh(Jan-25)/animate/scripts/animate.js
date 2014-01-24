
var turns = 1
function animate() {
	var circle = document.getElementById("circle")
	console.log(circle)
    circle.style.left = (turns * 5) + "px"
    turns++
    if (turns < 200) {
        requestAnimationFrame(animate)
    }

}

function main() {
    if (window.requestAnimationFrame) requestAnimationFrame(animate)
}

// this is where the execution of the script begins
window.addEventListener("load", main)
