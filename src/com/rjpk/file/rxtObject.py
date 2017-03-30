'''
Created on 2016年12月29日

@author: Administrator
'''
import os

project=("zftWeb","rxtOrgLoan","rxtSchedule",
         "rxtWebService","cfcaWeb","rxtApp",
         "rxtCnceServer","sanyLoan","sysConfigService","wsEtl");
         
def rename(filePath,runObj):
    pathDir = os.listdir(filePath);
    for filename in pathDir:
        objName = os.path.splitext(filename)[0];
#       全部生成xml2结尾的
        oldDir = os.path.join(filePath,filename)
        for objIndex in runObj:
            if objName==project[objIndex]:
                newDir = os.path.join(filePath,objName+".xml");
                os.renames(oldDir, newDir);
                continue;
                
def renameAll(filePath):
    pathDir = os.listdir(filePath);
    for filename in pathDir:
        objName = os.path.splitext(filename)[0];
        oldDir = os.path.join(filePath,filename)
        newDir = os.path.join(filePath,objName+".xml2");
        os.renames(oldDir, newDir);

if __name__ == '__main__':
    filePath = "E:\\development\\tomcat\\apache-tomcat-7.0.42\\conf\\Catalina\\localhost"
    renameAll(filePath);
    runObject = [1];
    rename(filePath,runObject);
    print("over");

