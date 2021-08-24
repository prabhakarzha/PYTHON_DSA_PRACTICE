#  write a program to reverse given stirng or  input string

# s = 'Prabhakar'
# output=s[::-1]
# print(output)

name = input("enter any string:-")
output = name[::-1]
print(output)



# # using reversed method
# # 1.

# names = "Kahsyapsonu"
# r = reversed(names)
# output = '\n'.join(r)
# print(output)


# # 2.
# names = "Kahsyapsonu"
# r = reversed(names)
# output = ''.join(r)
# print(output)

# # 3.
# names = "Kahsyapsonu"
# r = reversed(names)
# for i in r:
# print(r)

# # 4.
# names = input('Enter Some String:')
# r = reversed(names)
# output = ''.join(r)
# print(output)




# # python program to check if a given string is a palindrome or not
# s = input('Enter a string:')

# def isPailindrome(s):
    
#     return s == s[::-1]


# ans = isPailindrome(s)


# if ans:
    
#     print("yes")
    
# else:
#     print("no")


# # write a program to reverse internal content of each word ?

# s ="my name is sonu kashyap"
# l=s.split() 
# print(l)
# l1 = []
# for i in l:
#     l1.append(i[::-1])
# print(l1)


# # write a program to reverse internal content of every second word ?

# s="one two three four five six"
# l= s.split()
# i = 0
# l1=[]
# while i < len(l):
#     if i%2==0:
#         l1.append(l[i])
#     else:
#         l1.append(l[i][::-1])
#     i=i+1
#     output = " " .join(l1)
# print(l1)
# print(output)

# # write a program to print the characters present at even index and odd index seperately for the given string ?

# s= "prabhakar"
# print("characters present at even index:")
# i=0
# while i<len(s):
#     print(s[i])
#     i=i+2
# print("characters present at odd index:")
# i=1
# while i < len(s):
#     print(s[i])
    
#     i=i+2
    
# #   using slice method  

# s= input("enter some input string:")
# print('The characters present at even index:',s[0::2])
# print('The characters present at odd index:',s[1::2])





