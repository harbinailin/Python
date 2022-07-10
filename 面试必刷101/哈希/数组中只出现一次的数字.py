# 一个整型数组里除了两个数字只出现一次，其他的数字都出现了两次。请写程序找出这两个只出现一次的数字。降序输出
# step 1: 遍历数组，用哈希表统计每个数字出现的频率。
# step 2: 然后再遍历一次数组，对比哈希表，找到出现频率为1的两个数字。
# step 3: 最后整理次序输出。
class Solution:
    def FindNumsAppearOnce(self, array: list[int]) -> list[int]:
        res = []
        hash = dict()
        for i in range(len(array)):
            if array[i] in hash:
                hash[array[i]] += 1
            else:
                hash[array[i]] = 1
        for i in range(len(array)):
            if hash[array[i]] == 1:
                res.append(array[i])
        res.sort(reverse=False)
        return res
