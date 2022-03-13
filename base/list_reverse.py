# 列表反转reverse() 永久改变，但是可以通过再次调用reverse()将列表恢复到原来的顺序
language = ['ruby', 'c', 'python', 'java', 'html']
print(language)
language.reverse()# 倒序
print(language)
language.reverse()# 原序
print(language)