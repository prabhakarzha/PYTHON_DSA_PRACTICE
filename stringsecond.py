#  write a program to reverse given stirng or  input string

s = input('enter any string:-')
output = ''
i = len(s)-1
while i >= 0:
    output = output + s[i]
    i=i-1
    

print(output)


#  write a program to reverse order of words pf given string

s = input("enter any string:")
l = s.split()
print(l)
l1 = l[::-1]
print(l1)
output = ' ' .join(l1)
print(output)


# write a program to reverse internal content of each word

s= input("enter any string:h")
l = s.split()
print(l)
l1 = []
for i in l:
    l1.append(i[::-1])
print(l1)


#program to sort characters of the string,first alphabet symbols followed by digits


