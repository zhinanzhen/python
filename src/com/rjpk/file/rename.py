'''
Created on 2016年11月19日

@author: Administrator
'''
import os

def rename(filePath):
    pathDir = os.listdir(filePath);
    a=0;
    for filename in pathDir:
        oldDir = os.path.join(filePath,filename)
        if os.path.isdir(oldDir):
            rename(oldDir);
            continue;
        a = a+1;
        oldSuffix = os.path.splitext(filename)[1];
        newName = str(a) + oldSuffix;
        newDir = os.path.join(filePath,newName);
        os.renames(oldDir, newDir);
   
if __name__ == '__main__':
    filePath = "C:\\Users\\Administrator\\Desktop\\py"
    rename(filePath);
