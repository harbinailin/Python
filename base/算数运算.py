# + - * **乘方运算 / //整除只保留整数
# 任意两个数相除时，结果总是浮点数
a = 100
b = 14
print(divmod(a, b))
print(1 + 2)
print(2 - 1)
print(3 * 2)
print(4 / 2)
print(4 // 2)
print(5 // 2)
print(5 / 2)
print(2 ** 3)
# 数字很大时，可以用下划线区分，将数字分组，便于阅读
big_num = 12_000_000_000
print(big_num)
# 同时给多个变量赋值，只要变量名和数值的个数相同即可
x, y, z = 1, 2, 3
print(x, y, z)
# 默认将全部大写的变量看做是常量
MAX_CONNECTIONS = 5000
print(MAX_CONNECTIONS)
