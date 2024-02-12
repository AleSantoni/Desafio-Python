
print("*******************************************************")
print("             Analizador de Texto")
print("*******************************************************")
print()
texto=input("Ingrese un texto para analizar : ").lower()
print()
#primera consigna#
a,b,c=input("Ingrese tres letras del abecedario :").lower()
letras_elegidas=[a,b,c]
r1=texto.count(a)
r2=texto.count(b)
r3=texto.count(c)
print()
print(f"La letra '{a}' apartece en el texto {r1} veces ")
print(f"La letra '{b}' apartece en el texto {r2} veces ")
print(f"La letra '{c}' apartece en el texto {r3} veces ")
print("////////////////////////////////////////////////////")
#Segunda consigna#
mi_lista=texto.split()
contador=len(mi_lista)
print(f"El texto tiene {contador} palabras")
print("////////////////////////////////////////////////////")
#Tercera consigna #
primera_letra=texto[0]
segunda_letra=texto[-1]
print(f"La primera letra es '{primera_letra}' y la ultima es '{segunda_letra}'")
print("////////////////////////////////////////////////////")
#Cuarta consigna mostrar texto en reversa #

mi_lista=texto.split()
mi_lista.reverse()

texto_reversa=" ".join(mi_lista)
print(texto_reversa)
print("////////////////////////////////////////////////////")
#Quinta consigna#
encontrado=("Pyhton" in mi_lista)
if encontrado==True:
    print("El texto contiene la palabra 'Python'")
else:

    print("El texto no contiene la palabra 'Python'")
