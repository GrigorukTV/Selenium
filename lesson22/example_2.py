import socket
import json

from config import LOCALHOST, random_port

my_socket = socket.socket()

address_and_port = (LOCALHOST, random_port())
my_socket.bind(address_and_port)
print("Started socket on", address_and_port)

my_socket.listen(10)

conn, addr = my_socket.accept()

# Получаем данные из соединения
data = conn.recv(1024)
list_headers = data.split(b"\r\n")
ready_headers = {}

for i in list_headers:
    elem = i.decode('UTF-8')
    if len(elem) == 0:
        continue
    # print(elem)

    part = elem.split(': ')
    if len(part) < 2:
        continue

    ready_headers[part[0]] = part[1]

ready = json.dumps(ready_headers)

conn.send(("HTTP/1.1 200 OK\n Connection: close\n Content-Type: application/json\n\n" + ready).encode('UTF-8'))


