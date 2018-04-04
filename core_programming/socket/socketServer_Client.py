#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from socket import *

HOST = 'localhost'
PORT = 5000
BUFFERSIZE = 1024
ADDR = (HOST, PORT)

while True:
    tcpCliSock = socket(AF_INET, SOCK_STREAM)
    tcpCliSock.connect(ADDR)
    data = input('>>> ')
    if not data:
        break
    tcpCliSock.send(b'%s' % data.encode('utf-8') )
    data = tcpCliSock.recv(BUFFERSIZE)
    if not data:
        break
    print(data)   
    tcpCliSock.close()
