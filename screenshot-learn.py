# python截图学习

from PIL import ImageGrab

# 最简单的截图
# img = ImageGrab.grab()
# img.save('1.png') # 存在当前工作根目录

# socket学习
import socket

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server.bind(('127.0.0.1', 5000)) # 绑定，参数是个元组，包含主机地址和端口号等。
server.listen(10) # 监听，最大链接数量是100

while True:
    socketclient, addr = server.accept() # 链接客户端，答应请求
    request = socketclient.recv(1024)
    print(request)
    res = 'http/1.1 200 ok \n\n<h1>hello world!</h1>'
    socketclient.sendall(res.encode('utf-8')) # 客户端发送消息
    socketclient.close()