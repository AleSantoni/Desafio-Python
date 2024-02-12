import math
import os
import time
import re
from pathlib import Path
import datetime

"""
¡Qué bueno que lograste abrirme!

Junto a esta nota se ha descomprimido 1 carpeta, y está repletas de 
subcarpetas y de archivos .txt.

No te preocupes por revisarlos, solo tienen texto aleatorio... 
excepto algunos. 

Tu trabajo es crear un Buscador de Números de Serie. ¿Qué es eso? 
Es un programa que se encargue de buscar números de serie que cumplan 
un determinado formato, dentro de un arbol de carpetas.

Tu programa va a recorrer todos los archivos y subcarpetas de un directorio
 raiz (en este caso, la carpeta que acabas de descomprimir), y va a buscar
 cualquier string que coincida con un patrón de número de serie. Sabemos
  que no puede haber más de un número de serie por archivo.

Para lograrlo vas a usar el módulo os para abrir e iterear por el directorio
, y las expresiones regulares para encontrar el formato de número de 
serie correcto.

A los fines de este ejercicio, estas son las condiciones de formato que deben
 cumplir los hallazgos:
- [N] + [tres carateres de texto] + [-] + [5 números]

Por ejemplo: Nryu-12365

La presentación en pantalla de los hallazgos debe ser un listado en
formato de tabla, que respete el siguiente formato de ejemplo:

----------------------------------------------------
Fecha de búsqueda: [fecha de hoy]

ARCHIVO		NRO. SERIE
-------		----------
texto1.txt	Nter-15496
texto25.txt	Ngba-85235

Números encontrados: 2
Duración de la búsqueda: 1 segundos
----------------------------------------------------

IMPORTANTE

* La 'Duración de búsqueda' debe estar redondeada hacia arriba

* No olvides que la mejor forma de recorrer un arbol de carpetas, probablemente sea con el método walk() de os.

* Observa que la fecha de búsqueda debe ser la fecha del día en que ejecutes el código, por lo que necesitas echar mano del módulo datetime.

* Animate a encontrar una manera de mostrar la fecha de hoy con el formato dd/mm/aa.

* Para informar la duración de la búsqueda al final de tu presentación, vas a necesitar del módulo time.

 Recuerda que para poder imprimir todo en formato de tabla puedes usar los caracteres especiales t para tabular.

"""

inicio=time.time()
print("Buscador de numeros de series")
ruta="C:\\Users\\asant\\OneDrive\\Documentos\\Curso Pyhton\\Dia 9\\Proyecto_Dia_9\\Mi_Gran_Directorio"
mi_patron=r"N\D{3}-\d{5}"
hoy=datetime.date.today()
nros_encontrados=[]
archivos_encontrados=[]

#funcion para encontrar archivos
def buscar_numero(archivo,patron):
    este_archivo=open(archivo,"r")
    texto=este_archivo.read()
    if re.search(patron,texto):
        return re.search(patron,texto)
    else:
        return ""

def crear_listas():
    for carpeta,subcarpetas, archivo in os.walk(ruta):
        for a in archivo:
            resultado=buscar_numero(Path(carpeta,a),mi_patron)
            if resultado != "":
                nros_encontrados.append(resultado.group())
                archivos_encontrados.append(a.title())


def mostrar_todo():
    indice=0
    print("-"*50)
    print(f"Fecha de búsqueda: {hoy.day} / {hoy.month} / {hoy.year} ")
    print("\n")
    print("ARCHIVO\t\t\tNRO. SERIE")
    print("-------\t\t\t----------")
    for a in archivos_encontrados:
        print(f"{a}\t{nros_encontrados[indice]}")
        indice+=1
    print("\n")
    print(f"Números encontrados: {len(nros_encontrados)}")
    fin=time.time()
    duracion=fin-inicio
    print(f"Duración de la búsqueda: {math.ceil(duracion)} segundos")
    print("-"*50)


crear_listas()
mostrar_todo()