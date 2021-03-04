num=int(input("enter a number"))
for i in range(2, num):
 if num % i ==0:
      print("is not a prime number")
 break
else:
    print("is prime number")
