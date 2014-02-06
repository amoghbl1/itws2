
class Base(object):
    def __init__(self):
	    self.x = 0
	    self.y = 0
	    #print "Base::__init__()"
    
    def increment(self):
        self.x += 1
        self.y += 1

class AnotherBase(object):
    def __init__(self):
        self.x = 100
        self.y = 100
        #print "AnotherBase::__init__()"

    def increment(self):
        self.x += 2
        self.y += 2

    def decrement(self):
        self.x -= 1
        self.y -= 1

class Derived(Base):
    def __init__(self):
        super(Derived, self).__init__()

    def stay_put(self):
    	super(Derived, self).increment()
    	self.x -= 1
    	self.y -= 1
    	#print self.x, self.y

    def __str__(self):
        return "Derived: (x: %s, y: %s)" % (self.x, self.y)


class MultiDerived(Base, AnotherBase):
    def __init__(self):
        Base.__init__(self)
        AnotherBase.__init__(self)
    
    def increment(self):
    	super(MultiDerived, self).increment()

def runAllTests():
    def testDerived():
        d = Derived()
        assert(d.x == 0 and d.y == 0)
        assert(str(d) == "Derived: (x: 0, y: 0)")
        
        prev_x = d.x
        prev_y = d.y
        d.stay_put()
        assert(d.x == prev_x and d.y == prev_y)

    def testMultiDerived():
    	d = MultiDerived()
        assert(d.x == 100 and d.y == 100)
    	
    	d.increment()
        assert(d.x == 101 and d.y == 101)

    "Call each test<X> function"
    testDerived()
    testMultiDerived()


runAllTests()
