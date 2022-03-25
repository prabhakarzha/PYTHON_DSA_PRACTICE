class Node:

    def __init__(self, data, next, prev):
        self.data = data
        self._next = next
        self._prev = prev

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self._size = 0

    def __len__(self):
        return self._size

    def isempty(self):
        return self._size == 0

    def addlast(self, e):
        newest = Node(e, None, None)
        if self.isempty():
            self.head = newest
            self.tail = newest
        else:
            self.tail._next = newest
            newest._prev = self.tail
            self.tail = newest
        self._size += 1
        
    def addfirst(self,e):
        newest = Node(e, None, None)
        

        newest._next = self.head
        self.head._prev = newest
        self.head = newest
        self._size += 1

    def display(self):
        p = self.head
        while p:
            print(p.data,end=' --> ')
            p = p._next
        print()

    def displayrev(self):
        p = self.tail
        while p:
            print(p.data,end=' <-- ')
            p = p._prev
        print()


L = DoublyLinkedList()
L.addlast(7)
L.addlast(4)
L.addlast(12)
L.addlast(8)
L.addlast(3)
L.addfirst(11)
L.display()
print('Size:',len(L))
L.displayrev()














