#!/usr/bin/python2.7
import curses
import argparse
import socket
import threading
from multisock import *
import time
import os.path as op
import os
from getpass import getuser

# Argument handling
parser = argparse.ArgumentParser(description='Simple socket chat')

# Argument choices
parser.add_argument('-H', '--host', type=str, metavar='', required=True, help='Target hosts IP')
parser.add_argument('-P', '--port', type=int, metavar='', required=True, help='Target hosts Port')
parser.add_argument('-i', '--home', type=str, metavar='', required=False, help='Your IP')

# Quiet or debug
quiet_group = parser.add_mutually_exclusive_group()
quiet_group.add_argument('-q', '--quiet', action='store_true', help='print quietly')
quiet_group.add_argument('-d', '--debug', action='store_true', help='print debugging')

# Declaring args
args = parser.parse_args()

# Getting the home ip (user's ip)
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.connect(("8.8.8.8", 80))
homeip = s.getsockname()[0]
s.close()

if args.home == None:
    args.home == homeip

# Curses CLI display
screen = curses.initscr()
dims = screen.getmaxyx()
#screen.refresh()
#screen.addstr(0, 0, "Hello World!")
#screen.clear()
#screen.getch()
#curses.endwin()

# The class for managing the conversation
class Convo():
    def __init__(self):
        self.contents = ''
        self.convo_num = []
        self.filenum = 0
        self.filename = ''

    def __len__(self):
            return len(self.contents)

    def __call__(self):
        return "convo: " + str(self.filenum)

    def file(self):
        if op.isdir("~/.sockspeak"):
            # Getting the information of the sockspeak files
            os.chdir("/home/" + getuser() + "/.sockspeak")
            self.sockspeaklist = os.listdir("./")
            for x in sockspeaklist:
                if first(6, x) == 'convo_':
                    try:
                        self.conv_num.append(int(not_first_last(6, 4, x)))
                    except:
                        pass

            for x in conv_num:
                if x > self.filenum:
                    self.filenum = x

            self.filename = "convo_" + self.filenum + ".txt"
        else:
            pass
    def create(self):
        try:
            self.file_dir_name = "/home/" + getuser + "/" + filename
            self.file = open(self.file_dir_name, 'w')
        except:
            print("Error: main:Convo.create()"

def send_thread(sock_used):
    global conversation

def recv_thread(sock_used):
    global conversation

def socket_silence():
    global args
    global mainsock
    if args.quiet:
        mainsock.quiet = 0
    elif args.debug:
        mainsock.quiet = 2
    else:
        mainsock.quiet = 1

def main():
    global mainsock
    global screen
    global args
    mainsock = Sock(args.home, args.host, args.port)
    socket_silence()
    mainsock.create()
    mainsock.try_conn()
    screen.clear()
    screen.refresh()

    while True:
        try:
            u_in = screen.getch()
            if str(u_in) == '16':
                mainsock.send("Ping")
        except KeyboardInterrupt as msg:
            mainsock.quit()
            break
    mainsock.quit()

    '''
    s_t = threading.Thread(target=send_thread, args=(mainsock,))
    r_t = threading.Thread(target=recv_thread, args=(mainsock,))

    s_t.start()
    r_t.start()

    s_t.join()
    r_t.join()
    '''
try:
    print "if __name__"
    if __name__ == "__main__":
        main()
        curses.endwin()
except Exception as msg:
    print str(msg)
    mainsock.quit()
    curses.endwin()
