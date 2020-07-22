#coding=utf8
# auther:shixingjian  time:2020/06/30
import socket
#创建socket对象
sk = socket.socket()
#发起连接
sk.connect(('127.0.0.1',1234))
while True:
    send_date = input('>>>')
    #发送数据
    sk.sendall(send_date.encode('utf8'))
    if send_date == 'bye':
        break
    #接收消息
    server_data = sk.recv(1024).decode('utf8')
    print('服务端：',server_data)
#释放资源
sk.close()