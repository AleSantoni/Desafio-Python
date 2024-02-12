
print()
print("*********Hola Buenos Dias**********")
print()
nombre = input("Cual es tu nombre?")
ventas= input("Cuales fueron tus ventas totales en este dia  ?")
resultado=round(float(ventas)*0.13,2)

print(f"Felicitaciones '{nombre}' el 13% de tus ventas fueron : {resultado}")