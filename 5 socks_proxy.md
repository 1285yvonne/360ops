# 5 socks_proxy

---

##��������
��������һ��Զ�˷���������ͨ��ssh��¼������ı��ص�����ʵ��һ���򵥵�socks������񣬿����ڶ�������������������½������ӡ�����ʾ��ssh tunnel��

##��
��Զ�˷�������ipΪ1.2.3.4�������˿�16077������ssh��-D����ʵ��socks����socks_proxy.sh
```
ssh -Nf -D 16077 1.2.3.4
```
���ִ��Ȩ��
```chmod +x socks_proxy.sh```

CentOS��,��ִ�нű������ ```. /home/cyf/devops/socks_proxy.sh```���뵽�ű��ļ�```/etc/rc.local```��```/etc/sysconfig/network-scripts/ifup```����ʵ���ڶ�����������������½�������





