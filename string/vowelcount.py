string = input('enter a string:-')
final = string.lower()
vowels = 0
for i in final:
    if(i=='a' and 'A' or i=='e' or i=='i' or i=='o' or i=='u'):
        vowels += 1
print("number of vowels are:")
print(vowels)