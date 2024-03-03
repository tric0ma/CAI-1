###############
### IMPORTS ###
import hashlib
import base64
from datetime import datetime, timedelta
import time
import os
import math

class fecha:
    def hashing(word, salt):
            saltedpass =  str(word).lower() + str(salt)
            hash = hashlib.sha256(saltedpass.encode('utf-8')).digest()
            hash_base64 = base64.b64encode(hash)
            res = str(hash_base64.decode('utf-8'))
            return res

    def comparar(result, goal):
        if result == goal:
            print(f"HASH MATCHING! {result}")
            print(f"PASSWORD: {fecha_actual}")
            fin = time.time()
            tiempo_ejecucion = math.floor(fin - inicio)
            print(f"ELAPSED TIME: {tiempo_ejecucion} secs")
            return True
        return False


if __name__ == "__main__":
    os.system('clear')
    inicio = time.time()
    goal = '95qamsyzWZOlJq5/glwBO2u/ijcH7SFlDoS2ZCtAIzY='
    salt = 18
    print(f"Cracking hash: {goal} \n\n")
    #Definir la fecha inicial y final
    fecha_inicial = datetime(2010, 1, 1)
    fecha_final = datetime(2020, 12, 31)
    #Iterar sobre cada día desde la fecha inicial hasta la fecha final
    fecha_actual = fecha_inicial
    while fecha_actual <= fecha_final:
        # Formatear la fecha en "ddMMyyyy"
        fecha_formateada = fecha_actual.strftime("%d%m%Y")
        #Imprimir la fecha formateada
        result = fecha.hashing(fecha_formateada,salt)
        if fecha.comparar(result, goal):
            break
        #Incrementar la fecha actual en un día
        fecha_actual += timedelta(days=1) 