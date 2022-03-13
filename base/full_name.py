# 大小写转换 title首字母大写\upper全大写\lower全小写
first_name = 'nice'
second_name = 'ailin'
# f"{name}" 支持Python3.6 format()3.6之前
# way1
full_name = f"{first_name} {second_name}"
print(full_name.title())
# way2
# print("{} {}".format(first_name.title(), second_name.title()))
# way3
# full_name="{} {}".format(first_name.title(),second_name.title())
# print(full_name)

name = "Erlin"
print(name.upper())
print(name.lower())
