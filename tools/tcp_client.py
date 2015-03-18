#!/bin/env python3

from socket import *

HOST = '192.168.2.100'
PORT = 8001
BUFSIZ = 1024
ADDR = (HOST, PORT)

tcpClientSock = socket(AF_INET, SOCK_STREAM)
tcpClientSock.connect(ADDR)

while True:
  data = input('> ')
  if not data:
    break
  tcpClientSock.send(bytes(data, 'utf-8'))
  """
  data = tcpClientSock.recv(BUFSIZ)
  if not data:
    break
  print(str(data, encoding='utf-8'))
  """

tcpClientSock.close()

