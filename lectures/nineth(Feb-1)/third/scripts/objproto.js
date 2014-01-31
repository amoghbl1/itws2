
function Pixel(a, r, g, b) {
    a &= 0xFF
    r &= 0xFF
    g &= 0xFF
    b &= 0xFF
    this.c = a << 24 | r << 16 | g << 8 | b

    this.alpha = function() { return (this.c >> 24) & 0xFF }
    this.red   = function() { return (this.c >> 16) & 0xFF }
    this.green = function() { return (this.c >> 8)  & 0xFF }
    this.blue  = function() { return this.c & 0xFF }

    return this
}

function MonochromePixel(gray) {
	var scale = gray & 0xFF
	return new Pixel(255, scale, scale, scale)
}

(function tests() {
    var total_tests = 2
    var tests_failed = 0

    var p = new MonochromePixel(127)
    console.assert(p instanceof Pixel || ++tests_failed && false, "p instanceof Pixel")

    var p = new MonochromePixel(127)
    console.assert(p.constructor == Pixel || ++tests_failed && false, 
                   "p.constructor == MonochromePixel")

    console.log("second --- total tests:  ", total_tests)
    console.log("       --- tests passed: ", total_tests - tests_failed)
    console.log("       --- tests_failed: ", tests_failed) 
})()
