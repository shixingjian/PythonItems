# auther:shixingjian  time:2020/06/29
#coding=utf8
import time
# def foo():#被装饰函数
#     print('执行测试用例')
#     time.sleep(1)

#闭包：一个内部函数引用外部作用域（不包括全军作用域）的变量，那么函数就叫做闭包
# def func(name):
#     def inner(age):
#         print('name:',name,'age:',age)
#     return inner;
# func = func('mary')
# func(24)#func函数生命周期结束后，name依然存在，因为它被闭包引用了；所以闭包延长了了局部变量的生命周期


#-------简单装饰器------
# def show_time(func):#装饰函数
#     def inner(case_name):
#         begin_time = time.time()
#         func(case_name)#-------再次调用foo（）相当于再次调用inner（）
#         end_time = time.time()
#         print('总耗时：',end_time - begin_time)
#     return inner
# foo = show_time(foo)#---->foo = inner
# foo()

# @show_time  #@语法堂，相当于foo = show_time(foo)#---->foo = inner
# def foo(case_name):#被装饰函数------foo被装饰成foo
#     print('执行测试用例')
#     time.sleep(1)
#
# foo(1)

#------------带参函数的装饰器----------

# def show_time(func):
#     def inner(values):#修改inner的参数就行
#         start_time = time.time()
#         func(values)
#         end_time = time.time()
#         print('执行时间为',end_time-start_time)
#     return inner
#
# @show_time
# def func2(values):
#     print(values)
#     time.sleep(1)
#     print('%s,again' %values)
#     print(type(values))
# func2(3)

#----------装饰可变数量参数函数-------
# def add_show_time(func):# 带参数函数的装饰,修改inner 的参数就好了
#     def inner(*args):
#         start = time.time()
#         func(*args)
#         end = time.time()
#         print('函数执行时间为;%s' % (end - start))
#     return inner
# @add_show_time
# def add(*args):
#     amount = 0
#     for i in args:
#         amount += i
#     print(amount)
#     print(type(args))
#     time.sleep(1)
#     return amount

# add(1,2,3,4)





