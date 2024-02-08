###############
### IMPORTS ###
import hashlib
import base64
import os
import time
import math

class matricula:
    ########################
    ### HASHING FUNCTION ###
    def hashing(word, salt):
        saltedpass =  str(word)  + str(salt)
        hash = hashlib.sha256(saltedpass.encode('utf-8')).digest()
        hash_base64 = base64.b64encode(hash)
        res = str(hash_base64.decode('utf-8'))
        return res
    ########################
    ### COMPARE FUNCTION ###
    def comparar(contra, result):
        if result == goal:
            print(f"HASH MATCHING! {result}")
            print(f"PASSWORD: {contra}")
            fin = time.time()
            tiempo_ejecucion = math.floor(fin - inicio)
            print(f"ELAPSED TIME: {tiempo_ejecucion} secs")
            return True
        return False
    ########################
    ### NUMBERS FUNCTION ###
    def pruebaNums(l1, l2, l3):
        for i in range(10**4): #----------------------------------------------------------------- Bucle que se ejecuta 10000 veces
            i1, i2, i3, i4 = i // 1000, (i % 1000) // 100, (i % 100) // 10, i % 10
            contra = f"{i1}{i2}{i3}{i4}{l1}{l2}{l3}"
            result = matricula.hashing(contra, salt)
            #print(result)
            if matricula.comparar(contra, result):
                break


if __name__ == "__main__":
    os.system('clear')
    inicio = time.time()
    ### DATA ###
    salt=39 #------------------------------------------------------------------------------------ salt
    l1 = 'L' #----------------------------------------------------------------------------------- primera letra de la matrícula
    goal ='tN8Sr9V3cOeqHyXSbkrFm0jXSJ+hVvlG1PkXyKxuRDc=' #----------------------------------------- hash objetivo
    letras = ['B','C','D','F','G','H','J','K','L','M','N','P','R','S','T','V','W','X','Y','Z']#-- posibles letras para la matrícula
    longitud = len(letras) #--------------------------------------------------------------------- longitud de la lista de letras

    print(f"Cracking hash: {goal} \n\n")

    for l3 in letras:
        for l2 in letras:
            matricula.pruebaNums(l1, l2, l3)