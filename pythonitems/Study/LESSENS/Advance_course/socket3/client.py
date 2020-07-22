#coding=utf8
# auther:shixingjian  time:2020/06/30
import socket
sk = socket.socket()
sk.connect(('127.0.0.1',1200))
print('客户端启动')
while  True:
    send_data = input('>>>')
    sk.sendall(send_data.encode('utf8'))
    if send_data == 'exit':
        break
    server_data = sk.recv(1024)
    print(server_data.decode('utf8'))
sk.close()