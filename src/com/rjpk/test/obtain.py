'''
Created on 2016年10月10日

@author: Administrator
'''
#coding=utf-8
import urllib.request
import re

def getHtml(url):
    page = urllib.request.urlopen(url)
    html = page.read()
    return html

def getImg(html):
    reg = r'src="(.+?\.jpg)"'
    imgre = re.compile(reg)
    imglist = re.findall(imgre,html)
    return imglist 

html = getHtml("http://tieba.baidu.com/p/2738151262")

print(getImg(html))
