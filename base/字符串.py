a = "i love Python"
print(a[0])
print(a[-1])
print(a[2:5])
print(a[:6])
print(a[4:])
b = a.upper()
print(b)
c = a.title()
print(c)
d = b.lower()
print(d)
# 修改字符串 不可以直接修改
d = d[:7] + 'P' + d[8:]
print(d)
a = "今天晚饭花了%.1f元"
b = 15.6
c = a % b
print(c)
a = "今天%s每斤%d元"
b = ("草莓", 35)
c = a % b
print(c)
print(a % b)
a = "今年GDP比去年上涨了%.2f%%"
b = 12.3333
print(a % b)
