class StacksArray:
    def __init__(self):
        self.data = []
        
    def __len__(self):
        return len(self.data)
    def isempty(self):
        return len(self.data)== 0 
    def push(self,e):
        self.data.append(e)
    def pop(self):
        if self.isempty():
            print("Empty stack")
            return
        return self.data.pop()
    def top(self):
        if self.isempty():
            print("Empty stack")
        return self.data[-1]
S=StacksArray()
S.push(input("enter any Value:"))
print(S.data)
print('length:',len(S))




# Stack = []
# def push(Stack):
#     element = input("enter any element:")
#     Stack.append(element)
# def pop(Stack):
#     if len(Stack)==0:
#         print("Stack is empty")
#     else:
#         Stack.pop()
#         print("removed element:")
# push(Stack)
# print(Stack)
# pop(Stack)
# print(Stack)
    

    

    