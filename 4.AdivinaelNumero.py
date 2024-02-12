from random import randint

print("*******************************************************")
print("****************ADIVINA EL NUMERO *********************")
print("*******************************************************")
print()
nombre=input("Ingresa tu nombre: ")

intentos=8
random=randint(0,101)
print(random)

while intentos != 0 :
    numero = int(input("Eliga un numero entre el 1 y el 100 = "))

    if numero >0 and numero <101:


        if numero == random:
            print(f"Felicidades {nombre}, ganaste!! en {intentos} intentos")
            break
        elif numero < random:

            intentos -= 1
            if intentos == 0:
                print("Perdiste")
                break
            else:
                print(f"El numero es mayor te quedan {intentos} intentos ")

        elif numero > random:

            intentos -= 1
            if intentos == 0:
                print("Perdiste")
                break
            else:
                print(f"El numero es menor te quedan {intentos} intentos ")






    else:
        print("El numero ingresado es incorrecto")



