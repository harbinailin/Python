import socket

s = socket.socket()
print("发送端创建成功")
s.bind(('localhost', 8998))
s.listen(3)

print("等待连接")
# s.settimeout(15.0)
c, addr = s.accept()
print("ip地址和端口号", addr)
ack_expected = "1"
ack = "0"

while True:

    frame = input("输入要发送的信息")

    c.send(bytes(frame, 'utf-8'))
    while ack_expected != ack:
        try:
            c.settimeout(10.0)
            ack = c.recv(1024).decode()  # received acknowledgement from receiver

            while ack_expected != ack:  # if ack expected doesnt match with received one then resend frame
                print(frame, "ack值不正确，验证失败，信息重新发送!")
                c.send(bytes(frame, 'utf-8'))
                ack = c.recv(1024).decode()
        except socket.timeout:  # in case of time 76out again resend the frame

            while ack_expected != ack:
                print(frame, "超时10s，信息将重新发送!!")
                break

    # asking user if wants to close the connection
    print("验证通过，信息成功传输")
    stop_connection = input("输入'yes'以关闭连接,输入'no'以继续传输数据")
    if stop_connection == "yes":
        print("连接已关闭")
        c.close()
        s.close()
        break
    if ack_expected == "0":
        ack_expected = "1"
    else:
        ack_expected = "0"
