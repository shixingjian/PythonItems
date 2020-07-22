print(type(100))

print(1/3)

a = 5
b = 4

print(a%b)
# /表示除法，\表示转义或换行
print(' hello \n'*3)
info = 'abcdef'
print(info[0])
print(info[1:3])
print(info[:3])
print(info[3:])
print(info[::1])
print(info[::-1])
alist = [10,20,30,20,50,20]
while 20 in alist:
    alist.remove(20)
print(alist)

print('{:09.2f}{{}}'.format(1234.567890))
print('{:#6x}'.format(108))#十六进制加前缀0x
name = 'tom'
age = 18
# info = f'我叫:{name:*>6},我的年龄:{age:*>6},我自己的{{}}'
info = f'我叫:{0:*>6},我的年龄:{1:*>6},我自己的{{}}'.format(name,age)
print(info)

#冒泡排序
blist = [9,2,0,3]
for i in range(0,len(blist)-1):
    for j in range(0,len(blist)-1-i):
        if blist[j] > blist[j+1]:
            blist[j],blist[j+1] = blist[j+1],blist[j]
print(blist)
dlist = 'ab c d'
info = ''.join(dlist.split())#删除任意和所有空白
info[:-3]#删除字符串后三位
#print(''.join(dlist.split())[:-3].upper())

clist = 'abcd'
print(type(clist.split('c')[1]))
import sys
#sys.path.append('f:\\')
print(sys.path)
import shixingjian
shixingjian.func()


