import socket

client = socket.socket()
name = input("enter your name: ")

client.connect(('localhost',8099))
print("req send to the server")

print(client.recv(1024).decode())
client.send(bytes(name,'utf-8'))
