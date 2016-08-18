# 5 socks_proxy

---

##问题描述
假设您有一个远端服务器可以通过ssh登录，在你的本地电脑上实现一个简单的socks代理服务，可以在断网或重启的情况下重新建立连接。（提示：ssh tunnel）

##答
设远端服务器的ip为1.2.3.4，本机端口16077，利用ssh的-D参数实现socks代理，socks_proxy.sh
```
ssh -Nf -D 16077 1.2.3.4
```
添加执行权限
```chmod +x socks_proxy.sh```

CentOS下,将执行脚本的语句 ```. /home/cyf/devops/socks_proxy.sh```加入到脚本文件```/etc/rc.local```和```/etc/sysconfig/network-scripts/ifup```，以实现在断网或重启情况下重新建立连接





