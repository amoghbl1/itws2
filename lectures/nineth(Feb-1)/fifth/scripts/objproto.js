
function Pixel(a, r, g, b) {
    this.init(a, r, g, b)
    return this
}

Pixel.prototype.alpha = function() { return (this.c >> 24) & 0xFF }
Pixel.prototype.red   = function() { return (this.c >> 16) & 0xFF }
Pixel.prototype.green = function() { return (this.c >> 8)  & 0xFF }
Pixel.prototype.blue  = function() { return this.c & 0xFF }
Pixel.prototype.init = function(a, r, g, b) {
    a &= 0xFF
    r &= 0xFF
    g &= 0xFF
    b &= 0xFF
    this.c = a << 24 | r << 16 | g << 8 | b
    /* Pixel.prototype.c = a << 24 | r << 16 | g << 8 | b */
}

function MonochromePixel(gray) {
    var scale = gray & 0xFF
    this.init(255, scale, scale, scale)
	return this
}

MonochromePixel.prototype = new Pixel(0, 0, 0,  0);

(function tests() {
    var total_tests = 5
    var tests_failed = 0

/*  
    var p = new Pixel(255, 127, 127, 127)
    console.assert(p instanceof Pixel || ++tests_failed && false, "p instanceof Pixel")
    console.assert(p.constructor == Pixel || ++tests_failed && false, "p.constructor == Pixel")
*/
    var mp = new MonochromePixel(42)
    console.assert(mp instanceof MonochromePixel || ++tests_failed && false, "mp instanceof Pixel")

    var mq = new MonochromePixel(255)
    console.assert(mq.constructor == MonochromePixel.prototype.constructor || ++tests_failed && false, 
                   "mq.constructor == MonochromePixel.prototype.constructor")
    console.assert(mq.constructor == Pixel || ++tests_failed && false, 
                   "mq.constructor == Pixel")
    
    console.log("second --- total tests:  ", total_tests)
    console.log("       --- tests passed: ", total_tests - tests_failed)
    console.log("       --- tests_failed: ", tests_failed) 
})()
