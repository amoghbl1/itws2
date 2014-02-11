from q2 import *
a=DoublyLinkedList()
a.insert("a","a")
a.insert("b","b")
a.insert("c","c")
fli = ForwardListIterator(a)
for i in fli:
	if i==None:
		assert(0)
	assert(1)
