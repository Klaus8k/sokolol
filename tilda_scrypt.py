import socket
import requests

host = ('37.230.141.81', 50000)

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
    sock.bind(host)
    sock.listen()

    conn, addr = sock.accept()
    with conn:
        print(f'connections by {addr}')
        while True:
            data = conn.recv(1024)
            if not data:
                break
            conn.sendall(data)

