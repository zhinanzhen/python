'''
Created on 2017年3月7日

@author: Administrator
'''
try:
    print(1/0)
except ZeroDivisionError as err:
    print('22222 {0}'.format(err));
except BaseException:
    print('');
except:
    print('');
    
    