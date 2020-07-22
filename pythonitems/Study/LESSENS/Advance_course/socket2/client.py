#coding=utf8
# auther:shixingjian  time:2020/06/30
import socket
import os
sk = socket.socket()
#连接服务器
sk.connect(('127.0.0.1',1234))

def post_file(sk_obj,file_path):
  '''
  发送文件
  :param sk_obj:
  :param file_path:
  :return:
  '''
  #发送文件大小
  file_size = os.stat(file_path).st_size  #int
  sk_obj.sendall(str(file_size).encode('utf8'))
  sk_obj.recv(1024)#避免粘包，就是由于网络延迟原因，一个数据包没接收完，另一个包也发过去了，导致两个包粘在一起了
  #发送文件名称
  file_name = os.path.split(file_path)[1]
  sk_obj.sendall(file_name.encode('utf8'))
  sk_obj.recv(1024)#避免粘包
  #发送文件内容
  with open(file_path,'rb') as f:
      while file_size > 0:
          sk_obj.sendall(f.read(1024))
          file_size = file_size - 1024
post_file(sk,r'F:\pycharm\project\Study\File\photo.jpg')
#释放资源
sk.close()
