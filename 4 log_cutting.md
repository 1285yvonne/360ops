# 4 log_cutting


##����������
��־�и������һ��access.logÿ�������������־��ʵ��һ����־�и�Ĺ��ܣ���˵����ʵ�ַ�ʽ����ʲôȱ�ݡ�


----------


##��
����```logrotate```�ָ������־����Apache����־�ļ�Ϊ��
��Ŀ¼```/etc/logrotate.d```�½��������ļ�```apache```���������£�
```
/usr/local/apache2.4/logs/access_log
{
notifempty
daily
error root
rotate 1
create 0644 root root
olddir /home/cyf/logs #��ת�����ļ�����Ŀ¼/home/cyf/logs
postrotate
#��ת������־�ļ�����Ϊ�����յĸ�ʽ�磺2016.Aug.18
mv /home/cyf/logs/access_log.1 /home/cyf/logs/$(date +"%y-%m-%d")
endscript
}
```
ͨ��crontab����ÿ��23:59��ִ��һ��
```
59 23 * * * /usr/sbin/logrotate -f /etc/logrotate.d/apache
```



