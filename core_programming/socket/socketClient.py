#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import socket
from time import ctime

HOST = '192.168.41.12'
PORT = 6000
BUFFSIZE = 1024
ADDR = (HOST,PORT)

TcpCliSock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
TcpCliSock.connect(ADDR)

while True:
    data = input('> ')
    if not data:
        break
    TcpCliSock.send(b'%s' % bytes(data,'utf-8'))
    data1 = TcpCliSock.recv(BUFFSIZE)
    if not data1:
        break
    print(data1)
TcpCliSock.close()