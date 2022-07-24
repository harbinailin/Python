class Solution:
    def Find(self, target: int, array: list[list[int]]) -> bool:
        n = len(array)
        m = len(array[0])
        if n == 0 and m == 0:
            return False
        i = n - 1
        j = 0
        while i >= 0 and j < m:
            if array[i][j] > target:
                i = i - 1
            elif array[i][j] < target:
                j = j + 1
            else:
                return True
        return False


target = 7
array = [[1, 2, 8, 9], [2, 4, 9, 12], [4, 7, 10, 13], [6, 8, 11, 15]]
print(Solution().Find(target, array))
