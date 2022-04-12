import socket  # Importing socket library of python by which we connect server and client

c = socket.socket()  # creating socket object for receiver
print("接收端创建成功")

c.connect(('localhost', 8998))  # connecting to server on port number 8998

rec_message = "starting msg"
while True:
    received_message = c.recv(1024).decode()
    print(received_message, "信息接收成功")
    if received_message != rec_message:
        ack = input("输入ack值: ")
        c.send(bytes(ack, 'utf-8'))

