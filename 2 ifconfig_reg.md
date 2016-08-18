# 2 ifconfig_reg

标签（空格分隔）： 360-ops

---

##问题描述
解析ifconfig命令的标准输出，返回一个hash。key是网卡名称 value是对应的ip。

##答：
我喜欢将awk命令写进script中调用：由于题目中说需要返回一个hash，我设了一个数组变量用来存放结果，详见2.awk

然后调用脚本：

```
ifconfig | awk -f 2.awk
输出结果：
name: docker0 ip:172.17.0.1
name: eth0 ip:10.104.32.39
name: lo ip:127.0.0.1
```




