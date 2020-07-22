#coding=utf8
# auther:shixingjian  time:2020/07/05
import rsa
str = 'shixingjian'
(pubkey,privkey)=rsa.newkeys(1024)#实例化加密对象
#公钥加密
pwd = rsa.encrypt(str.encode(),pubkey)
print("rsa加密后的结果为",pwd.hex())
#私钥解密
depwd = rsa.decrypt(pwd,privkey)
print("解密后的结果为",depwd.decode('utf8'))