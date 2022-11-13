#!usr/bin/python
import subprocess
import socket

print("Enter your Ngrok token")
token = input()
ngrok_start = subprocess.run("./ngrok config add-authtoken", "token")
s = socket.socket()
host = input()
port = int(input())
s.bind((host, port))

s.listen(5)
while True:
    c, addr = s.accept()
    print("Got connection from", addr, c.send("Thank you for connecting"))
    ngrok_start
