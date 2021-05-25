import socket

HOST = ''
PORT = 12000
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORT))
s.listen()
conn, addr = s.accept()
print('Connected by', addr)
while 1:
    data = conn.recv(4096)
    print(data.decode())
    conn.send("Hello".encode('utf-8'))
    if not data: break
    conn.sendall(data)
conn.close()