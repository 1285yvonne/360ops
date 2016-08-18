# 1 password_cache

标签（空格分隔）： 360-ops

---

##问题描述：
运维操作在很多情况下需要访问不同的服务器，运维人员可能会频繁的输入自己的账号和密码。
是否可以通过一个简单方式只需要输入一遍密码，然后余下的操作都可以不再重复的输入密码。
密码应该存储在什么地方会比较隐蔽，让有这台机器sudo权限的其他人看不到。（可以不写代码，回答便可）

##答：
使用```ssh-keygen```和```ssh-copy-id```实现

 1. ```ssh-keygen -t rsa``` 在本地使用ssh-keygen产生密钥对
 2. ```ssh-copy-id -i ~/.ssh/id_rsa.pub remote-server```
    将公钥复制到远程机器中

visudo或vim /etc/sudoer修改中sudo用户的权限，使其无法进入私钥所在目录
