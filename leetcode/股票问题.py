# 数组 i 股票 价格
# 计算最大利润
# 7 1 5 3 6 4
#
def gupiao():
    list = [7, 1, 5, 3, 6, 4]
    list = int(list)
    n = len(list)
    num = 0
    new_list = []
    for i in range(n):
        for j in range(i, n):
            num = list[j] - list[i]
            if num > 0:
                new_list.append(num)
    print(max(new_list))
    # price = sum(new_list)
    # new_list1.append(price)
    # print(new_list1.max())
