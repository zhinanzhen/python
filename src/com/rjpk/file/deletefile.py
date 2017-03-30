'''
Created on 2016年11月18日

@author: Administrator
'''
import os

def deletefile(filePath):
    pathDir = os.listdir(filePath);
    for filename in pathDir:
        oldDir = os.path.join(filePath,filename)
        if os.path.isdir(oldDir):
            deletefile(oldDir);
            continue;
        name = os.path.splitext(filename)[0];
        if name.find("svn") >= 0:
            os.remove(oldDir);
  
if __name__ == '__main__':
    filePath = "C:\\Users\\Administrator\\Desktop\\py"
    deletefile(filePath);
