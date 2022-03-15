# while循环不断运行，直到不满足指定条件为止。for循环用于针对集合内部所有的元素，当每个元素都执行后才结束运行。
# current_number = 1
# while current_number <= 5:
#     print(current_number)
#     current_number += 1
#
# prompt = "\n tell me something, and i will repeated it back to you: "
# prompt += "\n Enter 'quit' to end the program"
# message = ""
# while message != 'quit':
#     message = input(prompt)
#     if message != 'quit':
#         print(message)

# # 更简洁的写法 设置标志
# prompt = "\n tell me something, and i will repeated it back to you: "
# prompt += "\n Enter 'quit' to end the program"
# active = True
# while active:
#     message = input(prompt)
#     if message == 'quit':
#         active = False
#     else:
#         print(message)

# break 使用break退出循环
# prompt = "\n tell me something, and i will repeated it back to you: "
# prompt += "\n Enter 'quit' to end the program"
# while True:
#     message = input(prompt)
#     if message == 'quit':
#         break
#     else:
#         print(message)

# 在循环中使用continue 打印1-10的奇数
current_number = 0
while current_number < 10:
    current_number += 1
    if current_number % 2 == 0:
        continue
    print(current_number)
