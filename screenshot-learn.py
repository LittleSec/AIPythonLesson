# python截图学习

from PIL import ImageGrab

# 最简单的截图
# img = ImageGrab.grab()
# img.save('1.png') # 存在当前工作根目录

# socket学习
import socket

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server.bind(('127.0.0.1', 5050)) # 绑定，参数是个元组，包含主机地址和端口号等。
server.listen(10) # 监听，最大链接数量是100

while True:
    socketclient, addr = server.accept() # 链接客户端，答应请求
    print(1)
    res = b"""HTTP/1.1 200 OK
    <html><body>hello</body></html>
    """
    print(2)
    socketclient.sendall(res) # 客户端发送消息
    print(3)
    socketclient.close()