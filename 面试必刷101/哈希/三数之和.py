# 哈希+双指针  给出一个有n个元素的数组S，S中是否有元素a,b,c满足a+b+c=0？找出数组S中所有满足条件的三元组。
# step 1：排除边界特殊情况。
# step 2：既然三元组内部要求非降序排列，那我们先得把这个无序的数组搞有序了，使用sort函数优先对其排序。
# step 3：得到有序数组后，遍历该数组，对于每个遍历到的元素假设它是三元组中最小的一个，那么另外两个一定在后面。
# step 4：需要三个数相加为0，则另外两个数相加应该为上述第一个数的相反数，我们可以利用双指针在剩余的子数组中找有没有这样的数对。
# 双指针指向剩余子数组的首尾，如果二者相加为目标值，那么可以记录，而且二者中间的数字相加可能还会有。
# step 5：如果二者相加大于目标值，说明右指针太大了，那就将其左移缩小，相反如果二者相加小于目标值，说明左指针太小了，
# 将其右移扩大，直到两指针相遇，剩余子数组找完了。
class Solution:
    def threeSum(self, num: list[int]) -> list[list[int]]:
        res = list(list())
        n = len(num)
        # 不够三元组
        if n < 3:
            return res
        # 排序
        num.sort()
        for i in range(n - 2):
            if i != 0 and num[i] == num[i - 1]:
                continue
            # 后续的收尾双指针
            left = i + 1
            right = n - 1
            # 设置当前数的负值为目标
            target = -num[i]
            while left < right:
                # 双指针指向的二值相加为目标，则可以与num[i]组成0
                if num[left] + num[right] == target:
                    res.append([num[i], num[left], num[right]])
                    while left + 1 < right and num[left] == num[left + 1]:
                        # 去重
                        left += 1
                    while right - 1 > left and num[right] == num[right - 1]:
                        # 去重
                        right -= 1
                        # 双指针向中间收缩
                    left += 1
                    right -= 1
                # 双指针指向的二值相加大于目标，右指针向左
                elif num[left] + num[right] > target:
                    right -= 1
                # 双指针指向的二值相加小于目标，左指针向右
                else:
                    left += 1
        return res


num = [-10, 0, 10, 20, -10, -40]
print(Solution().threeSum(num))
