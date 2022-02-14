class Node:
    def __init__(self, data,next):
        self.data = data
        self.next = None
class SingleLinkedList:
    def __init__(self):
        self.head=None
        
    def addfirst(self,data):
        newest=Node(data,next)
        newest.next=self.head

        self.head = newest
        
    def addlast(self,data):
        newest=Node(data,next)
        temp=self.head
        while(temp.next!=None):
            temp = temp.next
        temp.next = newest
        
    def specificadd(self,data,pos):
        newest=Node(data,next)
        temp=self.head
        for i in range(pos-1):
            temp = temp.next
        newest.next=temp.next
        temp.next = newest
    def removefirst(self,data):
        self.head=self.head.next
        
    def removelast(self,data):
        temp=self.head
        while (temp.next.next !=None):
            temp=temp.next
        temp.next=None
    
    def specificdel(self,data,pos):
        temp=self.head
        for i in range(pos-1):
            temp=temp.next
        temp.next=temp.next.next
        
        
    #delete a node without head pointer
            
    # def withoutheadremove(self,node):
    #     node.data=node.next.data
    #     node.next=node.next.next
        
    #delete a last node of single link list
    
     
        
            
    def display(self):
        temp = self.head
        while temp:
            print(temp.data, end='-->')
            temp = temp.next
      
L = SingleLinkedList()
L.addfirst(5)
L.addfirst(6)
L.addfirst(1)
L.addlast(7)
L.addlast(4)
L.addlast(12)
L.addlast(13)

# L.specificadd(2,3)
# L.removefirst(1)
# L.removelast(1)
# L.removelast(1)
# L.specificdel(2,2)
# L.withoutheadremove(L.head.next.next)


L.display()
        
        
            
            
        
        
        
            

            
                
                    
        
      
    
        
        
      





            
        
      
            
            
        
        

    