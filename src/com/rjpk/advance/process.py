'''
Created on 2017年3月8日

@author: Administrator
'''
import multiprocessing

def hello(name):
    '''say hello'''
    print('hello %s'%name)
    return

if __name__=='__main__':
    p1=multiprocessing.process(target=hello,args=('joy',))
    p1.start()