row= int(input("enter the row number:"))
col = int(input("enter the column number:"))
print("Enter the element for the matrix1:")

matrix1 = [[int(input()) for i in range(col)] for j in range(row)]
print("matrix1:")

for i in range(row):
    for j in range(col):
        print(format(matrix1[i][j],"<3"),end = "")
    print()
print("Enter the element for the matrix2:")

matrix2 = [[int(input()) for i in range(col)] for j in range(row)]
print("matrix2:")

for i in range(row):
    for j in range(col):
        print(format(matrix2[i][j],"<3"),end = "")
    print()
        


