# import uuid
# print(uuid.uuid4())
import time
# ti1=[1,2,3]
# ti2=[4,5,6]
# ti3=[[0,4,9],[1,5,5],[6,9,9]]
# ti4=[7,8,9]
# for i,j in zip(ti1,ti2):
#     print(i,j)
# print(list(enumerate(ti2)))

# for i,one in enumerate(ti2):
#     print(i,one)
# try:
#     for i,j,q in ti3:
#         print(i,j,q)
# except Exception as err:
#     print(err)

# print(time.strftime('%Y-%m-%d',time.localtime(time.time()+60*60*24)))#计算当前时间后一天时间
class A:
    x = 10
    def __init__(self):
        a = 1
    @classmethod
    def foo(cls):
        print(cls.x)

A.x = 5
A().foo()
