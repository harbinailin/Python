import socket

c = socket.socket()
print("接收端创建成功")

c.connect(('localhost', 8998))

rec_message = "end msg"
while True:
    received_message = c.recv(1024).decode()
    print(f"传输信息是：{received_message}, 信息发送成功")
    print("等待验证。。。。。")
    if received_message != rec_message:
        ack = input("输入ack值: ")
        c.send(bytes(ack, 'utf-8'))

