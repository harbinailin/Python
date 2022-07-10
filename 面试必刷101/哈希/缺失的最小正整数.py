# 给定一个未排序的整数数组nums，请你找出其中没有出现的最小的正整数
class Solution:
    def minNumberDisappeared(self, nums: list[int]) -> int:
        # step 1：构建一个哈希表，用于记录数组中出现的数字。
        # step 2：从1开始，遍历到n，查询哈希表中是否有这个数字，如果没有，说明它就是数组缺失的第一个正整数，即找到。
        # step 3：如果遍历到最后都在哈希表中出现过了，那缺失的就是n + 1.
        hash = dict()
        for i in range(len(nums)):
            if nums[i] in hash:
                hash[nums[i]] += 1
            else:
                hash[nums[i]] = 1
        res = 1
        while res in hash:
            res += 1
        return res


list_num = [0, 2, 3]
print(Solution().minNumberDisappeared(list_num))
