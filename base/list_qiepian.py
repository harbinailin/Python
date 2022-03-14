# 切片 指定列表元素的要使用的第一个元素和最后一个元素的索引
players = ['charles', 'martine', 'michael', 'florence', 'eli']
# print(players[0:2])
# # 当不指定第一个索引时，Python将从列表头开始，包含表头
# print(players[:2])
# print(players[2:4])
# print(players[:4])
# # 当不指定最后一个索引时，默认打印到最后一个值
# print(players[2:])
# # 打印最后三个人的名字
# print(players[-3:])
# # 注意切片和range()方法类似，可以用第三个参数来指定步长
# print(players[0:4:2])

# 遍历切片
# 输出前三个运动员
for player in players[:3]:
    print(player.title())

# 复制列表
my_foods=['pizza','falafel','carrot cake']
friend_foods=my_foods[:]
print(f"my favourite foods are {my_foods}")
print(f"friend foods are {friend_foods}")
my_foods.append('apple')
friend_foods.append('banana')
print(f"my favourite foods are {my_foods}")
print(f"frined foods are {friend_foods}")