import  socket
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
#create connection
s.connect(('192.168.149.128',9999))
#accept information
print(s.recv(1024).decode('utf-8'))
for data in [b'Michael',b'Tracy',b'Sarah']:
    #send data
    s.send(data)
    print(s.recv(1024).decode('utf-8'))
s.send(b'exit')
s.close()