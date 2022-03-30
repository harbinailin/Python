import socket

# 创建socket对象
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# 获取本地主机名
host = socket.gethostname()
# 设置端口
port = 9999
# 连接服务，指定主机的端口
s.connect((host, port))
# 接收小于1024字节的数据
message = s.recv(1024)
s.close()
print(message.decode('utf-8'))
