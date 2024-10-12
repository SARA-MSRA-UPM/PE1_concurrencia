# Practica Guiada 1 - Concurrencia y Paralelismo

Este repositorio contiene el código de la práctica guiada "Concurrencia y
Paralelismo" de la asignatura Software Avanzado Radar (SARA) del Master en
Sistemas Radar.

El repositorio contiene las siguientes carpetas:
- `app`: contiene el archivo main.py para ejecutar la aplicación y la carpeta
  `src` donde se situan el resto de archivos.
- `app/src`: contiene cada uno de los paquetes de python que usaremos durante
  el desarrollo de la práctica dividido de forma básica por las diferentes
  funcionalidades.
    - `actors`: contiene las distintas clases con la lógica de funcionamiento
      principal de la práctica
    - `helpers`: contiene archivos con funcionalidades generales del proyecto
      que pueden ser utilizada por cualquier clase principal.
    - `base`: contine clases base utilizadas en como núcleo de distintas
      funcionalidades del proyecto.

## Escenario de la práctica
El escenario de la práctica consiste en una implementación de un modelo
digital de un radar. Además del modelo del radar también existe un modelo
digital de puntos con distintas caraterísticas que pueden ser detectados por
el radar. Presenta la misma estructura e implementación que en la 
[Práctica Guiada 1](https://github.com/SARA-MSRA-UPM/PG1_concurrencia).

## Ejecución
El primer paso para poder ejecutar la práctica y comprobar su funcionamiento
será la creación de un entorno virtual propio del proyecto. En PyCharm es
posible crear un entorno virtual mediante la interfaz gráfica. En caso
necesario los comandos son los siguientes.
```
# Linux
# Crear
python3 -m venv venv
# Activar
source venv/bin/activate
# Desactivar
deactivate

# Windows
# Crear
python3 -m venv venv
# Activar
venv\Scripts\activate.bat
venv\Scripts\Activate.ps1
# Desactivar
deactivate
```

Una vez creado el entorno virtual es necesario instalar las dependencias
propias del proyecto. Las dependencias están definidas en el fichero
`requirements.txt`. En PyCharm se pueden instalar las dependencias mediante la
interfaz gráfica. En caso necesario los comandos son los siguientes.
```
pip install -r requirements.txt
```

Por último tras instalar las dependencias necesarias en nuestro entorno
virtual podemos arrancar el proceso principal de nuestro proyecto ejecutando
el fichero `app/main.py`.
```
python3 app/main.py
```

## Objetivos a realizar
1. **Ejecución con varios radares y lectores** Durante la primera práctica 
guiada utilizamos un único radar y un único lector. El primer objetivo de esta 
práctica es realizar las modificaciones necesarias en la aplicación para que 
se ejecuten de forma concurrente varias hebrás de radares y varios lectores.

2. **Encontrar detecciones comunes** El segundo objetivo es buscar detecciones 
de puntos por varios radares distintos. Para esto es necesario haber 
completado el primer objetivo. Para esto se facilita el esqueleto de las 
clases `DetetectionsSet` y `CommonDetectionsSearcher`. Aunque no es 
obligatorio implementar la funcionalidad mediante estas clases es recomendado. 

   1. **Implementar DetectionsSet** Esta clase representa una estructura de 
   datos en la que se guardarán el conjunto de todas las detecciones de los 
   distintos radares en ejecución. 

   2. **Implementar CommonDetectionsSearcher** Esta clase debe implementar la 
   funcionalidad de  busqueda de puntos comunes. Las detecciones de los 
   distintos radares los obtendrá de `DetectionsSet`.
