'''
Created on 2016年10月26日

@author: Administrator
'''
# count = 0
# while(count < 10):
#     count += 1
#     if(count%2 == 0):
#         continue
#     print(count)

# bs = [3,4,5]
# for b in bs:
#     print(b)
#     
# print("for by index")
# for i in range(len(bs)):
#     print(bs[i])

# for num in range(10,20):
#     for i in range(2,num):
#         if num%i == 0:
#             j=num/i
#             print ('%d 等于  %d * %d' %(num ,i ,j))
#             break
#     else:
#         print(num,'是一个质数')
        
i=2
while (i < 100):
    i += 1
    j = 2
    while(j < i):
        if i%j == 0 :
            k=i/j
            print('%d 等于  %d * %d' %(i ,k ,j))
            break
        j += 1
    else:
        print(i,'是一个质数')
        
     
     
     
     
     
     
     
     