# 给出一个整型数组 numbers 和一个目标值 target，请在数组中找出两个加起来等于目标值的数的下标，返回的下标按升序排列。
class Solution():
    def twoSum(self, numbers: list[int], target: int) -> list[int]:
        # 哈希表是一种根据关键码（key）直接访问值（value）的一种数据结构。
        # 而这种直接访问意味着只要知道key就能在O(1)O(1)O(1)时间内得到value，
        # 因此哈希表常用来统计频率、快速检验某个元素是否出现过等。
        # 解法
        # step 1：构建一个哈希表，其中key值为遍历数组过程中出现过的值，value值为其相应的下标，因为我们最终要返回的是下标。
        # step 2：遍历数组每个元素，如果目标值减去该元素的结果在哈希表中存在，说明我们先前遍历的时候它出现过，根据记录的下标，就可以得到结果。
        # step 3：如果相减后的结果没有在哈希表中，说明先前遍历的元素中没有它对应的另一个值，那我们将它加入哈希表，等待后续它匹配的那个值出现即可。
        # step 4：需要注意最后的结果是下标值加1.

        res = []
        # 创建hash表，二元组分别表示数组下标和值
        hash = dict()
        for i in range(len(numbers)):
            # 在哈希表中查找值为target-numbers[i]
            temp = target - numbers[i]
            if temp not in hash:
                # 如果temp不在hash表中，我们将他存入hash
                hash[numbers[i]] = i
            else:
                # 如果temp在hash中，我们将两个数的下标存在res列表中，并返回
                res.append(hash[temp] + 1)
                res.append(i + 1)
                break
        return res
