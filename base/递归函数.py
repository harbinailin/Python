# # 函数直接或间接调用了本身 称为函数的递归调用 这个函数称为递归函数
# def func(n):
#     if n == 1:
#         return 1
#     return n * func(n - 1)

# 尾递归优化
def f1(num, product):
    if num == 1:
        return product
    return f1(num - 1, num * product)


def f(n):
    return f1(n, 1)


# n = int(input("请输入n的值："))
print(f(1000))

# 汉诺塔问题 递归求解
# f(n) = n != 1 * 2 * 3 * ... * (n - 1) * n = (n - 1)!*n = f(n - 1) * n


# def move(n, a, b, c):
#     """
#     有三根杆(编号A、B、C)，在A杆自下而上、由大到小按顺序放置n个圆盘
#     游戏的目标：把A杆上的圆盘全部移到C杆上，并仍保持原有顺序叠好。
#     操作规则：每次只能移动一个盘子，并且在移动过程中三根杆上都始终保持大盘在下，
#     小盘在上，操作过程中盘子可以置于A、B、C任一杆上。
#     :param n: 圆盘个数
#     :param a: 第一个杆子
#     :param b: 第二个杆子
#     :param c: 第三个杆子
#     :return: 每次移动的路径
#     """
#     if n == 1:
#         print(a, '-->', c)
#         return
#     else:
#         move(n - 1, a, c, b)  # 首先需要将(n-1)个圆盘移动到b杆子上
#         move(1, a, b, c)  # 将a杆子上的最后一个圆盘移动到c杆子上
#         move(n - 1, b, a, c)  # 再将b杆子上的(n-1)个圆盘移动到c杆子上
#
#
# move(3, 'A', 'B', 'C')
