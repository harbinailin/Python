import struct
a=0
b=True
c='Python'
buf=struct.pack('i?',a,b)  #字节流化，i表示整形格式，'?'表示逻辑格式
f=open('二进制1.txt','wb')
f.write(buf)
f.write(c.encode())  #c.encode()返回c编码后的字符串，是一个bytes对象
f.flush()
f.close()
f=open('二进制1.txt','rb')
text=f.read()
ret=struct.unpack('i?6s',text) #对二进制字符串解码
print(ret)
# import json
#
# content = [120, 'true', "asbchiajnk"]
# with open("二进制文件.json", 'w') as f:
#     json.dump(content, f)
#
# with open("二进制文件.json") as f:
#     content = json.load(f)
# print(content)

# from struct import *
#
# with open("二进制文件.txt", "wb") as f:
#     f.write(pack("i?d", 12345, 'true', 123.456))
#
# # 读取文件
# with open("二进制文件.txt", "rb") as f:
#     (a, b, c) = unpack("i?d", f.read(8 + 1 + 8))
#     print(a, b, c)
