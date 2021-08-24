        

row = int(input("Enter the value of row: "))
col = int(input("Enter the value of col: "))

def matrix(row,col):
    o=[]
    for i in range(row):
        row=[]
        for j in range(col):
            inp = int(input(f"Value of o[{i}][{j}]:-"))
            row.append(inp)
        o.append(row)
    return o

def sum(A,B):
    output = []
    for i in range(len(A)):  #number of rows 
        row =[]
        for j in range(len(B)): #number of columns 
            row.append(A[i][j]+B[i][j])
        output.append(row)
    return output
            

print("enter matrix A:")
A = matrix(row,col)
print('\n',A)


print("enter matrix B:")
B = matrix(row,col)
print('\n',B)

s= sum(A,B)
print(s)




        




        


