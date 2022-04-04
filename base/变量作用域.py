# 作用域分为局部作用域和全局作用域
# 局部作用域在函数内部
# 全局作用域 定义在函数外的变量
x = 100
y = 10


def changex():
    x = 200
    global y
    y = 20
    return x, y


print(x)
print(y)
print(changex())
print(x)
print(y)

