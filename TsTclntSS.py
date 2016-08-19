# -*- coding: utf-8 -*-
__author__ = 'dell'

from socket import *

HOST = '119.29.151.142'
PROT = 16077
BUFSIZ = 4096
ADDR = (HOST, PROT)


def receive(obj, size):
    result = ''
    while size > 0:
        stream_data = obj.recv(BUFSIZ)
        size -= BUFSIZ
        result += stream_data
    return result


tcpCliSocket = socket(AF_INET, SOCK_STREAM)
tcpCliSocket.connect(ADDR)

while True:
    data = raw_input('> ')
    if not data:
        continue
    tcpCliSocket.sendall(data)
    receive_size = tcpCliSocket.recv(BUFSIZ)
    try:
        size = int(receive_size)
    except ValueError, e:
        print e.message
        continue
    result = receive(tcpCliSocket, size)
    if not result:
        continue
    print result

tcpCliSocket.close()
