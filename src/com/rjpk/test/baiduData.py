'''
Created on 2016年10月11日

@author: Administrator
'''
import urllib.request

url = "http://www.baidu.com"
data = urllib.request.urlopen(url).read()
data = data.decode('utf-8')
print(data)