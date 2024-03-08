import hashlib
import hmac

def calcular_mac(mensaje, key, nonce):

    digest = hmac.new(key,(mensaje + str(nonce)).encode('utf-8'), hashlib.sha256)
    return digest.hexdigest()