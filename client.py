import  sys
import  socket
buf_size=1024
server_adress=('192.168.149.128',8888)
try:
    client=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
except:
    print('create socket failed')
    sys.exit()
client.connect(server_adress)
while True:
    data=input('please input message:')
    if not data:
        print('please input again')
        continue
    client.sendall(data.encode('utf-8'))
    data1=client.recv(buf_size)
    print(data1)
client.close()