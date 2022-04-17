# 输入：
# 4
# 输出：
# *
#  *
#   *
#    *
while True:
    try:
        n = int(input())
        for i in range(n):
            print(' ' * i + "*")
    except:
        break
