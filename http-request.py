import socket
host = 'data.pr4e.org'
port = 80
myScokt = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
myScokt.connect((host, port)); 
cmd = f'GET http://{host}/romeo.txt HTTP/1.0\n\n'.encode()
#GET http://data.pr4e.org/romeo.txt HTTP/1.0
myScokt.send(cmd)
while True:
    data = myScokt.recv(512)
    if(len(data) < 1): #EOF
        break
    print(data.decode())
    myScokt.close()