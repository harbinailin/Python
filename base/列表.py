# # list 用方括号[] 表示列表,用逗号,分割其中的元素
# # list 列表通常用来存储一些经常变化的东西，比如游戏角色之类的，一些不可修改的值的集合通常用元组
# webdrivre = ['chorme', 'firefox', 'safari', 'ie', '360']
# print(webdrivre)
# # 访问列表元素，按照索引从0开始
# print(webdrivre[0])
# # 返回最后一个列表元素索引值=-1 倒数第二个元素-2
# # 可以用于返回不知列表长度时，返回最后的元素
# print(webdrivre[-1])
# # 和f字符串组合使用，返回消息
# message = f"My favourite webdriver is {webdrivre[0].title()}."
# print(message)
#
# # 修改列表元素
# webdrivre[0] = 'CHROME'
# print(webdrivre)
#
# # 添加列表元素 append
# webdrivre.append('chrome dev')
# print(webdrivre)
#
# # 动态创建列表 先创建空列表，用于存储用户输入的值，然后将用户提供的新值添加到列表中
# list = []
# list.append('i')
# list.append('am')
# list.append('ailin')
# print(list)
#
# # 插入元素 insert
# webdrivre.insert(2, 'new 360')
# print(webdrivre)
#
# # 删除元素
# # way1 已知要删除的元素再列表中，可以使用del语句
# del webdrivre[2]
# print(webdrivre)
# # way2 使用pop方法删除元素，(列表尾部元素，列表最后一个元素)可以将删除的元素另存，再使用
# popped_webdriver = webdrivre.pop()
# print(webdrivre)
# # 将被删除的尾部元素输出
# print(f"\t{popped_webdriver}")
# # way3 使用pop(i)弹出列表中任意位置的元素
# first_webdriver = webdrivre.pop(3)
# print(f"my favourite webdriver is {first_webdriver}")
# print(webdrivre)
# # 根据元素值删除元素 当不知道元素位置时候，但是知道元素的值，可以用remove,但是remove只会删除第一个出现的值，所以列表中如果有多个相同需要删除的元素，就需要使用循环
# webdrivre.remove('360')
# print(webdrivre)
# my_webdirver = 'firefox'
# webdrivre.remove(my_webdirver)
# print(webdrivre)
print(f"my webdirver is {my_webdirver}")

# 给定两个列表，返回相同和不同的元素
list1=[1,2,3]
list2=[2,4,5]
set1=set(list1)
set2=set(list2)
# 相同求和 不同求或
print(set1 & set2)
print(set1 ^ set2)