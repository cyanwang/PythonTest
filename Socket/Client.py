# encoding=utf8   
import socket
phone=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
phone.connect(('127.0.0.1',8080))
while True:
    msg=input('>>:').strip()
    if not msg:continue
    phone.send(msg.encode('utf8'))
    data=phone.recv(1024)
    print('server back res 服务端返回结果：>>%s',data)