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
copytruncate
nocreate
dateext
}
```
ͨ��crontab����ÿ��23:59��ִ��һ��
```
59 23 * * * /usr/sbin/logrotate -f /etc/logrotate.d/apache
```



