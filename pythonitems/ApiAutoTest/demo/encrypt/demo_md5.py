#coding=utf8
# auther:shixingjian  time:2020/07/05
import hashlib
pwd = 'shixingjian'
md5 = hashlib.md5()
md5.update(pwd.encode('utf-8'))
print('md5加密后的结果为：',md5.hexdigest())