class Node:
    def __init__(self,data,next):
        self.data=data
        self.next = None
class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0
        
    def isempty(self):
        return self.head == None
        
    def addlast(self,data):
        newest = Node(data,None)  #node is calling here .when we pass the data in node it will store in newest variable
        if self.isempty():
            self.head = newest
        else:
            self.tail.next = newest
        self.tail = newest
        self.size += 1
items = LinkedList()
items.addlast('sonu')
items.addlast('kashyap')
print("\nhead.data: ",items.head.data)
print("tail.data: ",items.tail.data)
print(items)

