# 不可变的列表称为元组 tuple 元组用圆括号来标识() 在元组定义后，就可以用索引来访问其他元素，就像访问列表元素一样
# 不可试图更改元组内元素的值，但可以整个元组重新赋值
demensions = (20, 50)
for demension in demensions:
    print(demension)
print(demensions[0])
print(demensions[1])
# demensions[0]=250 报错，元组元素不可单个赋值
demensions = (100, 500)
print(demensions)

a = (1, 2)
b = ('a', 'b')
print(a + b)
a = (1, 2, 3)
print(a[1:-1])
