'''
Created on 2016年10月26日

@author: Administrator
'''
import time
import calendar

localtime = time.localtime(time.time());
print(time.asctime(localtime));
print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
print(time.strftime("%a %b %d %H:%M:%S %Y", time.localtime()))
a = "Sat Mar 28 22:24:24 2016"
print(time.mktime(time.strptime(a,"%a %b %d %H:%M:%S %Y")))


cal = calendar.month(2016,10)
print(cal)