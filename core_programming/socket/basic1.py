#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import socket
#from socket import *
from time import ctime

HOST = ''
PORT = 6000
BUFFSIZE = 1024
ADDR = (HOST, PORT)

TcpSerSock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
TcpSerSock.bind(ADDR)
TcpSerSock.listen(5)


while True:
    print("waiting for connecting ......")
    TcpClientSock, addr = TcpSerSock.accept()
    print('...connect from:', addr)

    while True:
        data = TcpClientSock.recv(BUFFSIZE)
        if not data:
            break
        TcpClientSock.send(b'%s' % data)

    TcpClientSock.close()
TcpSerSock.close()
