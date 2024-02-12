from tkinter import *
import random
import datetime
from tkinter import messagebox,filedialog

from tkinter import IntVar, StringVar

operador=""
precios_comida=[200,300,400,500,600,700,800]
precios_bebida=[50.50,60.60,70.70,80.80,90.90,100,125.50]
precios_postre=[100,200,300,400,500,600,700]
def click_boton(numero):
    global operador
    operador=operador + numero
    visor_calculadora.delete(0, END)
    visor_calculadora.insert(END, operador)

def borrar():
    global operador
    operador=""
    visor_calculadora.delete(0, END)

def obtener_resultado():
    global operador
    resultado=str(eval(operador))
    visor_calculadora.delete(0, END)
    visor_calculadora.insert(0, resultado)
    operador=""
def revisar_check():
   x=0
   for comida in cuadro_comida:
       if variable_comidas[x].get()==1:
           cuadro_comida[x].config(state=NORMAL)
           if cuadro_comida[x].get()=="0":
               cuadro_comida[x].delete(0, END)
           cuadro_comida[x].focus()

       else:
           cuadro_comida[x].config(state=DISABLED)
           texto_comida[x].set("0")

       x +=1
   x=0
   for bebida in cuadro_bebida:
       if variable_bebidas[x].get()==1:
           cuadro_bebida[x].config(state=NORMAL)
           if cuadro_bebida[x].get() == "0":
               cuadro_bebida[x].delete(0, END)
           cuadro_bebida[x].focus()
       else:
           cuadro_bebida[x].config(state=DISABLED)
           texto_bebida[x].set("0")
       x +=1
   x=0
   for postre in cuadro_postre:
       if variable_postres[x].get()==1:
           cuadro_postre[x].config(state=NORMAL)
           if cuadro_postre[x].get() == "0":
               cuadro_postre[x].delete(0, END)
           cuadro_postre[x].focus()
       else:
           cuadro_postre[x].config(state=DISABLED)
           texto_postre[x].set("0")
       x +=1
def total():
    sub_total_comida = 0
    p = 0
    for cantida in texto_comida:
        sub_total_comida += float(cantida.get()) * precios_comida[p]
        p += 1

    sub_total_bebidas = 0
    p = 0
    for cantida in texto_bebida:
        sub_total_bebidas += float(cantida.get()) * precios_bebida[p]
        p += 1

    sub_total_postre = 0
    p = 0
    for cantida in texto_postre:
        sub_total_postre += float(cantida.get()) * precios_postre[p]
        p += 1
    sub_total=sub_total_comida+sub_total_bebidas+sub_total_postre
    impuesto=sub_total*0.07
    total=sub_total+impuesto

    var_costo_comida.set(f"${round(sub_total_comida,2)}")
    var_costo_bebida.set(f"${round(sub_total_bebidas,2)}")
    var_costo_postre.set(f"${round(sub_total_postre,2)}")
    var_subtotal.set(f"${round(sub_total,2)}")
    var_impuesto.set(f"${round(impuesto,2)}")
    var_total.set(f"${round(total,2)}")


def recibo():
    texto_recibo.delete(1.0, END)
    num_recibo=f"N# - {random.randint(1000,9999)}"
    fecha=datetime.datetime.now()
    fecha_recibo=f"Fecha - {fecha.day}/{fecha.month}/{fecha.year}  Hora - {fecha.hour}:{fecha.minute} "
    texto_recibo.insert(END, f"Datos:\t{num_recibo}\t\t{fecha_recibo}\n")
    texto_recibo.insert(END, f"*" * 77 + "\n")
    texto_recibo.insert(END, f"Items\t\tCant.\tCosto Items\n")
    texto_recibo.insert(END, f"-" * 97 + "\n")
    x=0

    for comida in texto_comida:
        if comida.get() !="0":
            texto_recibo.insert(END, f"{lista_comidas[x]}\t\t{comida.get()}\t"
                                         f"${int(comida.get())*precios_comida[x]}\n")
        x+=1
    x=0
    for bebida in texto_bebida:
        if bebida.get() !="0":
            texto_recibo.insert(END, f"{lista_bebidas[x]}\t\t{bebida.get()}\t"
                                     f"${int(bebida.get())*precios_bebida[x]}\n")
        x+=1
    x=0
    for postre in texto_postre:
        if postre.get() !="0":
            texto_recibo.insert(END, f"{lista_postres[x]}\t\t{postre.get()}\t"
                                     f"${int(postre.get())*precios_postre[x]}\n")
        x+=1

    texto_recibo.insert(END, f"-" * 97 + "\n")
    texto_recibo.insert(END, f"Costo Comida:\t\t\t{var_costo_comida.get()}\n")
    texto_recibo.insert(END, f"Costo Bebida:\t\t\t{var_costo_bebida.get()}\n")
    texto_recibo.insert(END, f"Costo Postre:\t\t\t{var_costo_postre.get()}\n")
    texto_recibo.insert(END, f"-" * 97 + "\n")
    texto_recibo.insert(END, f"SubTotal:\t\t\t{var_subtotal.get()}\n")
    texto_recibo.insert(END, f"Impuesto:\t\t\t{var_impuesto.get()}\n")
    texto_recibo.insert(END, f"Total:\t\t\t{var_total.get()}\n")
    texto_recibo.insert(END, f"*" * 77 + "\n")
    texto_recibo.insert(END, f"Gracias por su visita los esperamos pronto")

def guardar():
    info_recibo=texto_recibo.get(1.0, "end")
    archivo=filedialog.asksaveasfile(mode="w",defaultextension=".txt")
    archivo.write(info_recibo)
    archivo.close()
    messagebox.showinfo("Informacion", "Su recibo ha sido guardado")

def resetear():
    texto_recibo.delete(0.1, END)
    for texto in texto_comida:
        texto.set("0")
    for texto in texto_bebida:
        texto.set("0")
    for texto in texto_postre:
        texto.set("0")

    for cuadro in cuadro_comida:
        cuadro.config(state=DISABLED)
    for cuadro in cuadro_bebida:
        cuadro.config(state=DISABLED)
    for cuadro in cuadro_postre:
        cuadro.config(state=DISABLED)

    var_costo_comida.set("")
    var_costo_bebida.set("")
    var_costo_postre.set("")
    var_subtotal.set("")
    var_impuesto.set("")
    var_total.set("")

    for v in variable_comidas:
        v.set(0)
    for v in variable_bebidas:
        v.set(0)
    for v in variable_postres:
        v.set(0)


# iniciar tkinter
aplicacion= Tk()
#PTamaño de la ventana
aplicacion.geometry("1270x530+0+0")
#Evitar maximizar la ventana
aplicacion.resizable(0,0)
#Titulo de la ventana
aplicacion.title("Mi Restaurante - Sistema de Facturacion")
#Colores de la ventana
aplicacion.config(bg="burlywood")
# Panel Superior
panel_superior=Frame(aplicacion,  bd=1, relief=FLAT)
panel_superior.pack(side=TOP)
#etiqueta Titulo
etiqueta_titulo = Label(panel_superior, text="Sistema de Facturacion", font=("Dosis", 56), bg="burlywood",
                      fg="azure4", width=29,  height=1)
etiqueta_titulo.grid(row=100, column=0) # grid significa cuadricula
#Panel Izquierdo
panel_izquierdo = Frame(aplicacion,  bd=1, relief=FLAT, width=250, height=500, bg="azure4")
panel_izquierdo.pack(side=LEFT)

#Panel Costos
panel_costos = Frame(panel_izquierdo,  bd=1, relief=FLAT, bg="azure4",padx=100)
panel_costos.pack(side=BOTTOM)

#Panel Comidas
panel_comidas = LabelFrame(panel_izquierdo, text="Comidas",font=("Dosis",19, "bold"),  bd=1, relief=FLAT,
                           fg="azure4")
panel_comidas.pack(side=LEFT)
#Panel Bebidas
panel_bebidas = LabelFrame(panel_izquierdo, text="Bebidas",font=("Dosis",19, "bold"),  bd=1, relief=FLAT,fg="azure4")
panel_bebidas.pack(side=LEFT)
#Panel Postres
panel_postres = LabelFrame(panel_izquierdo, text="Postres",font=("Dosis",19, "bold"),  bd=1, relief=FLAT,fg="azure4")
panel_postres.pack(side=LEFT)

# Panel Derecha
panel_derecha = Frame(aplicacion,  bd=1, relief=FLAT)
panel_derecha.pack(side=RIGHT,expand=True)
#Panel Calculadora
panel_calculadora = Frame(panel_derecha,  bd=1, relief=FLAT, bg="burlywood")
panel_calculadora.pack()
#Panel  Recibo
panel_recibo = Frame(panel_derecha,  bd=1, relief=FLAT, bg="burlywood")
panel_recibo.pack()
#Panel Botones
panel_botones = Frame(panel_derecha,  bd=1, relief=FLAT, bg="burlywood")
panel_botones.pack()
#Listas de Productos
lista_comidas=["Milanesas", "Tacos", "Pasta", "Pizza Especial", "Ensalada", "Salmon","Pizza 4 Quesos"]
lista_bebidas=["Agua", "Coca Cola", "Fanta", "Sprite", "Vino", "Soda","Fernet"]
lista_postres=["Helado", "Flan", "Brownie", "Tiramisu", "Mousse ", "Pastel1", "Pastel2"]

#Generar items de comidas
variable_comidas=[]
cuadro_comida=[]
texto_comida=[]
contador=0
for comida in lista_comidas:

    #crear checkbuttons para comida
    variable_comidas.append("")
    variable_comidas[contador]=IntVar() # variable de control para el checkbutton, si esta seleccionado o no el checkbutton, se guarda en variable_comidas[contador] el valor 1 o 0, si esta seleccionado el checkbutton, el valor es 1,
    comida=Checkbutton(panel_comidas,
                       text=comida.title(),
                       font=("Dosis",19,"bold"),
                       onvalue=1,
                       offvalue=0,
                       variable=variable_comidas[contador],
                       command=revisar_check)
    comida.grid(row=contador,
                column=0,
                sticky=W)# sticky=W es para que se ajuste a la izquierda
    # crear cuadros de entrada
    cuadro_comida.append("")
    texto_comida.append("")
    texto_comida[contador] = StringVar() # variable de control para el cuadro de entrada, si esta seleccionado o no el checkbutton, se guarda en variable_comidas[contador] el valor 1 o 0, si esta seleccionado el checkbutton, el valor
    texto_comida[contador].set("0") # setear el valor de la variable de control, en este caso, setear el valor 0, para que no se muestre en el cuadro de entrada, solo cuando se seleccione el checkbutton, se
    cuadro_comida[contador]=Entry(panel_comidas,
                                 font=("Dosis",18,"bold"),
                                 bd=1,
                                 width=6,
                                 state=DISABLED,
                                 textvariable=texto_comida[contador])
    cuadro_comida[contador].grid(row=contador,
                                column=1)
    contador+=1
#Generar items de bebidas
variable_bebidas=[]
cuadro_bebida=[]
texto_bebida=[]
contador=0
for bebida in lista_bebidas:


    # crear checkbuttons para bebidas
    variable_bebidas.append("")
    variable_bebidas[contador]=IntVar() # variable de control para el checkbutton, si esta seleccionado o no el checkbutton, se guarda en variable_comidas[contador] el valor 1 o 0, si esta seleccionado el checkbutton, el valor es 1,
    bebida=Checkbutton(panel_bebidas,
                       text=bebida.title(),
                       font=("Dosis",19,"bold"),
                       onvalue=1,
                       offvalue=0,
                       variable=variable_bebidas[contador],
                       command=revisar_check)
    bebida.grid(row=contador,
                column=0,
                sticky=W)# sticky=W es para que se ajuste a la izquierda
    # crear cuadros de entrada
    cuadro_bebida.append("")
    texto_bebida.append("")
    texto_bebida[contador] = StringVar()  # variable de control para el cuadro de entrada, si esta seleccionado o no el checkbutton, se guarda en variable_comidas[contador] el valor 1 o 0, si esta seleccionado el checkbutton, el valor
    texto_bebida[contador].set("0")  # setear el valor de la variable de control, en este caso, setear el valor 0, para que no se muestre en el cuadro de entrada, solo cuando se seleccione el checkbutton, se
    cuadro_bebida[contador] = Entry(panel_bebidas,
                                   font=("Dosis", 18, "bold"),
                                   bd=1,
                                   width=6,
                                   state=DISABLED,
                                   textvariable=texto_bebida[contador])
    cuadro_bebida[contador].grid(row=contador,
                                column=1)
    contador+=1
#Generar items de postres
variable_postres=[]
cuadro_postre=[]
texto_postre=[]
contador=0
for postre in lista_postres:


    # crear checkbuttons para postres
    variable_postres.append("")
    variable_postres[contador]=IntVar() # variable de control para el checkbutton, si esta seleccionado o no el checkbutton, se guarda en variable_comidas[contador] el valor 1 o 0, si esta seleccionado el checkbutton, el valor es 1,
    postre=Checkbutton(panel_postres,
                       text=postre.title(),
                       font=("Dosis",19,"bold"),
                       onvalue=1,
                       offvalue=0,
                       variable=variable_postres[contador],
                       command=revisar_check)
    postre.grid(row=contador,
                column=0,
                sticky=W)# sticky=W es para que se ajuste a la izquierda
    # crear cuadros de entrada
    cuadro_postre.append("")
    texto_postre.append("")
    texto_postre[contador] = StringVar()  # variable de control para el cuadro de entrada, si esta seleccionado o no el checkbutton, se guarda en variable_comidas[contador] el valor 1 o 0, si esta seleccionado el checkbutton, el valor
    texto_postre[contador].set(
        "0")  # setear el valor de la variable de control, en este caso, setear el valor 0, para que no se muestre en el cuadro de entrada, solo cuando se seleccione el checkbutton, se
    cuadro_postre[contador] = Entry(panel_postres,
                                   font=("Dosis", 18, "bold"),
                                   bd=1,
                                   width=6,
                                   state=DISABLED,
                                   textvariable=texto_postre[contador])
    cuadro_postre[contador].grid(row=contador,
                                column=1)
    contador+=1
# variables
var_costo_comida=StringVar()
var_costo_bebida=StringVar()
var_costo_postre=StringVar()
var_subtotal=StringVar()
var_impuesto=StringVar()
var_total=StringVar()
#Etiquetas de costos y campo de entrada
etiqueta_costo_comida=Label(panel_costos,
                            text="Costo Comida",
                            font=("Dosis",12,"bold"),
                            fg="white",
                            bg="azure4")
etiqueta_costo_comida.grid(row=0,column=0)
texto_costo_comida=Entry(panel_costos,
                         font=("Dosis",12,"bold"),
                         bd=1,
                         width=10,
                         state="readonly",
                         textvariable=var_costo_comida)
texto_costo_comida.grid(row=0,column=1, padx=41)
# Etiquetas y campo de entrada para costo de bebidas
etiqueta_costo_bebida = Label(panel_costos,
                              text="Costo Bebidas",
                              font=("Dosis", 12, "bold"),
                              fg="white",
                              bg="azure4")
etiqueta_costo_bebida.grid(row=1, column=0)
texto_costo_bebida = Entry(panel_costos,
                           font=("Dosis", 12, "bold"),
                           bd=1,
                           width=10,
                           state="readonly",
                           textvariable=var_costo_bebida)
texto_costo_bebida.grid(row=1, column=1, padx=41)

# Etiquetas y campo de entrada para costo de postres
etiqueta_costo_postre = Label(panel_costos,
                              text="Costo Postres",
                              font=("Dosis", 12, "bold"),
                              fg="white",
                              bg="azure4")
etiqueta_costo_postre.grid(row=2, column=0)
texto_costo_postre = Entry(panel_costos,
                           font=("Dosis", 12, "bold"),
                           bd=1,
                           width=10,
                           state="readonly",
                           textvariable=var_costo_postre)
texto_costo_postre.grid(row=2, column=1, padx=41)
# Etiquetas para el subTotal
etiqueta_subtotal = Label(panel_costos,
                              text="SubTotal",
                              font=("Dosis", 12, "bold"),
                              fg="white",
                              bg="azure4")
etiqueta_subtotal.grid(row=0, column=2)
texto_subtotal = Entry(panel_costos,
                           font=("Dosis", 12, "bold"),
                           bd=1,
                           width=10,
                           state="readonly",
                           textvariable=var_subtotal)
texto_subtotal.grid(row=0, column=3, padx=41)
# Etiquetas para el Impuesto
etiqueta_impuestos = Label(panel_costos,
                              text="Impuestos",
                              font=("Dosis", 12, "bold"),
                              fg="white",
                              bg="azure4")
etiqueta_impuestos.grid(row=1, column=2)
texto_impuestos = Entry(panel_costos,
                           font=("Dosis", 12, "bold"),
                           bd=1,
                           width=10,
                           state="readonly",
                           textvariable=var_impuesto)
texto_impuestos.grid(row=1, column=3, padx=41)
# Etiquetas para el Total
etiqueta_Total = Label(panel_costos,
                              text="Total",
                              font=("Dosis", 12, "bold"),
                              fg="white",
                              bg="azure4")
etiqueta_Total.grid(row=2, column=2)
texto_Total = Entry(panel_costos,
                           font=("Dosis", 12, "bold"),
                           bd=1,
                           width=10,
                           state="readonly",
                           textvariable=var_total)
texto_Total.grid(row=2, column=3, padx=41)

# botones
botones=["total","recibo","guardar","resetear"]
botones_creados=[]
columnas=0
for boton in botones:
    boton=Button(panel_botones,
                 text=boton.title(),
                 font=("Dosis",14,"bold"),
                 fg="white",
                 bg="azure4",
                 bd=1,
                 width=9)
    botones_creados.append(boton)
    boton.grid(row=0,
               column=columnas,
               padx=5,
               pady=5)
    columnas+=1


botones_creados[0].config(command=total)
botones_creados[1].config(command=recibo)
botones_creados[2].config(command=guardar)
botones_creados[3].config(command=resetear)

# Area recibo
texto_recibo=Text(panel_recibo,
                  font=("Dosis",12,"bold"),
                  bd=1,
                  width=52,
                  height=10)
texto_recibo.grid(row=0,column=0)

#Calculadora
visor_calculadora=Entry(panel_calculadora,
                        font=("Dosis",16,"bold"),
                        width=39,
                        bd=1)
visor_calculadora.grid(row=0,
                       column=0,
                       columnspan=4)
botones_calculadora=["7","8","9","+","4","5","6","-","1","2","3","*","R","B","0","/"]
botones_guardados=[]

fila=1
columna=0
for boton in botones_calculadora:
    boton=Button(panel_calculadora,
                 text=boton.title(),
                 font=("Dosis",16,"bold"),
                 fg="white",
                 bg="azure4",
                 bd=1,
                 width=8)
    botones_guardados.append(boton) # guardar los botones en una lista, para poder acceder a ellos posteriormente, para poder activarlos o desactivarlos, segun sea necesario, en el codigo
    boton.grid(row=fila,
               column=columna)

    if columna==3:
        fila+=1
    columna += 1
    if columna==4:
        columna=0
botones_guardados[0].config(command=lambda:click_boton("7"))
botones_guardados[1].config(command=lambda:click_boton("8"))
botones_guardados[2].config(command=lambda:click_boton("9"))
botones_guardados[3].config(command=lambda:click_boton("+"))
botones_guardados[4].config(command=lambda:click_boton("4"))
botones_guardados[5].config(command=lambda:click_boton("5"))
botones_guardados[6].config(command=lambda:click_boton("6"))
botones_guardados[7].config(command=lambda:click_boton("-"))
botones_guardados[8].config(command=lambda:click_boton("1"))
botones_guardados[9].config(command=lambda:click_boton("2"))
botones_guardados[10].config(command=lambda:click_boton("3"))
botones_guardados[11].config(command=lambda:click_boton("*"))
botones_guardados[12].config(command=obtener_resultado)
botones_guardados[13].config(command=borrar)
botones_guardados[14].config(command=lambda:click_boton("0"))
botones_guardados[15].config(command=lambda:click_boton("/"))



# evitar que la pantalla se cierre

aplicacion.mainloop()
