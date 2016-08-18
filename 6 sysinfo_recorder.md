# 6 sysinfo_recorder

---

##问题描述
写一个本地服务，定时的搜集系统的cpu使用情况并记录下来。
需要考虑到cpu的使用情况包括哪项信息，用什么方式存储数据（记录文件的大小不能一直增长，记录的数据易于展示）。

##答：
利用```vmstat```来定时搜集系统的cpu使用情况，包括信息如下：
```shell
us：用户进程执行时间百分比（user time）
sy：内核系统进程执行时间百分比（system time）
wa：IO等待时间百分比
id：空闲时间百分比
```
每30秒搜集系统的cpu使用情况，每天的情况记录在以当天日期为文件名的日志文件中；详见脚本文件```sysinfo_recorder.sh```
使用```nohup sh sysinfo_recorder.sh &```后台一直运行脚本


