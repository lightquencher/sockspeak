#!/usr/bin/python2

import socket

# For controlling sockets
class Sock():
    def __init__(self, host, t_host, port):
        self.host = host
        self.t_host = t_host
        self.port = port
        self.role = ''
        self.quiet = 1
    def __call__(self):
        return self.role + " to " + self.host + ":" + str(self.port)
    def if_quiet(self, x, y):
        if self.quiet == 0:
            pass
        elif self.quiet == 1:
            print(x)
        elif self.quiet == 2:
            if y != "x":
                print(y)
            else:
                print(x)
        else:
            print("Sock.quiet error: Sock.quiet set to " + str(self.quiet) )
    # Create socket
    def create(self):
        self.if_quiet("Socket create", "x")
        try:
            self.s = socket.socket()
        except Exception as msg:
            self.if_quiet("Error at Sock.create()", ("Sock.create(): " + str(msg)))
    # Binding socket
    def bind(self):
        try:
            self.if_quiet("Socket binding", ("Binding to: " + self.host + ":" + str(self.port)))
            self.s.bind((self.host, self.port))
            self.s.listen(5)
            self.if_quiet("Socket bound", ("Bound to: " + self.host + ":" + str(self.port)))
        except Exception as msg:
            self.if_quiet("Error at Sock.bind()", ("Sock.bind(): " + str(msg)))
    # Accepting client
    def accept(self):
        try:
            self.if_quiet("Waiting for acception...", "x")
            self.conn, self.address = self.s.accept()
            self.if_quiet("Connection recieved", ("Connection from: " + self.address[0]))
            self.role = "server"
        except Exception as msg:
            self.if_quiet("Error at Sock.accept()", ("Sock.accept(): " + str(msg)))
    # Connecting to server
    def connect(self):
        try:
            self.if_quiet("Trying to connect...", ("Connecting to: " + self.t_host, str(self.port)))
            self.s.connect((self.t_host, self.port))
            self.if_quiet("Connected", ("Connected to: " + self.t_host, str(self.port)))
            self.role = "client"
        except Exception as msg:
            self.if_quiet("Error at Sock.connect()", ("Sock.connect(): " + str(msg)))
    def try_conn(self):
        try:
            try:
                self.if_quiet("Trying to connect...", ("Connecting to: " + self.t_host, str(self.port)))
                self.s.connect((self.t_host, self.port))
                self.if_quiet("Connected", ("Connected to: " + self.t_host, str(self.port)))
                self.role = "client"
            except:
                self.if_quiet("Socket binding", ("Binding to: " + self.host + ":" + str(self.port)))
                self.s.bind((self.host, self.port))
                self.s.listen(5)
                self.if_quiet("Socket bound", ("Bound to: " + self.host + ":" + str(self.port)))
                self.if_quiet("Waiting for acception...", "x")
                self.conn, self.address = self.s.accept()
                self.if_quiet("Connection recieved", ("Connection from: " + self.address[0]))
                self.role = "server"
        except Exception as msg:
            print("Try connection error: " + str(msg))
    # Authentication and encryption for later
    def auth(self, key):
        pass
    # Sending message, tries both to server and to client
    def send(self, x):
        if self.role == "client":
            self.s.send((x).encode())
        elif self.role == "server":
            self.conn.send(x.encode())
        else:
            print("Send error: role invalid")
    # Listens for message, tries both server and client
    def listen(self):
        if self.role == "client":
            return self.s.recv(2048)
        elif self.role == "server":
            return self.conn.recv(2048)
        else:
            print("Listen error: role invalid")
    def quit(self):
        if self.role == "client":
            self.s.close()
        elif self.role == "server":
            self.conn.close()
            self.s.close()
        else:
            print("Quit error: role invalid")

def first(j, x):
	i = 0
	y = ""
	try:
		while i != j:
			y += list(x)[i]
			i += 1
		return y
	except:
		print "Error: multisock: first"

def last(j, x):
	k = len(x)
	i = k - j
	y = ""
	try:
		while i != k:
			y += list(x)[i]
			i += 1
		return y
	except:
		print "Error: multisock: last"

def not_first(i, x):
	y = ""
	j = len(x)
	try:
		while i != j:
			y += list(x)[i]
			i += 1
		return y
	except:
		print "Error: multisock: not_first"

def not_last(i, x):
	y = ""
	j = len(x) - i
	k = 0
	try:
		while k != j:
			y += list(x)[k]
			k += 1
		return y
	except:
		print "Error: multisock: not_last"

def not_first_last(ix, iy, x):
    try:
        return not_last(iy, not_first(ix, x))
    except:
        print "Error: multisock: not_first_last"
