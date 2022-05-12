# 绝对素数：素数的数字位置经过对换后还是素数。 输出所有的两位绝对素数。
def isPrime(num: int):
    """
    判断素数
    :param num:判断素数函数的参数
    :return: True or False
    """
    if num == 1:
        return False
    # 用n%i==0就不是素数 i的取值范围是2到n-1
    for i in range(2, num):
        if num % i == 0:
            return False
    return True


def reverse(num: int):
    """
    将整数逆序
    :param num: 逆序函数的参数
    :return: renum 逆序之后的参数
    """
    renum = 0
    while num:
        last = num % 10
        renum = renum * 10 + last
        num //= 10
    return renum


list = []
# 设置一个空的列表用于存储绝对素数
for i in range(10, 100):  # 根据题目两位绝对素数 范围是10-99
    if isPrime(i):
        if isPrime(reverse(i)):
            list.append(i)

print("满足条件的绝对素数有：")
for p in list:
    print(p, end="  ")
print(f"\n绝对素数的个数是{len(list)}")
