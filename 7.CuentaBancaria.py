"""
Primero vas a crear una clase llamada Persona, y Persona
 va a tener solo dos atributos:
nombre y apellido. Luego, vas a crear una segunda clase
llamada Cliente, y Cliente va a
heredar de Persona, porque los clientes son personas, por
lo que el Cliente va a heredar
entonces los atributos de Persona, pero también va a tener
atributos propios, como número
de cuenta y balance, es decir, el saldo que tiene en su cuenta
bancaria.
Pero eso no es todo: Cliente también va a tener tres métodos.
El primero va a ser uno de los
métodos especiales y es el que permite que podamos imprimir a
nuestro cliente. Este método
va a permitir que cuando el código pida imprimir Cliente, se
muestren todos sus datos,
incluyendo el balance de su cuenta. Luego, un método llamado
Depositar, que le va a permitir
decidir cuánto dinero quiere agregar a su cuenta. Y finalmente,
un tercer método llamado
Retirar, que le permita decidir cuánto dinero quiere sacar de su
cuenta.
"""
class Persona:
    def __init__(self, nombre, apellido):
        self.nombre = nombre
        self.apellido = apellido
class Cliente(Persona):
    def __init__(self, nombre, apellido, num_cuenta):
        super().__init__(nombre, apellido)
        self.num_cuenta = num_cuenta
        self.saldo = 0

    def imprimir_cliente(self):

        print(f"Nombre: {self.nombre}\nApellido: {self.apellido}\nNumero de cuenta: {self.num_cuenta}\nSaldo $: {self.saldo}")

    def depositar(self, cantidad):
            self.saldo += cantidad
            print(f"Deposito exitoso, saldo actual: {self.saldo}")

    def retirar(self, cantidad):
        if  cantidad > self.saldo:
            print("Saldo insuficiente")
        elif  cantidad < 0:
            print("No se puede retirar un valor negativo")
        else:
            self.saldo -= cantidad
            print(f"Retiro exitoso, saldo actual: {self.saldo}")
def comprobarCliente(lista):
    while True:
        numeroCliente= int(input("Ingrese el numero de cliente: "))
        for cliente in lista:
            if cliente.num_cuenta == numeroCliente:
                print(f"Cliente encontrado bienvenido {cliente.nombre} , {cliente.apellido}")
                return cliente


        print("Cliente no encontrado")
def menu():
    lista_clientes = []
    cliente1 = Cliente("Alejandro", "Gasparini", 1)
    cliente2 = Cliente("Giuliana", "Gasparini", 2)
    cliente3 = Cliente("Juan", "Perez", 3)
    lista_clientes.append(cliente1)
    lista_clientes.append(cliente2)
    lista_clientes.append(cliente3)

    cliente=comprobarCliente(lista_clientes)
    while True:

        print("Bienvenido al Banco")
        print("Seleccione una opcion")
        print("1. Imprimir cliente")
        print("2. Depositar")
        print("3. Retirar")
        print("4. Salir")
        opcion = int(input("Ingrese la opcion: "))
        if opcion == 1:
            cliente.imprimir_cliente()
        elif opcion == 2:
            cantidad = int(input("Ingrese la cantidad a depositar: "))
            cliente.depositar(cantidad)
        elif opcion == 3:
            cantidad = int(input("Ingrese la cantidad a retirar: "))
            cliente.retirar(cantidad)
        elif opcion == 4:
            print("Saliendo del Menu del banco ")
            break

        else:
            print("Opcion invalida")
menu()
