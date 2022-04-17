# 输入：
# 2
# 输出：
#   *
#  * *
# * * *
#  * *
#   *
while True:
    try:
        n = int(input())
        for i in range(1, n + 1):
            print(" " * (n - i + 1) + "* " * i)
        for i in range(n + 1, 0, -1):
            print(" " * (n - i + 1) + "* " * i)
    except:
        break
