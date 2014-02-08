(function(window) {
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
        var total_tests = 5
        var tests_failed = 0

        var p = Pixel(255, 255, 0, 0)
        console.assert(p instanceof Window || ++tests_failed && false, 
                       "p must be a Window instance!")
        console.assert(p == window || ++tests_failed && false, 
                       "p must be a mutated window!")
        console.assert(p == Pixel(255, 255, 255, 255) || ++tests_failed && false, 
                       "p == window")

        var q = new Pixel(255, 255, 0, 0)
        console.assert(q instanceof Pixel || ++tests_failed && false, 
                       "p must be a Pixel instance!")

        var t = new Pixel(255, 255, 0, 0)
        console.assert(t.blue() == 0 && t.green() == 0 && t.red() == 255 || ++tests_failed && false, 
                       "Pixel behavior failure")

        console.log("second --- total tests:  ", total_tests)
        console.log("       --- tests passed: ", total_tests - tests_failed)
        console.log("       --- tests_failed: ", tests_failed) 
    }

    tests()
})(window)
