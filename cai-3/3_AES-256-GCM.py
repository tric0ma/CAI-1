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

# FUNCION PARA CIFRAR IMAGEN
def cifrar_imagen(imagen, clave, ruta_salida):

  # Abrir la imagen en modo binario
  with open(imagen, "rb") as f:
    imagen_bytes = f.read()

  # Generar un nonce aleatorio de 12 bytes
  nonce = get_random_bytes(12)

  # Crear un objeto de cifrado AES-256-GCM
  cipher = AES.new(clave, AES.MODE_GCM, nonce)

  # Codificar la imagen
  imagen_cifrada = cipher.encrypt(imagen_bytes)

  # Calcular el tag
  hash_imagen = hashlib.sha256(imagen_cifrada).digest()
  tag = hash_imagen[:16]

  # Guardar la imagen cifrada, el nonce y la etiqueta o tag
  with open(ruta_salida, "wb") as f:
    f.write(nonce)
    f.write(tag)
    f.write(imagen_cifrada)
    
  # PRINTS PARA COMPROBAR VALORES ANTES Y DESPUÉS DEL CIFRADO PARA CONTROLAR LA PÉRDIDA DE DATOS
  #print("TAM IMAGEN CIFRADA, "+str(len(imagen_cifrada))+ "\n")
  #print("NONCE DEL CIFRADO, "+str(nonce)+str(len(nonce))+ "\n")
  #print("TAG DEL CIFRADO, "+str(tag)+str(len(tag))+"\n")
  #print("-----------------------------------------------------")

# FUNCION PARA DESCIFRAR IMAGEN
def descifrar_imagen(imagen_cifrada, clave, ruta_salida):

  # Abrir la imagen cifrada en modo binario
  with open(imagen_cifrada, "rb") as f:
    nonce_des = f.read(12)
    tag_des = f.read(16)
    imagen_cifrada_bytes = f.read()
  
  # PRINTS PARA COMPROBAR VALORES ANTES Y DESPUÉS DEL CIFRADO PARA CONTROLAR LA PÉRDIDA DE DATOS
  #print("TAM IMAGEN DESCIFRADA, "+str(len(imagen_cifrada_bytes))+ "\n")
  #print("NONCE DEL DESCIFRADO, "+str(nonce_des)+str(len(nonce_des))+ "\n")
  #print("TAG DEL DESCIFRADO, "+str(tag_des)+str(len(tag_des))+"\n")

  # Crear un objeto de descifrado AES-256-GCM
  cipher = AES.new(clave, AES.MODE_GCM, nonce_des)

  # Descodificar la imagen
  try:
    #imagen_descifrada = cipher.decrypt_and_verify(imagen_cifrada_bytes, tag_des)
    imagen_descifrada = cipher.decrypt(imagen_cifrada_bytes)
  except ValueError as e:
    # En caso de pérdida de datos o corrupción de la imagen en cifrado/descifrado, lanza excepción
    print(f"Error al descifrar la imagen: {e}")
    return

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
    imagen = "craneo.png"
    #print(f"HASH IMAGEN ORIGINAL: {generar_hash(imagen)}")
    password = "una_contraseña_segura_y_larga"
    salt = b"una_sal_aleatoria"
    clave = generar_clave(password, salt)
    # Nombres para los archivos cifrados/descifrados
    imagen_cifrada = "imagen_cifrada.png"
    imagen_descifrada = "imagen_descifrada.png"
    # Llamada a los métodos de cifrado/descifrado
    cifrar_imagen(imagen, clave, imagen_cifrada)
    descifrar_imagen(imagen_cifrada, clave, imagen_descifrada)
    # Cálculo del tiempo de ejecución del script
    fin = time.time()
    tiempo_ejecucion = fin - inicio
    print("Tiempo de ejecución:", tiempo_ejecucion, "segundos")