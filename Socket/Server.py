# encoding=utf8   
import socket
phone=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
phone.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
phone.bind(('127.0.0.1',8080))
print("Starting run.....")
phone.listen(5)
while True:
    coon,client_addr=phone.accept()
    print(coon,client_addr)
    while True:
        try:
            data=coon.recv(1024)
            print('client data 收到消息:%s',data.decode('utf8'))
        except Exception:
            break
    coon.close()