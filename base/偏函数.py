# 偏函数通过设置参数的默认值，降低函数调用的难度
# 比如int()默认是将字符串转化为十进制数，可以通过设置base=2,8,16改变转换成的进制数
# 当函数的参数数量太多，需要简化时，可以借助functools.partial创建一个新函数，这个新的函数可以固定柱原函数的部分参数，从而使得函数调用更加方便
from functools import partial

print(int('123456', base=8))
int2 = partial(int, base=2)
print(int2('1001001'))
int3 = partial(int, base=8)
print(int3('2372'))
