#!/usr/bin/env python3
"""Raw TCP server that sends 'Gutentag, World!' to any connection.

Run: python3 server.py
Connect: nc localhost 9000
"""
import socket

HOST = ''
PORT = 9000

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server:
    server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server.bind((HOST, PORT))
    server.listen(5)
    print(f'TCP server listening on port {PORT}')
    while True:
        conn, addr = server.accept()
        with conn:
            conn.sendall(b'Gutentag, World!\n')
