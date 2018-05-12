# 简单的屏幕直播

'''
原理：
后台不停截图和存图。
后台开启服务器不停监听。
当前端请求时，就把图片传过去。
因为有两个“死循环”，所以需要用线程控制，进行一定的阻塞。
'''

from PIL import ImageGrab
import socket
import time
import threading

# 捕获屏幕
def capture(delay):
    while True:
        img = ImageGrab.grab()
        img.save('1.png')
        time.sleep(delay)

threading._start_new_thread(capture, (1,)) # 时间的单位是秒，不是毫秒
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print(socket.gethostname())
server.bind(('127.0.0.1', 5000))
server.listen(100)

while True:
    socketclient, addr = server.accept()
    request = socketclient.recv(1024)
    print(request)
    # res = 'http/1.1 200 ok \n\n<h1>hello world!</h1>'
    res = 'http/1.1 200 ok \nContent-type:image/png\n\n'
    socketclient.sendall(res.encode('utf-8'))
    file = open('1.png', 'rb')
    socketclient.sendall(file.read())
    socketclient.close()