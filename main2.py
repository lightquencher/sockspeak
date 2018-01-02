#!/usr/bin/python2

import socket
import threading
import lqsock
import os

def send_thread(sock_used):
    sock_used.send(raw_input("> "))

def recv_thread(sock_used):
    data = 'espeak "' + str(sock_used.listen()) + '"'
    os.system(data)

def main():
    mainsock = lqsock.Sock("192.168.0.252", "192.168.0.83", 3083)
    mainsock.create()
    mainsock.try_conn()

    # Connected

    s_t = threading.Thread(target=send_thread, args=(mainsock,))
    r_t = threading.Thread(target=recv_thread, args=(mainsock,))

    s_t.start()
    r_t.start()

    s_t.join()
    r_t.join()

main()
