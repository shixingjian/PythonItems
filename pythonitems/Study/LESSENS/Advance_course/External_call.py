# auther:shixingjian  time:2020/06/29
# ------程序外部调用----------
#---------方法一：
import os
# os.system('ipconfig')#相当于打开操作系统的shell，输入命令操作

# os.system('cmd.exe')#阻塞式调用，执行后该行程序后的代码不会执行，退出才执行
# print('after')

# result = os.system('ipconfig')
# print(result)#返回0，执行成功，返回1，执行失败

#-------方法二：
# import subprocess
#执行一个命令，并将结果以一个字节字符串的形式返回
#阻塞式调用
# out = subprocess.check_output('mspaint')
# # out = subprocess.check_output('ipconfig')
# # print(out.decode('gbk'))
# # print('after')

from subprocess import Popen,PIPE

# out = Popen('mspaint')
# #提供等待功能
# out.wait()
# print(out)

#输出重定向
# child = Popen(
#     'ipconfig',
#     stdout=PIPE,
#     encoding='gbk'
# )
# output,err = child.communicate()
# print(output,err)

#输入重定向
child = Popen(
    'python iotest.py',
    # stdout=PIPE,
    stdin=PIPE,
    # stderr=PIPE,
    encoding='gbk'
)
output,err = child.communicate('\n'.join(['1','2']))
print(output,err)