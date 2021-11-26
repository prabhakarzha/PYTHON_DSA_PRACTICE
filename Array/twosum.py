# def twosum(nums,target):
#     for i in range(len(nums)):
#         for j in range(i+1,len(nums)):
#             if target - nums[i] ==nums[j]:
#                 return[i,j]
#     return None
# test = [2,7,11,15]
# target = 17
# print(twosum(test,target))


a = [1, 2, 2, 3, 4, 4,]

def find_it(look_here):
    have_seen = set()
    for item in look_here:
        if item in have_seen:
            return item
        have_seen.add(item)

find_it(a)
            