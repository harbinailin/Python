str = "Hello,Python"
suffix = "Python"
print(str.endswith(suffix, 2))
# endswith 是判断字符串是否以suffix结尾 start end 返回True False
dicts = {'one': 1, 'two': 2, 'three': 3}
print(dicts['one'])
print(dicts['four'])
# py3 访问不存在的索引或key：
#    字典：key访问报KeyError，get访问默认返回None
#    列表、元组、字符串：IndexError

# py3 切片越界(索引为自然数情况)：
#    列表：
#       start越界：返回[] 空列表
#       end越界：返回原列表浅拷贝
#       start、end均越界：[] 空列表
#    元组：
#       start越界：返回() 空元组
#       end越界：返回原元组
#       start、end均越界：() 空元组
#    字符串：
#       start越界：返回'' 空字符
#       end越界：返回原字符串
#       start、end均越界：'' 空字符
