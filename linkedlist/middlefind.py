class Node:
    def __init__(self, data,next):
        self.data = data
        self.next = None
        
class SingleLinkedList:
    def __init__(self):
        self.head = None
        
        
    def addfirst(self,data):
        newest = Node(data,next)
        newest.next = self.head
        self.head = newest
        
    def addlast(self,data):
        newest = Node(data,next)
        temp=self.head
        while(temp.next!=None):
            temp=temp.next
            
        temp.next=newest
    
    def middlenode(self,data):
        slow=fast = self.head
        while(fast!=None and fast.next!=None):
            slow=slow.next
            fast=fast.next.next
        return slow
    
        
        
            
      
    
    def display(self):
        temp = self.head
        while temp:
            print(temp.data,end = '-->')
            temp=temp.next
            
L= SingleLinkedList()
L.addfirst(1)
L.addlast(2)
L.addlast(3)
L.addlast(4)
L.addlast(5)
L.addlast(6)
L.addlast(7)

L.middlenode(4)
L.display()



        

        