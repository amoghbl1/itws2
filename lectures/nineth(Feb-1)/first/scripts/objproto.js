
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

function tests() {
    var p = Pixel(255, 255, 0, 0)
    console.assert(p instanceof Window, "p must be a Window instance!")

    var q = new Pixel(255, 255, 0, 0)
    console.assert(q instanceof Pixel, "p must be a Pixel instance!")

    console.log("first --- all tests passed")
}

tests()
