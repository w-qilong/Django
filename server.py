import sys
import  socket
buf_size=1024
server_adress=('192.168.149.128',8888)
try:
    server=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
except:
    print('create socket failed')
    sys.exit()
print('socket created')
server.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
try:
    server.bind(server_adress)
except:
    print('connect failed')
    sys.exit()
print('socket bind')
server.listen(5)
while True:
    client,client_adress=server.accept()
    print('connect by :',client_adress)
    while True:
        data=client.recv(buf_size)
        print(data)
        client.sendall(data)
server.close()