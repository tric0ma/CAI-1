###############
### IMPORTS ###
import hashlib
import base64
import nltk
#nltk.download('words') #solo hace falta ejecutar esta 
                       #linea la primera vez
from nltk.corpus import words
import time
import math
import os

class ingles:

    def hashing(word, salt):

            saltedpass =  str(word).lower() + str(salt)
            hash = hashlib.sha256(saltedpass.encode('utf-8')).digest()
            hash_base64 = base64.b64encode(hash)
            res = str(hash_base64.decode('utf-8'))
            return res


    def comparar(result, goal):
        if result == goal:
            print(f"HASH MATCHING! {result}")
            print(f"PASSWORD: {w}")
            fin = time.time()
            tiempo_ejecucion = math.floor(fin - inicio)
            print(f"ELAPSED TIME: {tiempo_ejecucion} secs")

            return True
        return False

if __name__ == "__main__":

    os.system('clear')
    inicio = time.time()
    english_words = words.words()
    goal = 'i9wtdI1MWrc9erJH0cDL6Mqyh4fOEs2NIEPp8k+VhqU='
    salt = 40
    print(f"Cracking hash: {goal} \n\n")
    for w in english_words:
        result = ingles.hashing(w,salt)
        if ingles.comparar(result, goal):
            break 