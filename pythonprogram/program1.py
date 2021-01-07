
#filter() function forms a new list that contains only elements that satisfy a certain condition

def starts_with_A(s):
      return s[0]=="A"

fruit =["Apple","Banana","pear","mango","Apricot"]
filter_object =filter(starts_with_A,fruit)
print(list(filter_object))

