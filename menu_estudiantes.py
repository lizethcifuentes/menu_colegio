# se importa la libreria tkinter con todas sus funciones
from tkinter import *
from tkinter import messagebox

#funciones de la app
# entar  menu academico
def entrar():
    messagebox.showinfo("informacion", "¿desea ingresar?")
    cent = int(nombre.get())

#salir
def salir():
    messagebox.showinfo("informacion", "¿desea salir")
    cent = int(nombre.get())
    # salir
def salir():
    messagebox.showinfo("Temperatura 1.0", "La app se va a cerrar")
    ventana_principal.destroy()
 

# se declara una variable llamada ventana_principal, que adquiere las caracteristicas de un objeto Tk()
ventana_principal = Tk()

# titulo de la ventana
ventana_principal.title("encuesta")

# tamaño de la ventana
ventana_principal.geometry("700x600")

# deshabilitar boton de maximizar
ventana_principal.resizable(False, False)

# color de la ventana
ventana_principal.config(bg="thistle")

#--------------------------------
# variables globales
#--------------------------------
nombre = StringVar()
grado = StringVar()
codigo = StringVar()
tarjeta_identidad = StringVar()

#--------------------------------
# barra menu
#--------------------------------
barra_menu = Menu()
ventana_principal.config(menu=barra_menu)

menu_entrar = Menu(tearoff=0)
menu_entrar.add_command(label="entrar", command=entrar)
menu_entrar.add_separator()
menu_entrar.add_command(label="Borrar", command=salir)

menu_salir = Menu(tearoff=0)
menu_salir.add_command(label="Salir", command=salir)

barra_menu.add_cascade(label="entrar", menu=menu_entrar)
barra_menu.add_cascade(label="Salir", menu=menu_salir)

# frame entrada datos
#--------------------------------
frame_entrada = Frame(ventana_principal)
frame_entrada.config(bg="medium purple", width=490, height=180)
frame_entrada.place(x=10, y=10)

#logo app
logo=PhotoImage(file="img/escudo_colegio.png")
lb_logo=Label(ventana_principal, image=logo, bg="thistle")
lb_logo.place(x=10,y=50)

# titulo de la app
titulo = Label(ventana_principal, text="colegio san jose de guanenta")
titulo.config(bg="slate blue", fg="white", font=("garamond", 15))
titulo.place(x=10,y=20)

#titulo para datos
titulo = Label(ventana_principal, text="ingrese los siguientes datos")
titulo.config(bg="cyan", fg="black", font=("garamond", 10))
titulo.place(x=305,y=60)


# etiqueta para nombre
lb_nombre = Label(frame_entrada, text = "nombre: ")
lb_nombre.config(bg="cyan", fg="black", font=("garamond", 10))
lb_nombre.place(x=300, y=80)

# caja de texto para ingresar nombre
entry_nombre = Entry(frame_entrada, textvariable=nombre)
entry_nombre.config(bg="white", fg="black", font=("garamond", 10), width=6)
entry_nombre.focus_set()
entry_nombre.place(x=366,y=80)

# etiqueta para grado
lb_nombre = Label(frame_entrada, text = "grado: ")
lb_nombre.config(bg="cyan", fg="black", font=("garamond", 10))
lb_nombre.place(x=300, y=110)

# caja de texto para ingresar grado
entry_grado = Entry(frame_entrada, textvariable=grado)
entry_grado.config(bg="white", fg="black", font=("garamond", 10), width=6)
entry_grado.focus_set()
entry_grado.place(x=366,y=110)

# etiqueta para codigo estudiantil
lb_nombre = Label(frame_entrada, text = "codigo: ")
lb_nombre.config(bg="cyan", fg="black", font=("garamond", 10))
lb_nombre.place(x=300, y=140)

# caja de texto para ingresar grado
entry_grado = Entry(frame_entrada, textvariable=codigo)
entry_grado.config(bg="white", fg="black", font=("garamond", 10), width=6)
entry_grado.focus_set()
entry_grado.place(x=366,y=140)



#run
ventana_principal.mainloop()