from collections import Counter

"""
统计字符串的中各个字符的个数，并按照字典的个数输出
"""
s = 'aaabbbbdbbbcccc'
c1 = Counter(s)
print(dict(c1))
