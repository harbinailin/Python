# 字典用花括号{},是一种动态结构，由键值对构成:'key':value,键值对之间用逗号分割。
ailin = {'age': 20, 'name': 'ailin', 'phone-number': '1552702870'}
print(ailin['age'])
ailin['wechat'] = 'harbinailin'
print(ailin)

# 建立空字典,向内传值
rou = {}
rou['num'] = 20
rou['price'] = 50
print(rou)

# 修改键值对的值
rou['price'] = rou['price'] + 50
# 获取键值[]方括号表示法
print(rou['price'])

# 删除键值对 用del语句 永久删除
del rou['price']
print(rou)

# 需要获取可能不存在的值时，建议用get()一共俩参数，1.需要返回的键名2.如果该键不存在时，返回的解释，第二个参数可不写，返回None
point_value = rou.get('points', 'no point value assigned')
print(point_value)
age_value = rou.get('age')
print(age_value)

# 遍历字典
for key in rou.keys():
    print(key)

for value in rou.values():
    print(value)
# 遍历字典，查看某键是否在该字典中
if 'value' not in rou.keys():
    print("value not in rou' key")

# 按照特定序列返回字典中的键 正序
for key in sorted(ailin.keys()):
    print(key)
# 倒序
for key in sorted(ailin.keys(), reverse=True):
    print(key)
