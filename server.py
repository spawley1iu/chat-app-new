import socket

HOST = '127.0.0.1'  # localhost
PORT = 65432        # arbitrary non-privileged port

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((HOST, PORT))
server_socket.listen()

print(f"Server listening on {HOST}:{PORT}...")
conn, addr = server_socket.accept()
print(f"Connected by {addr}")

conn.sendall(b"Hello, Client!")
conn.close()
