class Solution:
    def search(self, nums: list[int], target: int) -> int:
        """
        :param nums: 有序数组
        :param target: 目标值
        :return:数组中若存在目标值，则返回目标值的下标值，否则返回-1
        """
        left = 0
        right = len(nums) - 1
        while left <= right:
            mid = int((left + right) / 2)
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                right = mid - 1
            else:
                left = mid + 1
        return -1


nums = [2, 5, 7, 9, 12, 16, 15]
target = 5
print(Solution().search(nums, target))
