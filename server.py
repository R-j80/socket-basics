import socket


server = socket.socket()   #created socket
print("socket created")

server.bind(('127.0.0.1' ,8099))  #binding the socket with port number

server.listen(3)
print("waiting for connections")

while True:
    conn, addr = server.accept()   #it will give client's socket and addr
    print(addr," ")
    print('connected')
    conn.send(bytes('Hello client', 'utf-8'))
    rec = conn.recv(1024).decode()
    print(rec)

    conn.close()
