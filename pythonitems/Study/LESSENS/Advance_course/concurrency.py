# auther:shixingjian  time:2020/06/29
#coding=utf8
import threading
import time
# def foo(somethiong,num):
#     for i in range(num):
#         print(somethiong)
#         time.sleep(5)
# t1 = threading.Thread(target=foo,args = ['看电影',3])
# t2 = threading.Thread(target=foo,args = ['听音乐',5])
# t1.start()
# t2.start()


# ----------线程处理io（输入、输出）密集型任务（有大量等待时间）----------
#io任务：数据库查询，等待结果；请求接口，等待返回；需要大量等待时间
# begin_time = time.time()
# def foo(something):
#     print(something)
#     time.sleep(2)
# # foo("看电影") #串行运行用了4.001161575317383
# # foo("听音乐")
#创建线程实例
# t1 = threading.Thread(target=foo,args=['看电影'])
# t2 = threading.Thread(target=foo,args=['听音乐'])
#启动线程
# t1.start()
# t2.start()
# #阻塞住主线程，并发耗时2.001303195953369
# t1.join()#t1运行完成前阻止主线程运行
# t2.join()#t2运行完成前阻止主线程运行
# end_time = time.time()
# print(end_time-begin_time)


# ----------线程处理计算密集型任务(永远串行的)----------

# def foo():
#     num = 0
#     for i in range(10000000):
#         num += 1
#
# begin_time = time.time()
'''
#----------串行时间：1.9423577785491943------------
foo()
foo()
'''
#----------并行时间：1.9173603057861328--------
#全局解释器锁（GIL）：无论有多少CPU，cpython同一时间只允许一个线程进入CPU
# t1 = threading.Thread(target=foo)
# t2 = threading.Thread(target=foo)
# t1.start()
# t2.start()
# t1.join()
# t2.join()
#
# end_time = time.time()
# print(end_time-begin_time)

#-------------------守护线程--------------------
# #默认：主线程运行结束后，想要退出进程，当有子线程存在，要等到子线程运行结束后主线程才会退出进程
# alist = []
# def foo():
#     while True:
#         time.sleep(1)
#         alist.append(1)
#         print('生产一个数据')
# t1 = threading.Thread(target=foo)
# t2 = threading.Thread(target=foo)
# #设置守护线程必须在start之前设置
# #起作用是主线程在运行结束后，不需要等待子线程运行结束，可直接退出
# #只对设置了子线程的线程生效
#
# t1.setDaemon(True)
# t1.start()
# t2.start()
# for i in range(3):
#     if alist:
#         alist.remove(1)
#         print('消费一个数据')
#     time.sleep(1)
# print('主线程运行结束')

# #-------------------不安全的并发------------------------
# r = threading.Lock()#声明一把锁
# '''
# 这把锁是同步锁，同步锁必须上锁与解锁相对，否则会产生bug
# 如果上锁之后不解锁，再次上锁，代码会阻塞
# 若果解锁之后，没有锁的时候进行解锁，代码会报错
# '''
#
# balance = 500#银行卡账户余额
# #操作账户余额
# def foo(num):
#     global balance#在局部作用域引用全局变量不用声明，但修改全局变量要声明
#     r.acquire()#上锁
#     account_balance = balance#将变量存到系统
#     time.sleep(1)#防止代码太少，CPU执行过快，t1，t2变成串行
#     account_balance = account_balance + num#操作后结果
#     balance = account_balance#将结果传递回去
#     r.release()#解锁
#
# t1 = threading.Thread(target=foo,args=[-300])#消费300
# t2 = threading.Thread(target=foo,args=[10000])#收入10000
# t1.start()
# t2.start()
# t1.join()
# t2.join()
# print(balance)

#---------------死锁-------------------
lockA = threading.Lock()#面试官的锁
lockB = threading.Lock()#小明的锁
#面试官
def foo1():
    lockA.acquire()
    print("请解锁死锁")
    time.sleep(1)
    lockB.acquire()
    print('"发offer"')
    time.sleep(1)
    lockA.release()
    lockB.release()
# 小明
def foo2():
    lockB.acquire()
    print('请发offer')
    time.sleep(1)
    lockA.acquire()
    print('解锁死锁')
    time.sleep(1)
    lockB.release()
    lockA.release()

t1 = threading.Thread(target=foo1)
# t2 = threading.Thread(target=foo2)
t1.start()
# t2.start()

#--------------------------递归锁-------------------------
# Rlock = threading.RLock()#小明的锁
# '''
# 递归锁内部维护着一把锁和一个计数器
# 每次上锁计数器加一
# 每次解锁计数器减一
# 计数器可以大于零，可以等于零，但不能小于零
# '''
# def foo1():
#     Rlock.acquire()
#     print("请解锁死锁")
#     time.sleep(1)
#     Rlock.acquire()
#     print('"请发offer"')
#     time.sleep(1)
#     Rlock.release()
#     Rlock.release()
# # 小明
# def foo2():
#     Rlock.acquire()
#     print('请发offer')
#     time.sleep(1)
#     Rlock.acquire()
#     print('解锁死锁')
#     time.sleep(1)
#     Rlock.release()
#     Rlock.release()
#
# t1 = threading.Thread(target=foo1)
# t2 = threading.Thread(target=foo2)
# t1.start()
# t2.start()