# dict2 = {'a':[12,23],'b':13}
# #dict2.clear()
# list = dict2['a']
# print(list)
# tuple1=(1,2,3,4,5)
# tuple1=tuple1[:1]+(0,)+tuple1[1:]
# print(tuple1)

# fireDir = 'f:\\51job.txt'
# fireDir1 = 'd:\\shixingjian.txt'
#
# with open(fireDir) as fo1 ,open(fireDir1) as fo2:
#     fo1.read()
#     fo2.read()

# def getName(srcStr):
#     alist = srcStr.split(',')
#     Name = alist[1].split(' ')[-1]
#     return Name
#
# srcStr = '-----,the name is mary,---------;'
# print(getName(srcStr))
# file3Dir = ('d:\\file3.txt')
# fo3 = open(file3Dir,'at')
# fo3.write('abcd')
# fo3.flush()
# fo3.close()
# import math
# print(math.ceil(5/3))#向上取整
# print(math.floor(5/3))#向下取整
# print(round(5/3))#四舍五入
# print(5//3)#取整数部分
# print(5%3)#取小数部分，1余数为2
# print(10**2)#10的2次方


# slist = [1,2,3]
# print(slist.remove(5))


# def insert_date(start,end):
#     sql1 = "insert into sq_course(name,`desc`,display_idx) values"
#     sql2 = ''
#     for i in range(start,end+1):
#         if i == end:
#             sql2 += f'("课程{i}","课程{i}的描述","1");'
#         else:
#             sql2 += f'("课程{i}","课程{i}的描述","1"),\n'
#     return sql1 + sql2
# print(insert_date(1,4))

# print(ord("你"))
# print(chr(20320))
#
# a = 'abc'
# b = b'abc'
# print(a.encode('gbk'))
# print(b)
# import os
# print(os.path.basename(r'F:\pycharm\project\Study\File\photo.jpg'))
# str = 'abcdefg'
# #截取下标为零的元素a
# print(str[0:1])
# #截取下标为0和1的元素a，b
# print(str[0:2])
# #截取下标为-1和-2的元素g，f
# print(str[-2:-1])
# #截取下标为0-5，步长为2的元素
# print(str[0:5:2])
# #截取字符串前段
# print(str[:2])
# #截取字符串后段
# print(str[-3:])
# #字符串正序
# print(str[::1])
# #字符串反序
# print(str[::-1])
# #split()切割
# print(str.split('cd'))

# list1 = [20,5.33,'pass',[10,20]]
# #1- 列表获取元素----下标获取
# print(list1[-1][-1])#--->20
# #2- 10不在列表里
# print(10 in list1[-1])#--->True

#3- 修改值
# list1 = [20,5.33,'pass',[10,20]]
# list1[0] = 100
# print(list1) #--->[100, 5.33, 'pass', [10, 20]]

#4- 增加元素
# #append()在列表尾部增加元素
# list1 = [20,5.33,'pass',[10,20]]
# list1[-1].append(30)
# print(list1)#----->[20, 5.33, 'pass', [10, 20, 30]]
# #insert  插入(你需要插入的下标，值)
# list1.insert(100,[10,20])#如果insert插入的下标大于len()和append一样的结果
# print(list1)#----->[20, 5.33, 'pass', [10, 20, 30], [10, 20]]

#4- 删除
# list1 = [20,5.33,'pass',[10,20]]
# del list1[1],list1[2]
# print(list1)#---->[20, 'pass']
#
# list1 = [20,5.33,'pass',[10,20]]
# del list1[1:3]
# print(list1)#---->[20, [10, 20]]
#
# list1 = [20,5.33,'pass',[10,20]]
# del list1[::2]
# print(list1)#---->[5.33, [10, 20]]

#2- pop  有返回值为被删元素值
# list1 = [20,5.33,'pass',[10,20]]
# ret = list1.pop(1)
# print(ret)#---->5.33


#remove--三种最慢一个,一次只能删一个元素
# list1 = [20,5.33,'pass',[10,20]]
# list1.remove(5.33)#直接删值-----值不清楚在什么位置--得去匹配删除
# print(list1)#---->[20, 'pass', [10, 20]]
# #如果这个不存在，remove会报错
# #只要这个元素在，我就一直删，如果元素已经不在，不能删
# list1 = [20,5.33,'pass',[10,20],10,10,10]
# while 10 in list1:
#     list1.remove(10)
# print(list1)#----->[20, 5.33, 'pass', [10, 20]]

# #清空列表
# list1 = [20,5.33,'pass',[10,20]]
# list1.clear()
# print(list1)#----->[]

#5- 合并
# list1 = [20,5.33,'pass',[10,20]]
# #临时合并
# print(list1+[5,6])#----->[20, 5.33, 'pass', [10, 20], 5, 6]不改变源对象,新对象临时存在新地址
# print(list1)#------>[20, 5.33, 'pass', [10, 20]]

#列表扩展--在原有地址进行扩展
# list1 = [20,5.33,'pass',[10,20]]
# list1.extend([20,20])
# print(list1)#------->[20, 5.33, 'pass', [10, 20], 20, 20]

# tu = (10,20,30,40)
# print(tu[1:3])#---->(20, 30)

# import requests
# r = requests.get("http://www.baidu.com")
# r.encoding = 'utf8'
# print(r.text)
















