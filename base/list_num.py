# range(a,b)包含a但不包含b range(1,10)==1~9
for value in range(1, 10):
    print(value)

# 使用range创建数字列表
numbers = list(range(1, 10))
print(numbers)

# range()第三个参数是步长。例输出1-10内的偶数
num = list(range(2, 11, 2))
print(num)
# 打印1-10内的奇数
nums = list(range(1, 10, 2))
print(nums)

# 求1-10的乘方
squares = []
for value in range(1, 11):
    # square = value ** 2
    # squares.append(square)
    squares.append(value ** 2)
print(squares)

# 最大值、最小值、求和
digits = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(max(digits))
print(min(digits))
print(sum(digits))
