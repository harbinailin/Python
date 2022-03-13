# 永久排序 sort()对列表元素排列顺序的改变是永久的
cars = ['bmw', 'audi', 'toyota', 'subaru']
print(cars)
# 按照字母顺序排序 正序abc
cars.sort()
print(cars)
# 按照字母顺序倒序 zyx 倒序reverse=True
cars.sort(reverse=True)
print(cars)

# 临时排序 sorted() 保留列表元素原来的顺序，只是以特定的排列方式展现出来
language = ['ruby', 'c', 'python', 'java', 'html']
print(language)
language_sort = sorted(language)
language_sort_1 = sorted(language, reverse=True)
print(language_sort)
print(language_sort_1)
print(language)
