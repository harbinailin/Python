# 输入：
# 3
# 输出：
#       *
#     **
#   ***
# ****
#   ***
#     **
#       *
while True:
    try:
        n = int(input())
        for i in range(n + 1, 0, -1):
            print(" " * 2 * (i - 1) + "*" * (n + 2 - i))
        for i in range(n, 0, -1):
            print(" " * 2 * (n - i + 1) + "*" * i)
    except:
        break
