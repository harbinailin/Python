from queue import *
import _thread
import socket
import random

IPSender = "127.0.0.1"
PORTSender = 5006

IPReceiver = "127.0.0.1"
PORTReceiver = 5007  # Im the receiver, this is my port


class UDP_Socket:
    def __init__(self, IPSender, PORTSender, IPReceiver, PORTReceiver):
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)  # UDP
        try:
            self.socket.bind((IPReceiver, PORTReceiver))
        except Exception as error:
            print(error)
        self.IPSender = IPSender
        self.PORTSender = PORTSender

    def send_msg(self, msg, IPSender, PORTSender):

        dpp = random.randint(1, 10)  # duplicate packet probability
        plrp = random.randint(1, 10)  # packet loss rate probability
        print('The message was sent once')
        if plrp > 2:
            self.socket.sendto(msg.encode(), (IPSender, PORTSender))
            if dpp == 1:
                print('The message was sent twice')
                self.socket.sendto(msg.encode(), (IPSender, PORTSender))
        return

    def listen_msg(self, queue):
        data, addr = self.socket.recvfrom(1024)  # buffer size is 1024 bytes
        queue.put(data.decode())


class Stop_And_Wait:
    def __init__(self, IPSender, PORTSender, IPReceiver, PORTReceiver, seq_num):
        self.UDP_layer = UDP_Socket(IPSender, PORTSender, IPReceiver, PORTReceiver)
        self.seq_num = seq_num
        self.rcv_msg = Queue()

    def change_seq_num(self, value):
        self.seq_num = value

    def stop_wait_receiver(self):
        print('Waiting for a message')

        try:
            _thread.start_new_thread(self.UDP_layer.listen_msg, (self.rcv_msg,))
        except:
            print('error creating thread')
            return None

        while True:
            try:
                msg = self.rcv_msg.get()  # If there is no message it will trow Empty exception
                print(msg)
                split_message = msg.split('||')
                seq_number_received = split_message[0]
                print("Seq number received = " + seq_number_received + " Seq number stored = " + self.seq_num)

                if seq_number_received == self.seq_num:  # If its repeated msg is discarded
                    print("This message is repeated")
                    if seq_number_received == "1":
                        ack = "0" + "||Repeated. Discarded"
                        self.UDP_layer.send_msg(ack, IPSender, PORTSender)

                    else:
                        ack = "1" + "||Repeated. Discarded"
                        self.UDP_layer.send_msg(ack, IPSender, PORTSender)
                else:
                    if seq_number_received == "1":
                        ack = self.seq_num + "||Received."
                        self.UDP_layer.send_msg(ack, IPSender, PORTSender)
                        self.change_seq_num("1")
                    else:
                        ack = self.seq_num + "||Received."
                        self.UDP_layer.send_msg(ack, IPSender, PORTSender)
                        self.change_seq_num("0")

                print("ACK: " + ack + "\n")
            except:
                pass


s_and_w = Stop_And_Wait(IPSender, PORTSender, IPReceiver, PORTReceiver, "0")
s_and_w.stop_wait_receiver()
