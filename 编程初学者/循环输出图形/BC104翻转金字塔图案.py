while True:
    try:
        n = int(input())
        for i in range(n, 0, -1):
            print((n - i) * " " + i * "* ")
    except:
        break
# 输入：
# 5
# 输出：
# * * * * *
#  * * * *
#   * * *
#    * *
#     *