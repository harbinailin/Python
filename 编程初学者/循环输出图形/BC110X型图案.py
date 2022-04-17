# 输入：
# 5
# 输出：
# *   *
#  * *
#   *
#  * *
# *   *
# 示例2
# 输入：
# 6
# 输出：
# *    *
#  *  *
#   **
#   **
#  *  *
# *    *
while True:
    try:
        n = int(input())
        for i in range(n):
            for j in range(n):
                if i == j or i + j + 1 == n:
                    print('*', end="")
                else:
                    print(' ', end="")
            print()
    except:
        break
