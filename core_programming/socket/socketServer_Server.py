#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from socketserver import (TCPServer as TCP ,StreamRequestHandler as SRH)
from time import ctime
HOST = ''
PORT =5000
ADDR = (HOST,PORT)

class MyRequestHandle(SRH):
    def handle(self):
        print('...connect from: ' , self.client_address)
        self.wfile.write(self.rfile.readline())
        self.wfile.write('aaaaaaa')


tcsServer = TCP(ADDR,MyRequestHandle)
print('... wait connect ')
tcsServer.serve_forever()