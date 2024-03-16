# CAI 3 realizado por el grupo 12 de SSII. #

Para poder ejecutar cualquier script de este CAI 3, sera necesario crear un entorno virtual donde instalar las dependencias
o librerías necesarias de Python. Para ello puede ejecutar el siguiente comando para crear dicho entorno virtual:

- python -m venv nombreDelEntorno

Una vez creado el entorno accedemos a el mediante el comando:

- source nombreDelEntorno/bin/activate (En Linux)
- source nombreDelEntorno/Scripts/activate (En Windows)

Cuando estemos dentro del entorno instalaremos las dependencias empleadas a través del comando:
- pip install "dependencia"

las dependencias se muestran en el siguiente listado, donde solo tendrá que usar el nombre antes de "==":

cffi==1.16.0
cryptography==42.0.5
pillow==10.2.0
pycparser==2.21
pycryptodome==3.20.0
pydicom==2.4.4
