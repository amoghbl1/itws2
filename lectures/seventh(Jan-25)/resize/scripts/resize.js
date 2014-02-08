
function onWindowResize(e) {
	var h = window.innerHeight
	var w = window.innerWidth
	var el = document.getElementById('height')
	el.innerText = 'height: ' + h
	el = document.getElementById('width')
	el.innerText = 'Width: ' + w
}

function main() {
    window.addEventListener("resize", onWindowResize)
    onWindowResize()
}

// this is where the execution of the script begins
window.addEventListener("load", main)
