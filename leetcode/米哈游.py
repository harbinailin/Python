import sys

if __name__ == "__main__":
    """
    输入
5 2
1 4 2 6 5
2 3
输出
4 1 6 5 2
排序 按照输入的index 倒序
    """
    # 读取每一行
    line = sys.stdin.readline().strip()
    # 把每一行的数字分隔后转化成int列表
    values = list(map(int, line.split()))
    # n = values[0]
    # m = values[1]
    line = sys.stdin.readline().strip()
    values1 = list(map(int, line.split()))
    # print(values1)
    line = sys.stdin.readline().strip()
    values2 = list(map(int, line.split()))
    i = 0
    n = values2[0]
    newlist = []
    for i in range(n):
        newlist.append(values1)
        print(sorted(newlist, reverse=True))
