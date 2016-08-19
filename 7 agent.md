# 7 agent

---

##问题描述
实现一个被控程序，连接对应的端口便可以对被控端输送命令。
这是一个可以重复调用的服务，不能把bash的io直接绑到tcp上。命令运行完后命令的输出应该能返回到控制机的STDOUT。（考察tcp，多线程等）

##答
被控端：利用Python的SocketServer模块实现多线程TCP服务器，利用subprocess和shlex模块实现命令的执行
控制端：利用socket模块实现数据的发送和接收，
代码详见agent.py\TsTclintSS.py



