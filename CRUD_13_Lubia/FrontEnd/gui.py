
from tkinter import *
from tkinter import ttk
from PIL import ImageTk, Image
import demo_database
import mysql.connector
 
window = Tk()

img = ImageTk.PhotoImage(Image.open("Inicio 2.png"))
frame_title =Label(window, image = img, width=150, height=150).pack(padx=30 , pady=2)



frame_app = Frame(window, width=800, height=500, bg="#3CB371")
frame_app.pack()
window.title("Inicio de sesion ")
 
connection =mysql.connector.connect(host="localhost", 
                                  user="root", 
                                  passwd="", 
                                  database="db_inicio")
 
nombre = StringVar()
correo = StringVar()
contrasena = StringVar()
 
def crear_registro():
    nombre = entry_nombre.get()
    correo = entry_correo.get()
    contrasena = entry_contrasena.get()
    
    inicio_db = demo_database.MyDatabase()
    data = (nombre, correo, contrasena)
    print(data)
    inicio_db.insert_db(nombre, correo, contrasena)

frame_navbar = Frame(frame_app, width=900, height=100,bg="#3CB371")
frame_navbar.grid(row=0, column=0)
frame_title = Frame(frame_app, width=900, height=150,bg="#3CB371")
frame_title.grid(row=1, column=0)
frame_options = Frame(frame_app, width=900, height=600 ,bg="#3CB371")
frame_options.grid(row=2, column=0)
 
frame_food = Frame(frame_options, width=350, height=500, bg="#3CB371")
frame_food.place(x=25, y=-10)
label_nombre = Label(frame_food, 
              text="Nombre:",
              font=("Franklin Gothic Medium Cond", "22", "bold"),
              fg="white",
              bg="#3CB371")
label_nombre.place(x=20, y=10)
entry_nombre = Entry(frame_food, justify=LEFT, width=30, font=("Calibri", "14", "bold"))
entry_nombre.place(x=20, y=47)
label_correo = Label(frame_food, 
              text="Correo :",
              font=("Franklin Gothic Medium Cond", "22", "bold"),
              fg="white",
              bg="#3CB371")
label_correo.place(x=20, y=80)
entry_correo = Entry(frame_food, justify=LEFT, width=30, font=("Calibri", "14", "bold"))
entry_correo.place(x=20, y=117)
label_contrasena = Label(frame_food, 
              text="Contrasena:",
              font=("Franklin Gothic Medium Cond", "22", "bold"),
              fg="white",
              bg="#3CB371")
label_contrasena.place(x=20, y=150)
entry_contrasena = Entry(frame_food, justify=LEFT, width=30, font=("Calibri", "14", "bold"))
entry_contrasena.place(x=20, y=188)
 
button_agregar = Button(frame_food, text="Insertar", command=crear_registro, font=("Calibri", "14", "bold"))
button_agregar.place(x=70, y=230)

def Leer():

    my_table = ttk.Treeview(frame_options)
    my_table['columns'] = ('NOMBRE', 'CORREO', 'CONTRASENA')
    my_table.column('#0', width=120, minwidth=60)
    my_table.column('NOMBRE', anchor=W, width=80)
    my_table.column('CORREO', anchor=W, width=150)
    my_table.column('CONTRASENA', anchor=W, width=90)
 
    my_table.heading('#0', text='ID_USUARIO', anchor=W)
    my_table.heading('NOMBRE', text='NOMBRE', anchor=W)
    my_table.heading('CORREO', text='CORREO', anchor=W)
    my_table.heading('CONTRASENA', text='CONTRASENA', anchor=W)


    cursor = connection.cursor()
    cursor.execute("SELECT NOMBRE, CORREO, CONTRASENA FROM TBL_SESION")
    registro = 0
    for fila in cursor:
        registro = registro + 1
        print(str(registro) +" - "+ str(fila))
        nombre = fila[0]
        correo = fila [1]
        contrasena = fila[2]
        my_table.insert(parent= '', index='end' , iid=registro, text=str(registro),
                values=(nombre, correo, contrasena))         
 
    connection.close()
    my_table.place(x=400,y=70)
  
button_leer = Button(frame_food, text="Leer", command=Leer ,font=("Calibri", "14", "bold"))
button_leer.place(x=180, y=230)



title1 = Label(frame_title, 
             text="NAVIPORTANS", 
              font=("Sketch 3D", "30"),
              justify=CENTER ,bg="#3CB371")
title1.place(x=25, y=10)
title2 = Label(frame_title, 
              text="Inicio Sesion, Los Campos son Obligatorios ", 
              font=("Franklin Gothic Medium Cond", "15"),justify=LEFT ,bg="#3CB371")
title2.place(x=25, y=50)
 
#my_table = ttk.Treeview(frame_options)
#my_table['columns'] = ('NOMBRE', 'CORREO', 'CONTRASENA')
#my_table.column('#0', width=120, minwidth=60)
#my_table.column('NOMBRE', anchor=W, width=80)
#my_table.column('CORREO', anchor=W, width=150)
#my_table.column('CONTRASENA', anchor=W, width=90)
 
#my_table.heading('#0', text='ID_USUARIO', anchor=W)
#my_table.heading('NOMBRE', text='NOMBRE', anchor=W)
#my_table.heading('CORREO', text='CORREO', anchor=W)
#my_table.heading('CONTRASENA', text='CONTRASENA', anchor=W)
 
#cursor = connection.cursor()
#cursor.execute("SELECT NOMBRE, CORREO, CONTRASENA FROM TBL_SESION")
#registro = 0
#for fila in cursor:
        #registro = registro + 1
        #print(str(registro) +" - "+ str(fila))
        #nombre = fila[0]
        #correo = fila [1]
        #contrasena = fila[2]
        #my_table.insert(parent= '', index='end' , iid=registro, text=str(registro),
                #values=(nombre, correo, contrasena))         
 
#connection.close()
  
#my_table.place(x=400,y=70)
 
window.mainloop()