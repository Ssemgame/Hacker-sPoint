import socket

s = socket.socket()
host = input()
port = int(input())

s.connect((host, port))
print s.recv(1024)
s.close()
