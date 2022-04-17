# 输入：
# 4
# 输出：
#    *
#   *
#  *
# *
while True:
    try:
        n = int(input())
        for i in range(n, 0, -1):
            print(" " * (i - 1) + "*")
    except:
        break
94