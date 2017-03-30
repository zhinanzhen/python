'''
Created on 2016年11月19日

@author: Administrator
'''
import os
import re

def replacefile(filePath):
    for filename in os.listdir(filePath):
        oldDir = os.path.join(filePath,filename)
        if os.path.isdir(oldDir):
            replacefile(oldDir);
            continue;
        replace(oldDir);

def replace(path):
    with open(path,"r") as r:
        lines = r.readlines();
        with open(path,"w") as w:
            for i in lines:
                regex = re.compile('\stable=*\s');
                if regex.search(i):
                    print(re.subn(regex,"123rrr",i)[0])
                    w.write(re.subn(regex,"123rrr",i)[0]);
#                     w.write(i.replace("xuxiangnan","徐向南你好"));
                else:
                    w.write(i);
def test():
    r1 = re.compile('world');
    if r1.match('world'):
        print('match success');
    else:
        print('not match success')
        
    if r1.search('helloworld'):
        print('yes');
    else:
        print('no');
        
    input1 = 'hello  abc world'
    output = re.subn('abc',"123",input1)
    print(output[0])
    
    print("=============================================")
    
    abc = 'df table fd ';
#     abc = '<class name="com.rksd.dzsp.acct.po.DzspAgent" table="T_DZSP_AGENT" dynamic-insert="true" dynamic-update="true">';
    regex = re.compile('\btable\b')
    print(re.subn(regex,"r",abc)[0])
        
if __name__ == '__main__':
    filePath = "C:\\Users\\Administrator\\Desktop\\py"
#     replacefile(filePath);
    test();
