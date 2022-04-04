# 关键字参数
def add(x, y):
    return x + y


print(add(3, 4))
print(add(x=3, y=4))
print(add(y=4, x=3))


# 默认参数
def sub(x, y=10):
    return x - y


print(sub(10))
print(sub(30, 20))


# 可变参数
# * 单星号的变量存放所有未命名的变量
def fruits(name, *args):
    print(name)
    for price in args:
        print(f"可变参数{price}")
    return


fruits("草莓")
fruits("草莓", 18, 19, 20, 21)

# 双星号的参数 代表字典对象
def buy(**args):
    print("水果名：")
    for name in args.keys():
        print(name)
    print("价格：")
    for price in args.values():
        print(price)


buy(草莓=68, 苹果=30)
