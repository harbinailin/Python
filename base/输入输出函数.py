# input()函数从标准输入读入一行文本，默认的标砖输入是键盘
# print()可以输出格式化的数据 字符串和变量之间用%分隔
# aa = input("请输入：")
# print("你输入的内容：", aa)
x = 5
print("x=%.2f" % x)
print("x=%d" % x)
y = "hello"
print("x=%d,y=%s" % (x, y))
print("%d %s" % (x, y))
# 输出字典对象的值，就将字典对象的键值用小括号包含起来
dic = {'x': '5', 'y': '12.3', 'z': 'hello'}
print("%(x)s, %(y)s, %(z)s" % dic)
# 默认情况下，print()函数输出是换行的，如果不要换行，需要在变量的末尾加上end=""
a = "博主名："
b = "二琳爱吃肉"
print(a, end="")
print(b, end="")
print()
