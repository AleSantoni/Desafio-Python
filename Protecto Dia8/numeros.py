from random import randint
"""
En nuestro caso, vas a crear el tunero para una farmacia que tiene tres áreas de atención:
perfumería, farmacia (que es donde venden los medicamentos), y cosméticos. Tu programa le
tiene que preguntar al cliente a cuál de las áreas desea dirigirse, y le va a dar un número de
turno según a qué área se dirija. Por ejemplo, si elige cosmética le va a dar el número C-54
(“C” de cosmética). Luego de eso, nos va a preguntar si queremos sacar otro turno. Esto, en
realidad, es para simular si viene un nuevo cliente. Y repetirá todo el proceso.
Algunas cosas a tener en cuenta:
Los diferentes clientes van a ir sacando turnos para diferentes áreas (perfumería, farmacia,
cosmética), en diferentes órdenes, por lo que el sistema debe llevar la cuenta de cuántos turnos
ha dado para cada una de esas áreas, y producir el siguiente número de cada área a medida
que se lo pida. ¿No te parece genial aprovechar la eficiencia de los generadores para poder
hacer esto?
Por otro lado, el mensaje donde le comunicamos el número de espera al cliente, debería tener
algo de texto adicional antes y después del número. Por ejemplo, “su turno es (-el número de
turno con el del comienzo-)”, y luego algo así como “aguarde y será atendido”. Para que
nuestro código no se repita, en vez de poner ese texto en cada una de las funciones que calculen
los números, podemos aprovechar la flexibilidad de los decoradores para crear ese texto
adicional una sola vez, y luego envolver a cualquiera de nuestras funciones con ese texto único.
Finalmente, deberías aprovechar que ahora ya sabes dividir tu programa en diferentes módulos,
y entonces separar el código en dos partes: por un lado, un módulo que se puede llamar
números.py, en el que vas a escribir todos los generadores y el decorador
"""
#Generador de turnos a l azzar


def generador_turnos(area):
    turno=0
    while True:
        turno+=1
        yield f"'{area}'-{turno}"


# Crear el generador fuera de la función imprimir_turno
generador_farmacia = generador_turnos("F")
generador_cosmetica = generador_turnos("C")
generador_perfumeria = generador_turnos("P")





def decorador_turno(funcion):
    def otra_funcion(area):

        print("Su turno ha sido asignado ")
        funcion(area)
        print("Aguarde un momento y sera atendido ")
        print()
    return otra_funcion


@decorador_turno
def imprimir_turno(generador):
    print(next(generador))



