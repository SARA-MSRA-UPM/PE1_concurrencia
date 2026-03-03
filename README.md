# Practica Entregable 1 - Concurrencia y Paralelismo

Este repositorio contiene el código de la práctica entregable "Concurrencia y
Paralelismo" de la asignatura Software Avanzado Radar (SARA) del Master en
Sistemas Radar.

El repositorio contiene las siguientes carpetas:

- `app`: contiene el archivo main.py para ejecutar la aplicación y ficheros
relacionados con el código de la aplicación.
- `app/src`: contiene cada uno de los paquetes de python que usaremos durante el
  desarrollo de la práctica dividido de forma básica por las diferentes
  funcionalidades.
  - `actors`: contiene las distintas clases con la lógica de funcionamiento
  principal de la práctica
  - `helpers`: contiene archivos con funcionalidades generales del proyecto que
  pueden ser utilizada por cualquier clase principal.
  - `models`: contine clases que actuan como modelos de datos del proyecto.
  - `monitors`: contiene las clases relacionadas con la implementación de los
  monitores de la práctica.

## Escenario de la práctica

El escenario consiste en el modelo digital de un radar. Además del modelo del
radar también existe un modelo digital de puntos con distintas caraterísticas
que serán detectados por el radar. Estos modelos serán los actores principales
y su implementación se puede consultar en el paquete `app/actors/*`.

Ambos modelos digitales son entidades independientes por lo que se han están
implementados utilizando hebras permitiendo su ejecución de concurrente. Esto
provoca que nos veamos obligados a implementar algún pratón de diseño de los
estudiados con el objetivo de manejar los datos generados por las distintas
detecciones del radar. Los patrones que vamos a utilizar son "Monitor" y
"Productor-Consumidor".

Para más detalles sobre las clases implementadas se puede consultar la
[Práctica Guiada 1](https://github.com/SARA-MSRA-UPM/PG1_concurrencia).

## Ejecución

El primer paso para poder ejecutar la práctica y comprobar su funcionamiento
será la creación de un entorno virtual propio del proyecto. Normalmente el IDE
al no encontrar un entorno virtual creado preguntará automáticamente si se desea
crearlo. En cualquier caso se pude crear utilizando los siguientes comandos:

- Linux

```shell
python3 -m venv .venv
source .venv/bin/activate
```

- Windows

```powershell
python3 -m venv venv
venv\Scripts\Activate.ps1
```

Una vez creado el entorno virtual es necesario instalar las dependencias propias
del proyecto. Las dependencias están definidas en el fichero `requirements.txt`.
Generalmente hay opciones para instalarlas de forma automática desde el IDE,
pero también se pueden instalar manualmente utilizando el siguiente comando:

```shell
pip install -r requirements.txt
```

Por último tras instalar las dependencias necesarias en nuestro entorno virtual
podemos arrancar el proceso principal de nuestro proyecto ejecutando el fichero
`app/main.py`.

```shell
python3 app/main.py
```

## Objetivos a realizar

1. **Ejecución con varios radares y cosumidores** Durante la primera práctica
guiada utilizamos un único radar y un único consumidor. El primer objetivo de
esta práctica es realizar las modificaciones necesarias en la aplicación para
que se ejecuten de forma concurrente varias hebras de radares y varios
consumidores.

2. **Encontrar detecciones comunes** El segundo objetivo es buscar detecciones
de puntos por varios radares distintos. Para esto es necesario haber
completado el primer objetivo. Para esto se facilita el esqueleto de las
clases `SystemDetectionsData` y `CommonDetectionsSearcher`. Aunque no es
obligatorio implementar la funcionalidad mediante estas clases es recomendado.
Deben existir al menos 3 radares que produzcan datos en al menos 2 monitores
distintos (cada radar solo puede estar conectado a un monitor). Cada monitor
tendrá un consumidor que consume sus datos. Los distintos consumidores cargarán los
datos leídos en un único objeto `SystemDetectionsData`.

   1. **Implementar SystemDetectionsData** Esta clase representa una estructura de
   datos en la que se guardarán el conjunto de todas las detecciones de los
   distintos radares en ejecución. Debe estar protegido frente a concurrencia
   al igual que la clase `DetectionsMonitor`.

   2. **Implementar CommonDetectionsSearcher** Esta clase debe implementar la
   funcionalidad de  busqueda de puntos comunes. Las detecciones de los
   distintos radares los obtendrá de `SystemDetectionsData`.
      - Esta clase se implementará como otra hebra al igual que
      `DetectionsConsumer` o `Radar`.
      - Debe realizar la busqueda de puntos comunes cada un cierto tiempo,
      largo comparado con la frecuencia de detecciones, cada 5 segundos
      debería ser suficiente.
