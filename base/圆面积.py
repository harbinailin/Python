import math

r = int(input("请输入圆的半径"))
print("半径为{:d}的圆的面积是{:.2f}".format(r, math.pi * r ** 2))
print("半径为{0}的圆的面积是{1}".format(r, math.pi * r ** 2))