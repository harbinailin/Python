import sys

# abs 求绝对值或负数的大小
print(abs(-99.2))
print(abs(1 + 3j))

# chr 根据ASCII码返回对应的字符 0-255
print(chr(97))  # a
print(chr(122))  # z
print(chr(65))  # A
print(chr(90))  # Z
# ord 返回字符的ACSII码或unicode字符
print(ord("A"))
print(ord("o"))
print(ord("\\"))

# complex 创建一个负数
print(complex(2, 4))
print(complex(3))
print(complex("4"))
print(complex("4+3j"))

# dir(object)返回对象的属性名称列表
print(dir(sys))
print(dir(list))

# float int list tuple max min
print(tuple("wyqhbda"))
# divmod()将a除以b的商和余数以元组的形式展示出来
print(divmod(8, 3))

# pow返回次方数
print(pow(2, 3))
print(pow(2, 3, 5))  # 第三个参数 就是求2的3次方除以5的余数
