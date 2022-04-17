# 输入：
# 3
# 输出：
# * * * *
# * * *
# * *
# *
# * *
# * * *
# * * * *
while True:
    try:
        n = int(input())
        for i in range(n + 1, 0, -1):
            print("* " * i + " " * (n - i + 1))
        for i in range(2, n + 2):
            print("* " * i)
    except:
        break
