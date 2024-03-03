import socket
import hashlib
import calcular_mac

HOST = "127.0.0.1"  # Standard loopback interface address (localhost)
PORT = 3030  # Port to listen on (non-privileged ports are > 1023)

KEY = bytes("98374509837459", "utf-8")



with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    conn, addr = s.accept()
    with conn:
        print(f"Connected by {addr}")
        while True:
            data = conn.recv(1024)
            if not data:
                break
            mensaje = data.decode().split("|")[0]
            nonce_recibido = data.decode().split("|")[1]
            mac_recibido = data.decode().split("|")[2]

            mac_calculado = calcular_mac.calcular_mac(mensaje, KEY, nonce_recibido)

            print("KEY -------------> ",KEY)
            print("MENSAJE ---------> ",mensaje)
            print("NONCE -----------> ",nonce_recibido)
            print("MAC CALCULATED --> ",mac_calculado)
            print("MAC RECEIVED ----> ",mac_recibido)


            if mac_calculado == mac_recibido:
                print("Mensaje recibido con éxito\n")
            else:
                print("Error de integridad en el mensaje recibido\n")

            conn.sendall(data)
