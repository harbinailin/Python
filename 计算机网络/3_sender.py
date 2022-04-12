import _thread
import time
from queue import *
import socket
import random

IPSender = "127.0.0.1"
PORTSender = 5006  # Im the sender, this is my port

IPReceiver = "127.0.0.1"
PORTReceiver = 5007


class UDP_Socket:
    def __init__(self, IPSender, PORTSender, IPReceiver, PORTReceiver):
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)  # UDP
        self.socket.bind((IPSender, PORTSender))
        self.IPReceiver = IPReceiver
        self.PORTReceiver = PORTReceiver

    def send_msg(self, msg, IPReceiver, PORTReceiver):

        dpp = random.randint(1, 10)  # duplicate packet probability
        plrp = random.randint(1, 10)  # packet loss rate probability
        if plrp > 2:
            print('The message was sent once')
            self.socket.sendto(msg.encode(), (IPReceiver, PORTReceiver))
            if dpp == 1:
                print('The message was sent twice')
                self.socket.sendto(msg.encode(), (IPReceiver, PORTReceiver))
        return

    def listen_msg(self, queue):
        while True:
            data, addr = self.socket.recvfrom(1024)  # buffer size is 1024 bytes
            queue.put(data.decode())


class Stop_and_wait:
    def __init__(self, IPSender, PORTSender, IPReceiver, PORTReceiver, seq_num):
        self.UDP_layer = UDP_Socket(IPSender, PORTSender, IPReceiver, PORTReceiver)
        self.seq_num = seq_num
        self.rcv_msg = Queue()

    def stop_wait_sender(self, msg):

        acknoledgment = False
        try:
            _thread.start_new_thread(self.UDP_layer.listen_msg, (self.rcv_msg,))
        except:
            print('error creating thread')
            return None
        attached_seq_msg = self.seq_num + "||" + msg
        print(attached_seq_msg)

        self.UDP_layer.send_msg(attached_seq_msg, IPReceiver, PORTReceiver)
        start = time.time()

        while not acknoledgment:
            if time.time() - start > 1:
                self.UDP_layer.send_msg(attached_seq_msg, IPReceiver, PORTReceiver)
                print("Sent the message again")
                start = time.time()

            try:
                ack_message = self.rcv_msg.get_nowait()  # If there is no message it will trow Empty exception
                split_message = ack_message.split('||')

                if split_message[0] == "1":
                    self.seq_num = "1"
                else:
                    self.seq_num = "0"

                acknoledgment = True
            except:
                pass
        return ack_message


s_and_w = Stop_and_wait(IPSender, PORTSender, IPReceiver, PORTReceiver, "1")

print("UDP target IP: " + IPReceiver + ". UDP target port: " + str(PORTReceiver))
while True:
    msg = input("What message you want to send? ")

    ack_message = s_and_w.stop_wait_sender(msg)
    print(ack_message + "\n")
