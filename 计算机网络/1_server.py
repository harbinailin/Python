import socket

# 创建socket对象
serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# 获取本地主机名
host = socket.gethostname()
port = 9999
# 绑定端口
serversocket.bind((host, port))
# 设置最大连接数，超过后排队
serversocket.listen(5)
while True:
    # 建立客户端连接
    clientsocket, addr = serversocket.accept()
    print("连接地址: %s" % str(addr))
    message = 'offer多多,美团快手捞捞我' + "\r\n"
    clientsocket.send(message.encode('utf-8'))
    clientsocket.close()

# socket 套接字
# 应用程序通过socket向网络发出请求或应答网络请求，使主机间或一台计算机上的进程间可以通信。
# 实验一实现计算机上两个进程进行通信

# 使用socket函数创建套接字

# 每一个socke对象都有accept bind(address) close connect(address) send shutdown(0receiver1sender2all)
# 创建socket对象，使用bind指定port端口，调用accept等待客户端连接并返回connection对象，表示已连接到客户端
# 导入socket模块
