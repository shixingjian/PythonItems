# #1.获取学生信息
# str = input('请输入学生信息：')
# #2.提取每个学生的姓名和年龄
# str1 = ''.join(str.split())[:-1] #删除任意空格和最后分号
# alist = str1.split(';')
# for one in alist:
#     temp = one.split(',') #name,age = one,split(',')
#     name = temp[0]
#     age = int(temp[len(temp)-1])
# #3.排版输出
#     print(f'{name:<20}:{age:0>2};')


#1.获取学生信息
str = input('请输入学生信息：')
#2.提取每个学生的姓名和年龄
alist = str.split(';') #以分号切割------list
del alist[-1]
for one in alist:
    temp = one.split(',') #name,age = one,split(',')
    name = temp[0].strip()
    age = int(temp[len(temp)-1].strip())
#3.排版输出
    print('{:<20}:{:0>2};'.format(name,age))
