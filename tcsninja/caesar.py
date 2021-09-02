# def ceaser(text,key):
#     result = ""
#     for i in range(len(text)):
#         char = text[i]
#         if (char.isupper()):
#             result+=char((ord(char)+key-65)%26+65)
#         elif (char.islower()):
#             result+=chr((ord(char)+key-97)%26 +97)
#         elif (char.isdigit()):
#             result+=str((int(char)+key))
#         elif(char =='-'):
#             result+='-'
#         elif(char.isspace()):
#             result+=" " 
#     return result
# text = input(("enter plain text:"))
# key = int(input("enter the key:"))
# print(ceaser(text,key))

diction = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
def Encrypt(message,key):
    result = ""
    for i in message:
        location = key + diction.index(i)
        location%=26
        result+=diction[location]
    print("value:")
    return result
message = input(("enter plain text:"))
key = int(input("enter the key:"))
print(Encrypt(message,key))
        
    