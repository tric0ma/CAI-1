# -*- coding: utf-8 -*-

resultados = []

with open("logs.txt", "r") as f:
     for log in f:
         mensaje = log.split(",")[1]
         resultado = mensaje.split(":")[1]
         if resultado.strip() == 'OK!':
             resultados.append(1)
         else:
             resultados.append(0)
                 
print('Tasa de éxito de las transferencias recibidas: ')
print(str(sum(resultados)/len(resultados)*100) + '%')
    
    
