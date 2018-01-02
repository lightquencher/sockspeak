#!/usr/bin/python2

import socket

# For controlling sockets
class Sock():
    def __init__(self, host, t_host, port):
        self.host = host
        self.t_host = t_host
        self.port = port
        self.role = ''
    # Create socket
    def create(self):
        print("Socket create")
        try:
            self.s = socket.socket()
        except Exception as msg:
            print("Error: " + str(msg))
    # Binding socket
    def bind(self):
        try:
            self.s.bind((self.host, self.port))
            self.s.listen(5)
            print("Socket bound")
        except Exception as msg:
            print("Binding error: " + str(msg))
    # Accepting client
    def accept(self):
        try:
            self.conn, self.address = self.s.accept()
            print("Connection from: " + self.address[0])
        except Exception as msg:
            print("Accept error: " + str(msg))
    # Connecting to server
    def connect(self):
        try:
            self.s.connect((self.t_host, self.port))
            print("Connected to: " + self.t_host)
        except Exception as msg:
            print("Connecting error: " + str(msg))
    def try_conn(self):
        try:
            try:
                print("Attempting to connect to server")
                self.s.connect((self.t_host, self.port))
                print("Connected to: " + self.t_host)
                self.role = "client"
            except:
                print("Attempting to create server")
                self.s.bind((self.host, self.port))
                self.s.listen(5)
                print("Socket bound")
                self.conn, self.address = self.s.accept()
                print("Connection from: " + self.address[0])
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
