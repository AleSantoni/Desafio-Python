
from pathlib import Path
from os import *



# Menu de opciones
def menu():
    print()
    print("*///////////////////////////////////////////////////////////////")

    print("******Bienvenido al Recetario de la Abuela TATA******")
    print()
    ruta=Path("C:/Users/asant/Recetas")
    print(f"La ruta del recetario es {ruta}")
    print()
    contador=0
    for archivo in ruta.glob("**/*.txt"):
        contador+=1
    print(f"En este Recetario encontraras {contador} recetas para disfrutar")
    print()
    print("*******************MENU*****************")
    print("             1 - Leer Receta")
    print("             2 - Crear Recetas")
    print("             3 - Crear Categoria")
    print("             4 - Eliminar Recetas")
    print("             5 - Eliminar Categoria")
    print("             6 - Finalizar Programa")
    print()
    print("*///////////////////////////////////////////////////////////////")
    opcion=obtener_opcion()
    if opcion == 1:
        opc=menu_categoria()
        leer_recetas(opc)
    elif opcion == 2:

        opc = menu_categoria()
        crear_receta(opc)
        print("Receta creada correctamente")
    elif opcion == 3:
        crear_categoria()





# Función para obtener la opción seleccionada
def obtener_opcion():
    while True:
        try:
            opcion = int(input("Ingrese una opción : "))
            if 1 <= opcion <= 6:
                return opcion
            else:
                print("Opción no válida. Por favor, ingrese un número entre 1 y 6.")
        except ValueError:
            print("Por favor, ingrese un número entero válido.")


#  Función para mostrar el menú de categorías

def menu_categoria():
    ruta = Path("C:/Users/asant/Recetas")

    print()
    print("*******************CATEGORIAS*****************")
    print()

    opciones = {}
    for indice, carpeta in enumerate(ruta.iterdir(), start=1):
        if carpeta.is_dir():
            opciones[indice] = carpeta
            print(f" {indice} - {carpeta.name}")

    print(f" {len(opciones) + 1} - Salir")
    print()

    while True:
        try:
            opcion = int(input("Ingrese el número de la categoría que desea ver o ingrese 0 para salir: "))

            if opcion == 0:
                return None
            elif 1 <= opcion <= len(opciones):
                return opciones[opcion].name
            else:
                print(f"Opción no válida. Por favor, ingrese un número entre 1 y {len(opciones)} o 6 para salir.")
        except ValueError:
            print("Por favor, ingrese un número entero válido.")
# funcion para recorrer una categoria y ver las recetas


def leer_recetas(ruta, opcion_categoria):
    categoria_ruta = ruta / opcion_categoria

    print()
    print(f"********** RECETAS DE LA CATEGORÍA: {opcion_categoria} **********")
    print()

    for indice, receta in enumerate(categoria_ruta.glob("**/*.txt"), start=1):
        print(f"{indice} - {receta.stem}")

    while True:
        try:
            indice = int(input("Ingrese el número de la receta que desea ver o ingrese 0 para salir: "))

            if indice == 0:
                return
            elif 1 <= indice <= len(list(categoria_ruta.glob("**/*.txt"))):
                receta_ruta = categoria_ruta / f"{indice}.txt"
                with open(receta_ruta, "r") as receta:
                    print(receta.read())
                return
            else:
                print(
                    f"Opción no válida. Por favor, ingrese un número entre 1 y {len(list(categoria_ruta.glob('**/*.txt')))} o 0 para salir.")
        except ValueError:
            print("Por favor, ingrese un número entero válido.")

# funcion para ingresar a las categorias





def crear_receta(opcion):
    if opcion == 1:
        print("Carnes")
        ruta = Path("C:/Users/asant/Recetas/Carnes")
        alta_receta(ruta)
    elif opcion == 2:
        print("Pastas")
        ruta = Path("C:/Users/asant/Recetas/Pastas")
        alta_receta(ruta)
    elif opcion == 3:
        print("Ensaladas")
        ruta = Path("C:/Users/asant/Recetas/Ensaladas")
        alta_receta(ruta)
    elif opcion == 4:
        print("Postres")
        ruta = Path("C:/Users/asant/Recetas/Postres")
        alta_receta(ruta)
    elif opcion == 5:
        print("Salir")






    elif opcion == 2:
        print("Pastas")
        ruta = Path("C:/Users/asant/Recetas/Pastas")


    elif opcion == 3:
        print("Ensaladas")
        ruta = Path("C:/Users/asant/Recetas/Ensaladas")

    elif opcion == 4:
        print("Postres")
        ruta = Path("C:/Users/asant/Recetas/Postres")


    elif opcion == 5:
        print("Salir")
def alta_receta(ruta):
    nombre = input("Ingrese el nombre de la receta : ")
    texto = input("Ingrese el texto de la receta : ")
    receta = open(ruta / f"{nombre}.txt", "w")
    receta.write(texto)

def crear_categoria():
    nombre = input("Ingrese el nombre de la categoria : ")
    ruta = Path("C:/Users/asant/Recetas")
    #crear un a carpeta
    ruta = ruta / nombre
    ruta.mkdir()
    print("Categoria creada correctamente")

def eliminar_receta():
    print("Eliminar Receta")
    menu_categoria()
    opcion = int(input("Digite la categoria en donde se encuentra la receta: "))
    if opcion == 1:
        print("Carnes")
        ruta = Path("C:/Users/asant/Recetas/Carnes")










"""

    
    menu_categoria()
    nombre=input("Ingrese el nombre de la receta : ")
    texto=input("Ingrese el texto de la receta : ")

    
def crear_categoria():
def eliminar_receta():
def eliminar_categoria():
    
# funcion swicht para ejecutar las opciones
def ejecutar_opcion(opcion):
    if opcion == 1:
        leer_receta()
    elif opcion == 2:
        crear_receta()
    elif opcion == 3:
        crear_categoria()
    elif opcion == 4:
        eliminar_receta()
    elif opcion == 5:
        eliminar_categoria()
    elif opcion == 6:
        print("Gracias por utilizar el programa.")
    
    system("cls")
 """
ruta=Path("C:/Users/asant/Recetas")
categoria=menu_categoria()
leer_recetas(ruta,categoria)