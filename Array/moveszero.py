nums=[1,2,0,3,0,40,5,0,6,3,0,9,0,3]

def soution(nums):
    for i in nums:
        if 0 in nums:
            nums.remove(0)
            nums.append(0)
    return nums
print(soution(nums))