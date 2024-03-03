from random import randint
import hashlib
import base64


mensaje = "34567893 987344 120"

for i in range(4294967295, -1, -1):
    numero_32_bits = i
    suma = mensaje + str(numero_32_bits)
    print(suma)
    hash = hashlib.sha256(suma.encode('utf-8')).digest()
    
    hash_base64 = base64.b64encode(hash)
            #res = str(hash_base64.decode('utf-8'))
    #print(f"Hash base64: {hash_base64}")
    if str(hash_base64) == "F7HZhdhQIaNZ4HsQ7PEB9XAMGYK1ToVmNwX0hw8p4Tk=":
      print("ENCONTRADO \n")
      print(numero_32_bits)
      break