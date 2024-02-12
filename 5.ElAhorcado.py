from random import *


# Lista de palabras
palabras = ["python", "programacion", "ahorcado", "juego", "desarrollo"]

# Elegir una palabra al azar
palabra_secreta = choice(palabras)

# Lista de letras adivinadas
letras_adivinadas = ["_"] * len(palabra_secreta)

# Número de vidas
vidas = 6

# Función para mostrar el estado actual del juego
def mostrar_estado():
    print("Palabra secreta: ", " ".join(letras_adivinadas)) # muestra
    print("Vidas restantes:", vidas)

# Función para pedir al jugador que elija una letra
def pedir_letra():
    letra = input("Ingresa una letra: ").lower()
    return letra

# Función para comprobar si la letra ingresada es válida
def es_letra_valida(letra):
    return letra.isalpha() and len(letra) == 1 #comprueba si hay caracteres alfabeticos y que si la longitud es de 1

# Función para actualizar las letras adivinadas
def actualizar_letras_adivinadas(letra, palabra_secreta, letras_adivinadas):
    for i in range(len(palabra_secreta)):# recorre la lista de letras adivinadas y si coincide con la letra seleccionada, la reemplaza por la letra seleccionada.
        if palabra_secreta[i] == letra:
            letras_adivinadas[i] = letra

# Función principal del juego
def jugar_ahorcado():
    global vidas # declara la variable global vidas
    while vidas > 0 and "_" in letras_adivinadas:
        mostrar_estado()
        letra = pedir_letra()

        if es_letra_valida(letra):
            if letra in palabra_secreta:
                actualizar_letras_adivinadas(letra, palabra_secreta, letras_adivinadas)
                print("¡Letra correcta!")
            else:
                vidas -= 1
                print("Letra incorrecta. Pierdes una vida.")
        else:
            print("Ingresa una letra válida.")

    mostrar_estado()

    if "_" not in letras_adivinadas:
        print("¡Felicidades! Has adivinado la palabra.")
    else:
        print(f"Lo siento, has perdido. La palabra era: {palabra_secreta}")

# Llamar a la función principal del juego
jugar_ahorcado()


