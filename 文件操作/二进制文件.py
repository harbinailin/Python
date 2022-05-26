import json

content = [120, 'true', 123.456]
filename = "二进制文件.json"
with open(filename, 'w') as f:
    json.dump(content, f)

with open(filename) as f:
    content = json.load(f)
print(content)

# from struct import *
#
# with open("二进制文件.txt", "wb") as f:
#     f.write(pack("i?d", 12345, 'true', 123.456))
#
# # 读取文件
# with open("二进制文件.txt", "rb") as f:
#     (a, b, c) = unpack("i?d", f.read(8 + 1 + 8))
#     print(a, b, c)
