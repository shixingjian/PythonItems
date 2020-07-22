#coding=utf8
# auther:shixingjian  time:2020/06/30
import socketserver
class MyServer(socketserver.BaseRequestHandler):
    def handle(self):
        print('消息来了...')
        while  True:
            #接收数据
            client_data = self.request.recv(1024).decode('utf8') #相当于conn.rev()
            print(client_data)
            #退出判断
            if client_data == 'exit':
                break
            #处理并发送数据
            server_data = input('>>>')
            self.request.sendall(server_data.encode('utf8'))

server = socketserver.ThreadingTCPServer(('127.0.0.1',1200),MyServer)
print("服务器启动...")
server.serve_forever()#启动服务，24小时运行
