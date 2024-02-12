from numeros import *


"""
llamar principal.py, donde vas a escribir las funciones que administran el 
funcionamiento del programa (como las instrucciones para elegir un área y para decidir si 
seguirá tomando nuevos turnos o si va a finalizar el programa). Recuerda que vas a necesitar 
importar el contenido de numeros.py dentro de principal.py para poder disponer de sus 
funciones. 



"""
def menu():
    print("*" * 50)


    print("         Bienvenido al sistema de turnos")
    print("1. Turnos de Farmacia")
    print("2. Turnos de Comsmetica")
    print("3. Turnos de Perfumeria")
    print("4. Salir")
    print("")

    try:
        opcion = int(input("Ingrese una opcion: "))
        return opcion

    except ValueError:
        print("Error: El valor ingresado no es un numero")
        print("*" * 50)






def main():
    while True:
        opcion = menu()
        if opcion == 1:
            imprimir_turno(generador_farmacia)
        elif opcion == 2:
            imprimir_turno(generador_cosmetica)
        elif opcion == 3:
            imprimir_turno(generador_perfumeria)
        elif opcion == 4:
            print("Gracias por utilizar el sistema")
            print("Hasta luego")

            break
        else:
            print("Opcion no valida")
            print("Intentelo de nuevo")
            print("*" * 50)


def inicio():

    main()

inicio()

