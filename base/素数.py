from math import sqrt

num = int(input("请输入数字"))
for i in range(2, int(sqrt(num))+1):
    if num % i == 0:
        print("不是素数")
        break
else:
    print("是素数")
