# input()的工作原理：让程序暂停等待用户输入，获取输入的值后Python将其赋给一个变量 按回车结束输入
message = input("Tell me something, and i will repeat it back to you: ")
print(message)
# input()输入的是字符串 用int()获取输入的数字
age = input("please input your age: ")
age = int(age)
if age >= 18:
    print('your age is larger than 18')
