import socket
import calcular_mac
import secrets

HOST = "127.0.0.1"  # The server's hostname or IP address
PORT = 3030  # The port used by the server
KEY = bytes("98374509837459", "utf-8") # Secret key shared with client
MENSAJE = "23234 2342 200" # The client account or message
NONCE = secrets.token_urlsafe() # Number Once to avoid replay attacks
nonces = set()
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    mac = calcular_mac.calcular_mac(MENSAJE, KEY, NONCE)
    # Enviar mensaje, nonce y resumen MAC al servidor
    s.sendall(f"{MENSAJE}|{NONCE}|{mac}".encode())
    data = s.recv(1024)
    nonce_recibido = data.split("|")[1]
    with open("nonces_client_bd.txt", "r") as f:
        for line in f:
            nonces.add(line.strip())

            with open("nonces_client_bd.txt", "a") as f:
    
                if nonce_recibido not in nonces:
            
                    f.write(str(nonce_recibido))
                    f.write("\n")
                else:
                    print("NONCE REPETIDO - FALLO")
                    break
print(f"Received {data!r}")