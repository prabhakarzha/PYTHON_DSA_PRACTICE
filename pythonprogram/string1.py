# value = input("enter a string:")
# value = value.lower()
# frequency={}
# for i in value:
#     if i in frequency:
#         frequency[i]=frequency[i]+1
#     else:
#         frequency[i]=1
# print(str(frequency))


value = input("enter a string:")
value= value.lower()
words = value.split()
for i in words:
    print(i[0])

    
