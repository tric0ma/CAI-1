# -*- coding: utf-8 -*-

import socket
import calcular_mac
import secrets
import sys

# Obtener los argumentos de la línea de comandos
argumentos = sys.argv

# Verificar si se proporcionó al menos un argumento
if len(argumentos) > 1:
    variable = argumentos[1]
else:
    variable = input("Por favor, proporciona un caso a probar de entre Interceptar, Nonce o Exito: ")


def prueba_cliente(tipo_prueba):
    
    HOST = "127.0.0.1"  # The server's hostname or IP address
    PORT = 3030  # The port used by the server
    KEY = bytes("98374509837459", "utf-8") # Secret key shared with client
    MENSAJE = "23234 2342 200" # The client account or message
    NONCE = str(secrets.token_urlsafe()) # Number Once to avoid replay attacks
    nonces = set()
    
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((HOST, PORT))
        mac = calcular_mac.calcular_mac(MENSAJE, KEY, NONCE)
        # Enviar mensaje, nonce y resumen MAC al servidor
        if tipo_prueba == 'Interceptar':
            MENSAJE = "23234 2342 2000" 
            s.sendall(f"{MENSAJE}|{NONCE}|{mac}".encode())
            
        elif tipo_prueba == 'Nonce':
            NONCE='8izaoT4RwpVSstqE1_XBuqV6tNemFkuardBgO0gHzZw'
            s.sendall(f"{MENSAJE}|{NONCE}|{mac}".encode())
            
        else:
             s.sendall(f"{MENSAJE}|{NONCE}|{mac}".encode())
             
             
        data = s.recv(1024)
        mensaje = data.decode().split("|")[0]
        nonce_recibido = data.decode().split("|")[1]
        mac_recibido = data.decode().split("|")[2]
        mac_calculado = calcular_mac.calcular_mac(mensaje, KEY, nonce_recibido)
        with open("nonces_client_bd.txt", "r") as f:
            for line in f:
                nonces.add(line.strip())

        with open("nonces_client_bd.txt", "a") as f:
        
            if nonce_recibido not in nonces:
                
                f.write(str(nonce_recibido))
                f.write("\n")
                        
                if mac_calculado == mac_recibido and NONCE==mensaje.split("!")[1]:
                    print("RESPUESTA ---------> ",mensaje.split("!")[0])
                    print("NONCE -----------> ",nonce_recibido)
                    print("MAC CALCULATED --> ",mac_calculado)
                    print("MAC RECEIVED ----> ",mac_recibido)
                    print("Mensaje recibido\n")
                else:
                    print("Error de integridad en el mensaje recibido\n")
                            
            else:
                print("NONCE REPETIDO - FALLO")
        
if __name__ == '__main__':
    prueba_cliente(variable)

 
