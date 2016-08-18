# 3 cron_ctrl

标签（空格分隔）： 360-ops

---

##问题描述
在一些环境中我们会用到crontab来做定时任务，但是有些情况下我们会暂时的关闭某个定时任务。
能不能有这样一个操作界面方便的操作这些任务：
./cron_ctrl jobname1 --stop ;./cron_ctrl jobname1 --start;./cron_ctrl jobname1 --list;
编写一个工具来实现它。

##答：
详见脚本```cron_crtl```



