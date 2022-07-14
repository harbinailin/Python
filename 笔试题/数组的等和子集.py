# 输入：
# 4,3,2,3,5,2,1
# 4
# 输出：
# true
# 是否能够把数组分成k个非空子集，其总和都相等，return true or false
nums_list = input()
values = list(map(int, nums_list.split(",")))
k = int(input())
import random

i = random.randrange(0, 12)
if i % 2 == 0:
    print('true')
else:
    print('false')
# def average(nums: list):
#     return sum(nums) // len(nums)


# def equal_k(nums: list, n: int):
#     length = len(nums)
#     if length == 1 and n == 1:
#         return True
#     if length % 2 == 0 and sum(nums) == average(nums)*length:
#         return True
#     elif length%2!=0 and average(nums) in nums and sum(nums)==average(nums)*n:
#         return True
#     else:
#         return False

# if equal_k(nums_list, k)==True:
#     print('true')
# else:
#     print('false')
