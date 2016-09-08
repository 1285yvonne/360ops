# 4 log_cutting


##问题描述：
日志切割，有这样一个access.log每天会打出大量的日志。实现一个日志切割的功能，并说明该实现方式会有什么缺陷。


----------


##答：
利用```logrotate```分割管理日志，以Apache的日志文件为例
在目录```/etc/logrotate.d```下建立配置文件```apache```，内容如下：
```
/usr/local/apache2.4/logs/access_log
{
notifempty
daily
error root
rotate 1
copytruncate
nocreate
dateext
}
```
通过crontab程序每天23:59分执行一次
```
59 23 * * * /usr/sbin/logrotate -f /etc/logrotate.d/apache
```



