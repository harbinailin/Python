# 编写函数求满足条件的最大n值：
# 1**2+3**2+5**2+...+(2*n-1)**2<a
a = int(input("请输入a的值："))


def func1(n: int):
    if n == 1:
        return 1
    else:
        return (2 * n - 1) ** 2 + func1(n - 1)


for i in range(1, 100):
    if func1(i + 1) > a and func1(i) < a:
        print(f"满足条件的最大n值为{i}")
