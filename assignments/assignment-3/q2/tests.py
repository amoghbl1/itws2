from q2 import *
a = DoublyLinkedList()
a.insert("a","a")
a.insert("b","b")
a.insert("c","c")
fli = ForwardListIterator(a)

for i in fli:
	if i==None:
		assert(0)
	assert(1)
rli = ReverseListIterator(a)

for i in rli:
	if i==None:
		assert(0)
	assert(1)

a = ExtendedDoublyLinkedList()
a.insert("a","A")
a.insert("b","B")
a.insert("c","C")
rli = a.getReverseIterator()

for i in rli:
	if i == None:
		assert(0)
	assert(1)
