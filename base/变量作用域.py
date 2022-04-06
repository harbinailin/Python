# 作用域分为局部作用域和全局作用域
# 局部作用域在函数内部
# 全局作用域 定义在函数外的变量
# Python会首先搜索局部命名空间(local namespace)，在搜索全局命名空间(global namespace)，之后在搜索内置名空间(built-in namespace),最后还是找不到输出NameError异常
# local>global>built-in(int string def print)
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
