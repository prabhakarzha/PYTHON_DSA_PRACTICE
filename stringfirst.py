#  write a program to reverse given stirng or  input string

s = 'Prabhakar'
output=s[::-1]
print(output)

name = input("enter any string:-")
output = name[::-1]
print(output)


# using reversed method
# 1.

names = "Kahsyapsonu"
r = reversed(names)
output = '\n'.join(r)
print(output)


# 2.
names = "Kahsyapsonu"
r = reversed(names)
output = ''.join(r)
print(output)

# 3.
names = "Kahsyapsonu"
r = reversed(names)
for i in r:
print(r)

# 4.
names = input('Enter Some String:')
r = reversed(names)
output = ''.join(r)
print(output)
