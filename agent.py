#! /usr/bin/env python

from SocketServer import (TCPServer as TCP, StreamRequestHandler as SRH, ThreadingMixIn as TMI)
from subprocess import Popen, PIPE
from shlex import split

HOST = ''
PROT = 16077
ADDR = (HOST, PROT)
BUFSIZE = 1024

class ThreadTcpServer(TMI, TCP):
    pass

class MyRequestHandler(SRH):
    def handle(self):
        print '......connected from:', self.client_address
        while True:
            comm = split(self.request.recv(BUFSIZE))
            print comm
            try:
                result = Popen(comm, stdout=PIPE, shell=False).stdout.readlines()
                print result
                for item in result:
                    self.request.send(str(len(item)))
                    self.request.sendall(item)
            except (OSError, ValueError):
                errorcode = "your command is wrong!please input the right command!"
                self.request.send(str(len(errorcode)))
                self.request.sendall(errorcode)
            

if __name__ == '__main__':
    tcpServ = ThreadTcpServer(ADDR, MyRequestHandler)
    print 'waiting for connection......'
    tcpServ.serve_forever()
