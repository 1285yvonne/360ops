# 4 log_cutting

---

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
create 0644 root root #新建空的日志文件
olddir /home/cyf/logs #将转储的文件存在目录/home/cyf/logs
postrotate
#将转储的日志文件名改为年月日的格式如：2016.Aug.18
mv /home/cyf/logs/access_log.1 /home/cyf/logs/$(date | awk '{OFS=".";print $6 OFS $2 OFS $3}')
endscript
}
```
通过crontab程序每天23:59分执行一次
```
59 23 * * * /usr/sbin/logrotate -f /etc/logrotate.d/apache
```
缺陷：这种方法假设日志文件中的记录日期都是同一天，无法处理日志中存在不同天数的情况


