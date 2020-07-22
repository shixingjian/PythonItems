#coding=utf8
# auther:shixingjian  time:2020/06/30
import socket
sk = socket.socket()
#绑定IP地址和端口号
sk.bind(('0.0.0.0',1234))
#监听
sk.listen()
print('服务端启动了')

def get_file(sk_obj):
    '''
    接收文件函数
    :param sk_obj:
    :return:
    '''
    #接收文件大小
    file_size = int(sk_obj.recv(1024).decode('utf8'))
    sk_obj.sendall(b'ok')
    #接收文件名称
    file_name = sk_obj.recv(1024).decode('utf8')
    sk_obj.sendall(b'ok')
    #接收文件内容
    with open('./%s' %file_name,'wb') as f:
        while file_size > 0:
            f.write(sk_obj.recv(1024))
            file_size = file_size - 1024
#等待客户端连接
conn,addr = sk.accept()
print('客户端地址：',addr)
get_file(conn)
conn.close()
sk.close()