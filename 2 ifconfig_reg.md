# 2 ifconfig_reg

---

##��������
����ifconfig����ı�׼���������һ��hash��key���������� value�Ƕ�Ӧ��ip��

##��
��ϲ����awk����д��script�е��ã�������Ŀ��˵��Ҫ����һ��hash��������һ���������������Ž�������2.awk

Ȼ����ýű���

```
ifconfig | awk -f 2.awk
��������
name: docker0 ip:172.17.0.1
name: eth0 ip:10.104.32.39
name: lo ip:127.0.0.1
```




