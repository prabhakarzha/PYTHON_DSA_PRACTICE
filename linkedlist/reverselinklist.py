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
        

    def display(self):
        temp = self.head
        while temp:
            print(temp.data, end='-->')
            temp = temp.next
            
            
    def reversenode(self,data):
        prev=None
        cur = self.head
        while(cur!=None):
            temp=cur.next #node ko khone se bchne k liy hm ise temp m store kr lete h
            cur.next=prev
            prev=cur
            cur=temp
        self.head=prev
    
L = SingleLinkedList()
L.addfirst(1)
L.addlast(2)
L.addlast(3)
L.addlast(4)
L.addlast(5)
L.addlast(6)
print("Given Linked list:-")
L.display()
L.reversenode(2) 
print("\nreverse Linked list")
L.display()

        
        
  
    
     
        
            
      







        
        
            
            
        
        
        
            

            
                
                    
        
      
    
        
        
      





            
        
      
            
            
        
        

    