num = [1,2,3,4,6,7,8,9]
def missingno(num):
    n = len(num)+1
    totalsum = n*(n+1)/2
    return totalsum-sum(num)
result = missingno(num)
print(int(result))