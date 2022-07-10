# 题目给出一个长度为n的数组，其中有一个数字出现次数超过了数组长度的一半，
# 需要我们找出这个数字输入数组非空，保证有解，这样就不用考虑特殊情况
# 具体做法：
#
#     step 1：构建一个哈希表，统计数组元素各自出现了多少次，即key值为数组元素，value值为其出现次数。
#     step 2：遍历数组，每遇到一个元素就把哈希表中相应key值的value值加1，用来统计出现次数。
#     step 3：本来可以统计完了之后统一遍历哈希表找到频次大于数组长度一半的key值，
#     但是根据我们上面加粗的点，只要它出现超过了一半，不管后面还有没有，必定就是这个元素了，
#     因此每次统计后，我们都可以检查value值是否大于数组长度的一半，如果大于则找到
class Solution:
    def MoreThanHalfNum_Solution(self, numbers: list[int]) -> int:
        hash = dict()
        for i in range(len(numbers)):
            if numbers[i] in hash:
                hash[numbers[i]] += 1
            else:
                hash[numbers[i]] = 1
            if hash[numbers[i]] >= (int)(len(numbers) / 2):
                return numbers[i]
        return 0
