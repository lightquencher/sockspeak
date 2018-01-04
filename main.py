#!/usr/bin/python2

import socket
import threading
import lqsock
import os

# The function for the sending thread
def send_thread(sock_used):
    data = raw_input("> ")
    sock_used.send(data)
    if data == "sockquit":
        sock_used.quit()
        quit()

# The function for the recieving thread
def recv_thread(sock_used):
    data = str(sock_used.listen())
    if data == "sockquit":
        sock_used.quit()
        quit()
    else:
        data = 'espeak "' + data + '"'
    os.system(data)

# Main
def main():
    global mainsock
    mainsock = lqsock.Sock("your-ip", "target-ip", 3083) # Change "your-ip" & "target-ip"
    mainsock.create()
    mainsock.try_conn()

    # Connected, and ready to send/recieve

    s_t = threading.Thread(target=send_thread, args=(mainsock,))
    r_t = threading.Thread(target=recv_thread, args=(mainsock,))

    s_t.start()
    r_t.start()

    s_t.join()
    r_t.join()

# Run this until keyboard interrupt
try:
    main()
except KeyboardInterrupt as msg:
    mainsock.send("sockquit")
    mainsock.quit()
    print "Done!"
