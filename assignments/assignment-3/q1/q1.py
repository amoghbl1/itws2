class DoublyLinkedList(object):
    "Internal representation of a node in the doubly-lined list"
    class Node(object):
        def __init__(self, key, val):
            "initialize the required fields of a node instance"
            self.key = key
            self.val = val
            self.next = None
            self.prev = None
            pass
        
        def __eq__(self, key):
            "compare the content of this node with the key"
            "assuming that content reffers to value"
            return self.val == key
        
        def val(self):
            "return the value stored in this node"
            return this.val

    def __init__(self):
        self.head = None
        self.tail = None
   
    """
    return the number of elements in the list.
    returns a number greater than or equal to zero.
    """
    def length(self):
        retn = 0
        prop = self.head
        while (prop != None):
            retn += 1
            prop = prop.next
        return retn

    """
    creates a new node initialized with 'key' and 'val', and makes
    'head' point to the new node.
    precondition: neither 'key' nor 'val' may be None. 
    postcondition: self.head will point to the new node.
    """
    def insert(self, key, val):
        temp = self.Node(key, val)
        temp.next = self.head
        temp.prev = None
        if self.head == None:
            self.head = temp
            self.tail = temp
            return True
        self.head.prev = temp
        self.head = temp
        return True

    """
    searches from the 'head' of the list, the first occurrence of 'key'. 
    when found, returns 'val' associated with the key.
    returns None when 'key' is not in the list.
    postcondition: Deletes the Node at the head position if it is not None and returns without doing anything if it is none.
    """ 
    def find(self, key):
        prop = self.head
        while prop != None:
            if prop.key == key:
                return prop.val
        return prop

    """
    removes the node, if there's one, at the 'tail' position.
    postcondition: Deletes the Node at the tail position if it is not None and returns without doing anything if it is none.
    """
    def deleteLast(self):
        if self.tail != None:
            self.tail = self.tail.prev
            if self.tail != None:
                self.tail.next=None 
            return True
        return True
        pass
    
    """
    removes the node, if there's one, at the 'head' position.
    postcondition: Deletes the Node at the head position if it is not None and returns without doing anything if it is none.
    """
    def deleteFirst(self):
        if self.head != None:
            self.head = self.head.next
            if self.head != None:
                self.head.prev=None 
            return True
        return True
        pass

    """
    finds the first entry that matches 'key', and deletes it.
    postcondition: Deletes the first entry of key and does not delete anything if it does not find anything matching key.
    """
    def delete(self, key):
        prop = self.head
        while prop != None:
            if prop.key == key:
                if prop.prev != None:
                    prop.prev.next = prop.next
                if prop.next != None:
                    prop.next.prev = prop.prev
            prop = prop.next
        return True
        pass