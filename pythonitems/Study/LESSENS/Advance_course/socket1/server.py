#coding=utf8
# auther:shixingjian  time:2020/06/30
import socket
#配置服务器的ip地址和端口号
ip = ('127.0.0.1',1234)
#创建socket对象
sk = socket.socket()
#绑定IP地址和端口号
sk.bind(ip)
#监听有没有请求过来
sk.listen()
print('服务端启动了')
#等待传入连接
#等到连接传入后，会返回一个新的套接字对象和客户端地址
while True:
    conn,addr = sk.accept()
    print('客户端地ip地址：',addr)
    while True:
        #接收消息
        client_data = conn.recv(1024).decode('utf8')
        print('客户端：',client_data)
        if client_data == 'bye':
            conn.close()
            break
        #发送数据
        send_data = input('>>>')
        conn.sendall(send_data.encode('utf8'))
#释放资源
# conn.close()
sk.close()
