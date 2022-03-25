# arr = [1,2,3,4,5]
# k = 3
# output = [3,2,1,5,4]

arr = [1,2,3,4,5]
k = 3
res = []
for i in range(0,len(arr),k):
    res.append((arr[i:i+k])[::-1])
print(res)
    
