#如果一个内部函数引用了外部作用域（不包括全局变量）的一个变量，那么这个内部函数称之为闭包。
def f1(n):
    def f2(x):
        return (x + n)

    return f2


# p1 = f1(n=2)
# print(p1(x=6))
p1 = f1(2)
print(p1(6))
