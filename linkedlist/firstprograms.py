class Node:
    def __init__(self, data,next):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):     #__init__ cl level built in method
        self.head =None
        self.tail = None
        self.size = 0

    def __len__(self):
        return self.size
    def isempty(self):     # isempty is our own defined method. so we will not use __isempty__
        # return self.size == 0
        return self.head == None

    def addlast(self,data):
        newest = Node(data,None)  #node is calling here .when we pass the data in node it will store in newest variable
        if self.isempty():
            self.head = newest
        else:
            self.tail.next = newest
        self.tail = newest
        self.size += 1
        
    def display(self):
        p = self.head
        while p:
            print(p.data,end = '-->')
            p=p.next
        print()
L = LinkedList()
L.addlast(7)
L.addlast(4)
L.addlast(12)
L.addlast(8)
L.addlast(3)


L.display()
print('size:',len(L))

        
    
    