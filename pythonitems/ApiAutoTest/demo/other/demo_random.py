#coding=utf8
# auther:shixingjian  time:2020/07/03
import random
import time
#1.random
print(random.random())#随机小数
print(random.randint(1000,10000))#随机整数

#2.time
print('大学英语'+str(int(time.time()*1000)))
print('182'+str(int(time.time()*1000))[5:])
