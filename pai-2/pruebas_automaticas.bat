@echo off

echo Ejecutando Caso de Prueba 1...
start cmd /c "py serversocket.py > servidor_prueba1.log 2>&1"
start cmd /c "py pruebasCliente.py Exito > cliente_prueba1.log 2>&1"
ping 127.0.0.1 -n 5 > nul

echo Ejecutando Caso de Prueba 2...
start cmd /c "py serversocket.py > servidor_prueba2.log 2>&1"
start cmd /c "py pruebasCliente.py Interceptar > cliente_prueba2.log 2>&1"
ping 127.0.0.1 -n 5 > nul

echo Ejecutando Caso de Prueba 3...
start cmd /c "py serversocket.py > servidor_prueba3.log 2>&1"
start cmd /c "py pruebasCliente.py Nonce > cliente_prueba3.log 2>&1"
ping 127.0.0.1 -n 5 > nul

echo Pruebas completadas.

start cmd /k type servidor_prueba1.log servidor_prueba2.log servidor_prueba3.log
start cmd /k type cliente_prueba1.log cliente_prueba2.log cliente_prueba3.log
finish
