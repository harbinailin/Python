# strip()删除前后的空白 lstrip()删除左部空白 rstrip()删除尾部空白
message_1 = ' python'
print(message_1)
# 永久删除
message_1 = message_1.lstrip()
print(message_1)
message_2 = 'python '
print(message_2)
message_2=message_2.rstrip()
print(message_2)
message_3 = ' python '
print(message_3)
# 暂时删除
print(message_3.strip())
print(message_3)
message_3=message_3.strip()
print(message_3)
