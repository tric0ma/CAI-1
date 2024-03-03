import socket
import hashlib
import calcular_mac
import random

HOST = "127.0.0.1"  # The server's hostname or IP address
PORT = 3030  # The port used by the server
KEY = bytes("98374509837459", "utf-8") # Secret key shared with client
MENSAJE = "23234 2342 200" # The client account or message
NONCE = random.randint(100000, 999999) # Number Once to avoid replay attacks

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    mac = calcular_mac.calcular_mac(MENSAJE, KEY, NONCE)
    # Enviar mensaje y MAC al servidor
    s.sendall(f"{MENSAJE}|{NONCE}|{mac}".encode())
    data = s.recv(1024)

print(f"Received {data!r}")