# se importa la libreria tkinter con todas sus funciones
from tkinter import *
from tkinter import messagebox

#funciones de la app

# entar  menu academico
def abrir_toplevel_datos():
    global Toplevel_datos
    abrir_toplevel_datos = Toplevel()
    abrir_toplevel_datos.title("lizeth dayana cifuentes ortiz")
    abrir_toplevel_datos.resizable(False,False)
    abrir_toplevel_datos.geometry("350x350")
    abrir_toplevel_datos.config(bg="thistle")

    #salir
    def salir():
        messagebox.showinfo("definitiva", "¿desea salir?")
        abrir_toplevel_datos.destroy()

    #texto para nota procedimental
    procedimental=Label(abrir_toplevel_datos, text="procedimental:")
    procedimental.config(bg="cyan", fg="black", font=("garamond",10))  
    procedimental.place(x=40 , y=50)  

    #caja de texto para nota procedimental
    entry_procedimental=Entry(abrir_toplevel_datos)
    entry_procedimental.config(bg="cyan", fg="black",font=("garamond",10),width=15)
    entry_procedimental.focus_set()
    entry_procedimental.place(x=160, y=50)

    #texto para nota cognitiva
    cognitiva=Label(abrir_toplevel_datos, text="cognitiva:")
    cognitiva.config(bg="cyan", fg="black", font=("garamond",10))  
    cognitiva.place(x=40 , y=80)  

    #caja de texto para nota cognitiva
    entry_cognitiva=Entry(abrir_toplevel_datos)
    entry_cognitiva.config(bg="cyan", fg="black",font=("garamond",10),width=15)
    entry_cognitiva.focus_set()
    entry_cognitiva.place(x=160, y=80)

    #texto para nota autoevaluacion
    autoevaluacion=Label(abrir_toplevel_datos, text="autoevaluacion:")
    autoevaluacion.config(bg="cyan", fg="black", font=("garamond",10))  
    autoevaluacion.place(x=40 , y=110)  

    #caja de texto para nota autoevaluacion
    entry_autoevaluacion=Entry(abrir_toplevel_datos)
    entry_autoevaluacion.config(bg="cyan", fg="black",font=("garamond",10),width=15)
    entry_autoevaluacion.focus_set()
    entry_autoevaluacion.place(x=160, y=110)

    
    #texto para nota bimestral
    bimestral=Label(abrir_toplevel_datos, text="bimestral:")
    bimestral.config(bg="cyan", fg="black", font=("garamond",10))  
    bimestral.place(x=40 , y=140)  

    #caja de texto para nota bimestral
    entry_bimestral=Entry(abrir_toplevel_datos)
    entry_bimestral.config(bg="cyan", fg="black",font=("garamond",10),width=15)
    entry_bimestral.focus_set()
    entry_bimestral.place(x=160, y=140)

    #texto para nota actitudinal
    actitudinal=Label(abrir_toplevel_datos, text="actitudinal:")
    actitudinal.config(bg="cyan", fg="black", font=("garamond",10))  
    actitudinal.place(x=40 , y=170)  

    #caja de texto para nota actitudinal
    entry_actitudinal=Entry(abrir_toplevel_datos)
    entry_actitudinal.config(bg="cyan", fg="black",font=("garamond",10),width=15)
    entry_actitudinal.focus_set()
    entry_actitudinal.place(x=160, y=170)


    def convertir():
        messagebox.showinfo("Nota Difinitiva", "Operacion realizada")

        # variables notas
        entry_proce_def = float(entry_procedimental.get())
        entry_cog_def = float(entry_cognitiva.get())
        entry_auto_def = float(entry_autoevaluacion.get())
        entry_acti_def = float(entry_actitudinal.get())
        entry_bime_def = float(entry_bimestral.get())

        entry_not_final = (0.3*entry_proce_def) + (0.3*entry_cog_def) + (0.1*entry_auto_def) + (0.1*entry_acti_def) + (0.2*entry_bime_def)

        if entry_not_final < 30:
                messagebox.showinfo("Resultado", "su nota definitiva es:  "+str(entry_not_final))
        else:
                messagebox.showinfo("Resultado", "su nota definitiva es:  "+str(entry_not_final))
# boton para convertir
    bt_convertir = Button(abrir_toplevel_datos,text="Resultado", command=convertir)
    bt_convertir.place(x=200, y=250, width=150, height=100)
    




#entrar menu medico general
def abrir_toplevel_salud():
    global toplevel_salud
    abrir_toplevel_salud = Toplevel()
    abrir_toplevel_salud.title("lizeth dayana cifuentes ortiz")
    abrir_toplevel_salud.resizable(False,False)
    abrir_toplevel_salud.geometry("350x350")
    abrir_toplevel_salud.config(bg="thistle")    

    #texto para peso
    peso=Label(abrir_toplevel_salud, text="peso:")
    peso.config(bg="cyan", fg="black", font=("garamond",10))  
    peso.place(x=40 , y=50)  

    #caja de texto para peso
    entry_peso=Entry(abrir_toplevel_salud)
    entry_peso.config(bg="cyan", fg="black",font=("garamond",10),width=15)
    entry_peso.focus_set()
    entry_peso.place(x=90, y=50)

    #texto para estatura
    estatura=Label(abrir_toplevel_salud, text="estatura:")
    estatura.config(bg="cyan", fg="black", font=("garamond",10))  
    estatura.place(x=40 , y=80)  

    #caja de texto para estatura
    entry_estatura=Entry(abrir_toplevel_salud)
    entry_estatura.config(bg="cyan", fg="black",font=("garamond",10),width=15)
    entry_estatura.focus_set()
    entry_estatura.place(x=110, y=80)

    

    def convertir_imc ():
        estatura = float(entry_estatura.get())
        peso = float(entry_peso.get())
        imc = peso / estatura**2
      
        if imc < 16:
            messagebox.showinfo("Resultado","esta muy flaco ")
        elif imc < 17:
            messagebox.showinfo("Resultado","esta en delgadez moderada")
        elif imc < 18.5:
            messagebox.showinfo("Resultado","esta en delgadez ligera")
        elif imc < 25:
            messagebox.showinfo("Resultado","esta saludable Saludable")
        elif imc < 30:
            messagebox.showinfo("Resultado","esta en Sobrepeso, a cuidarse")
        elif imc < 35:
            messagebox.showinfo("Resultado","esta en Obesidad grado I")
        elif imc < 40:
            messagebox.showinfo("Resultado","esta en Obesidad grado II")
        else:
             messagebox.showinfo("Resultado","esta en Obesidad grado III")
    # boton para convertir
    bt_convertir = Button(abrir_toplevel_salud,text="Resultado", command=convertir_imc)
    bt_convertir.place(x=200, y=170, width=150, height=100)
    

   
 
def entrar():
    messagebox.showinfo("informacion", "¿desea ingresar?")
    cent = int(nombre.get())

#salir
def salir():
    messagebox.showinfo("informacion", "¿desea salir")
    cent = int(nombre.get())
    # salir
def salir():
    messagebox.showinfo("colegio_san_jose_de_gualenta", "La app se va a cerrar")
    ventana_principal.destroy()
 

# se declara una variable llamada ventana_principal, que adquiere las caracteristicas de un objeto Tk()
ventana_principal = Tk()

# titulo de la ventana
ventana_principal.title("lizeth dayana cifuentes ortiz")

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
global img_salud
global img_datos

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

#-------------------------------
# frame entrada datos
#--------------------------------
frame_entrada = Frame(ventana_principal)
frame_entrada.config(bg="medium purple", width=500, height=500)
frame_entrada.place(x=10, y=10)

#logo app
logo=PhotoImage(file="img/escudo_colegio.png")
lb_logo=Label(ventana_principal, image=logo, bg="thistle")
lb_logo.place(x=10,y=50)


#boton para datos academicos
datos=PhotoImage(file="img/datos.png")
bt_datos =Button(frame_entrada, command=abrir_toplevel_datos)
bt_datos.config(image=datos, width=150, height=150)
bt_datos.place(x=50, y=300)

#boton para salud
salud=PhotoImage(file="img/salud.png")
bt_salud =Button(frame_entrada, command=abrir_toplevel_salud)
bt_salud.config(image=salud, width=150, height=150)
bt_salud.place(x=300, y=300)

# creamos los objetos para cada imagen
img_salud = PhotoImage(file="img/salud.png")
img_datos = PhotoImage(file="img/datos.png")



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

# caja de texto para ingresar codigo estudiantil
entry_grado = Entry(frame_entrada, textvariable=codigo)
entry_grado.config(bg="white", fg="black", font=("garamond", 10), width=6)
entry_grado.focus_set()
entry_grado.place(x=366,y=140)

ventana_principal.mainloop()