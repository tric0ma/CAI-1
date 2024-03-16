########## IMPORTS ###################################################
from pydicom import * #Librería para trabajar con imágenes DICOM
from PIL import Image #Librería para trabajar con imágenes en general
from Crypto.Cipher import AES #Cifrado AES
from Crypto.Util.Padding import pad, unpad #Relleno y padding del cifrado
import os #Librería para trabajar con el sistema operativo
import hashlib #Librería para trabajar con hashes
import time #Librería para calcular tiempos
######################################################################

# Función para redimensionar imágenes y poder trabajar con ellas después,
# necesario por la construcción del modelo AES-128-CBC y minimizar pérdidas
def redimensionar_imagen(imagen, tam):
  imagen = Image.open(imagen)
  return imagen.resize(tam).tobytes()# Guardamos los bytes de la imagen redimensionada

# Función para cifrar imágenes con parámetros: imagen, clave y formato de la imagen
def cifrar_imagen(imagen, clave, formato):
    # Comprobamos el formato de la imagen
    if formato == "DICOM":
      imagen_data = dcmread(imagen).PixelData.tobytes()
    elif formato in ("png", "jpg"):
      # Redimensionamos la imagen
      imagen_data = redimensionar_imagen(imagen, (512, 512))

    # Generar IV y clave
    iv = os.urandom(16)
    clave_aes = hashlib.pbkdf2_hmac('sha256', clave.encode(), b'salt', 100000, 32)

    # Cifrar la imagen
    imagen_data_padded = pad(imagen_data, AES.block_size) # Rellenamos con ceros para que sea multiplo de 16 bytes

    # Creamos objeto para el cifrado con la clave AES, el modo CBC y el vector de inicialización
    cipher = AES.new(clave_aes, AES.MODE_CBC, iv)

    # Ciframos/encriptamos la imagen con el modelo anterior
    imagen_cifrada = cipher.encrypt(imagen_data_padded)

    # Devolvemos la imagen cifrada junto con el vector de inicialización y el formato de la imagen
    return imagen_cifrada, iv, formato

# Función para descifrar la imagen previamente cifrada
def descifrar_imagen(imagen_cifrada, iv, clave, formato):
    clave_aes = hashlib.pbkdf2_hmac('sha256', clave.encode(), b'salt', 100000, 32)

    # Descifrar la imagen, para ello generamos un objeto cipher con el mismo modelo en el que
    # se cifró la imagen y el mismo vector de inicialización.
    cipher = AES.new(clave_aes, AES.MODE_CBC, iv)

    # Desciframos/desencriptamos la imagen previamente cifrada
    imagen_descifrada = cipher.decrypt(imagen_cifrada)

    # Elimianos el padding o relleno 
    imagen_descifrada = unpad(imagen_descifrada, AES.block_size)

    # Convertir bytes a imagen
    if formato == "dcm":
      imagen = Dataset()
      imagen.PixelData = imagen_descifrada
    elif formato in ("png", "jpg"):
      
      # Resizeamos la imagen al tamaño con el que se cifró para minimizar pérdidas o corrupción de datos
      imagen = Image.frombytes('RGB', (512, 512), imagen_descifrada)
    # Devolvemos la imagen resultante del descifrado
    return imagen

# MAIN #
if __name__ == '__main__':
  # Inicio del contador de tiempo
  inicio = time.time()
  # Ciframos la imagen, en este caso una radiografía en formato jpg con clave simple 12345
  imagen_cifrada, iv, formato = cifrar_imagen("pulmones_radiografia_web.jpg", "12345", "jpg")
  # Obtener la ruta del script para guardar en el mismo lugar la imagen cifrada/descifrada
  ruta_script = os.path.dirname(os.path.realpath(__file__))
  # Generar el nombre del archivo cifrado
  nombre_imagen_cifrada = "imagen_cifrada." + formato
  ruta_imagen_cifrada = os.path.join(ruta_script, nombre_imagen_cifrada)
  # Guardar la imagen cifrada
  with open(ruta_imagen_cifrada, "wb") as archivo:
    archivo.write(imagen_cifrada)
  # Descifrar la imagen
  imagen_descifrada = descifrar_imagen(imagen_cifrada, iv, "12345", formato)
  # Guardar la imagen descifrada
  if formato == "dcm":
    dcmwrite(imagen_descifrada, "imagen_descifrada.dcm")
  elif formato in ("png", "jpg"):
    imagen_descifrada.save("imagen_descifrada."+formato)
  fin = time.time()
  # Cálculo del tiempo de ejecución de este script
  tiempo_ejecucion = fin - inicio
  print("Tiempo de ejecución:", tiempo_ejecucion, "segundos")

