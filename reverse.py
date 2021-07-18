# def evennum(k):
#     even=[]
#     for i in k:
#         if i%2!=0:
#             even.append(i)
#     return even
# print(evennum([1,2,3,4,6,8,10,12]))
        
    

    
total_candies = 10
candiescount = int(input("enter no of candies:--"))
if  candiescount in range(1,6):
    print("No.of candies sold:",candiescount)
    print("No. of candies left:", total_candies-candiescount)
else:
    print("invalid input")
    print("No. of candies left:", candiescount)
