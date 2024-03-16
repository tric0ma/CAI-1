########## IMPORTS ###################################################
import hashlib #Librería para trabajar con hashes
from Crypto.Cipher import AES #Cifrado AES
from Crypto.Random import get_random_bytes # Librería para obtener los bytes del padding o relleno
import time #Librería para calcular tiempos
######################################################################

# Función para generar la clave de cifrado, la cual recibe una contraseña y salt
# y aplica SHA256 para combiar estos y generar la clave
def generar_clave(password, salt):
    password = password.encode()
    return hashlib.sha256(password + salt).digest()

# FUNCION PARA CIFRAR IMAGEN CON PADDING
def cifrar_imagen_con_relleno(imagen, clave, ruta_salida):
    # Abrir la imagen en modo binario
    with open(imagen, "rb") as f:
        imagen_bytes = f.read()

    # Calcular el tamaño del relleno necesario
    padding_size = (-len(imagen_bytes)) % 16

    # Generar bytes aleatorios para el relleno
    padding = get_random_bytes(padding_size)

    # Añadir el relleno a los datos
    imagen_bytes += padding

    # Crear un objeto de cifrado AES-256-ECB
    cipher = AES.new(clave, AES.MODE_ECB)

    # Codificar/cifrar la imagen
    imagen_cifrada = cipher.encrypt(imagen_bytes)

    # Guardar la imagen cifrada
    with open(ruta_salida, "wb") as f:
        f.write(imagen_cifrada)

# FUNCION PARA DESCIFRAR IMAGEN
def descifrar_imagen(imagen_cifrada, clave, ruta_salida):
    # Abrir la imagen cifrada en modo binario
    with open(imagen_cifrada, "rb") as f:
        imagen_cifrada_bytes = f.read()

    # Crear un objeto de descifrado AES-256-ECB
    cipher = AES.new(clave, AES.MODE_ECB)

    # Descodificar la imagen
    imagen_descifrada = cipher.decrypt(imagen_cifrada_bytes)

    # Guardar la imagen descifrada
    with open(ruta_salida, "wb") as f:
        f.write(imagen_descifrada)

# FUNCION PARA GENERAR HASH DE UNA IMAGEN
def generar_hash(imagen):
    # Abrir la imagen en modo binario
    with open(imagen, "rb") as f:
        imagen_bytes = f.read()

        # Calcular el hash SHA256
        hash_imagen = hashlib.sha256(imagen_bytes).digest()

    return hash_imagen

# MAIN #
if __name__ == '__main__':
    # Inicio del contador de tiempo del script
    inicio = time.time()
    # Imagen de pruebam en este caso una radiografía en formato JPG
    imagen = "pulmones_radiografia_web.jpg"
    # Establecemos una contraseña de ejemplo
    password = "una_contraseña_segura_y_larga"
    # Establecemos salt de ejemplo para añadir a contraseña y generar clave
    salt = b"una_sal_aleatoria"
    # Llamada al método generador de la clave
    clave = generar_clave(password, salt)
    # Nombre del archivo con la imagen cifrada
    imagen_cifrada = "imagen_cifrada.jpg"
    # Nombre del archivo con la imagen descifrada
    imagen_descifrada = "imagen_descifrada.jpg"
    # Llamada al método de cifrar la imagen junto con la clave anterior
    cifrar_imagen_con_relleno(imagen, clave, imagen_cifrada)
    # Llamada al método de descifrar la imagen junto con la clave anterior y la imagen cifrada
    descifrar_imagen(imagen_cifrada, clave, imagen_descifrada)
    # Cálculo del tiempo de ejecución del script
    fin = time.time()
    tiempo_ejecucion = fin - inicio
    print("Tiempo de ejecución:", tiempo_ejecucion, "segundos")