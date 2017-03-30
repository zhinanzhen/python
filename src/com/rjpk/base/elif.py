'''
Created on 2017年3月7日

@author: Administrator
'''
#from pip._vendor.distlib.compat import raw_input;
#a = int(raw_input("请输入一个整数\n"));
a = int(input("请输入一个整数\n"));
if a >= 90:
    print("优秀");
elif a >= 80:
    print("良");
elif a >= 70:
    print("中");
else:
    print("差");