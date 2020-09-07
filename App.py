#App principal
#Nivel 2 - Trbajo Práctico Final - POO
from tkinter import *
from Temas import *
from tkinter import messagebox
from tkinter import ttk
import Validar as MV
import DB as MDB
import sqlite3
import time


#Clase administradora va a contener etiquetas, campos para ingresar texto, marco ventana (render),reloj, treeview y botones nuevos 

class Administradora(object):

	def __init__(self,):
		
		#Ventana
		self.render = ventana
		self.render.title('TPF')
		self.render.resizable(width=False, height=False)
		self.render.iconbitmap('utn1.ico')
		self.render.config(bg='lightgrey')
		
		#Variable para campos
		self.Vale1= StringVar()
		self.Vale2 = StringVar()
		
		#Etiquetas y Campos de entrada
		self.reloj=Label(ventana, bg='lightgrey', font=('times', 10, 'bold'))
		self.reloj.grid(row=13, column=2 ,pady=10, padx=60)

		self.Saludo = Label(ventana, text='Bienvenidos', bg='aquamarine1', fg='black', font=('Arial', 10), width=25)
		self.Saludo.grid(row=0, column=0, columnspan=6, sticky=W+E)

		self.Titulo = Label(ventana, text='Título', bg='lightgrey', font=('Arial', 8))
		self.Titulo.grid(row=1, column=0,sticky=W)
		self.Descripcion = Label(ventana, text='Descripción', bg='lightgrey', font=('Arial', 8))
		self.Descripcion.grid(row=2, column=0, sticky=W)

		self.e1 = Entry(self.render, textvariable=self.Vale1, width=20)
		self.e1.grid(row=1, column=2, sticky=N) #Entrada de título

		self.e2 = Entry(self.render, textvariable=self.Vale2, width=20)
		self.e2.grid(row=2, column=2, sticky=N) #Entrada de descripción

		#Segmento nuevo con grid o con pack para uni 4/ 
		self.segmento = Frame(self.render, width=210, height=30, relief=RAISED, borderwidth=2)
		self.segmento.grid(row=7, column=0, columnspan=6)    

		self.titulo_temas = Label(self.render, fg='black', text= 'Personalizar', font=('Arial', 10))
		self.titulo_temas.grid(row=7, column=0, columnspan=6)

		self.segmento2 = Frame(self.render, width=210, height=20, relief=RAISED, borderwidth=2)
		self.segmento2.grid(row=8, column=0, columnspan=6)

		#Treeview
		self.tree = ttk.Treeview(ventana)
		self.tree["columns"] = ("col1", "col2")
		self.tree.column("#0", width=50, minwidth=50, anchor=W)
		self.tree.column("col1", width=80, minwidth=80)
		self.tree.column("col2", width=80, minwidth=80)
		self.tree.grid(column=0, row=3, columnspan=6)

		self.tree.heading("#0",text="ID",anchor=CENTER)
		self.tree.heading("col1", text = 'Título', anchor = CENTER)
		self.tree.heading("col2", text = 'Descripción', anchor = CENTER)

		#BOTONES NUEVO SEGMENTO
		self.cambiarfondo = IntVar()
		        
		self.botontema = Radiobutton(self.segmento2, text='Alice', variable=self.cambiarfondo, indicatoron=1, value=1, command=lambda:eleccion_tema(self.render, self.cambiarfondo.get()))
		self.botontema.grid(row=8, column=0)

		self.botontema2 = Radiobutton(self.segmento2, text='Aqua', variable=self.cambiarfondo, indicatoron=1, value=2, command=lambda:eleccion_tema(self.render, self.cambiarfondo.get()))
		self.botontema2.grid(row=9, column=0)

		self.botontema3 = Radiobutton(self.segmento2, text='BViolet', variable=self.cambiarfondo, indicatoron=1, value=3, command=lambda:eleccion_tema(self.render, self.cambiarfondo.get()))
		self.botontema3.grid(row=10, column=0)

		self.botontema4 = Radiobutton(self.segmento2, text='Burly', variable=self.cambiarfondo, indicatoron=1, value=4, command=lambda:eleccion_tema(self.render, self.cambiarfondo.get()))
		self.botontema4.grid(row=11, column=0)


		#Reloj
		def hora():
			hora_actual=time.strftime('%H:%M:%S') 
			self.reloj.config(text=hora_actual, bg="black", fg="green", font="Arial 12 bold")
			self.reloj.after(1000, hora)

		#Metodos, Alta, Mostrar datos en Base de datos y Crear basa
		def CrearDB():
			hora()
			MDB.crearbase()
			MDB.conectar()
			MDB.tabla()

		def mostrar(self):
			records = self.tree.get_children()
			for element in records:
				self.tree.delete(element)
			# Consiguiendo datos
			sql = 'SELECT * FROM producto ORDER BY id ASC'

			conn = MDB.create_connection()
			cur = conn.cursor()
			cur.execute(sql)

			resultado = cur.fetchall()

			for fila in resultado:
				self.tree.insert('', 0, text = fila[0], values = (fila[1],fila[2]))
			
		def dardealta():
			hora()
			MDB.create_connection()
			Base = sqlite3.connect('DBModuloUnidad4.db')
			Base = MDB.conectar()
			ctabla = Base.cursor()
			cb = "INSERT INTO producto VALUES (NULL, ?, ?)"
			datos = (self.Vale1.get(), self.Vale2.get())
			ctabla.execute(cb, datos)
			Base.commit()
			self.e1.delete(0, END)
			self.e2.delete(0, END)
			mostrar(self)
	
		def Borrar():
			id = self.tree.focus()
			a = self.tree.item(id)
			item = a['text']
			
			self.tree.delete(id)
			    
			conn = MDB.create_connection()
			cur = conn.cursor()
			sql = "DELETE from producto where Id =" + str(item)
			cur.execute(sql)
			conn.commit()
			messagebox.showinfo(message='''Registro eliminado con éxito''', title="Información")
			mostrar(self)


		def Ayuda():
			messagebox.showinfo(message='''Hola, antes de comenzar no olvides Crear tu Base de Datos.
Recordá que en caso de error podes eliminar el registro, seleccionando el mismo y haciendo click en el botón Borrar.''', title="Ayuda")

		#BOTONES
		BotonAlta = Button(ventana, text= 'Alta', command=dardealta, bg='lightgrey', font=("Arial", 9), width=4, height=1).grid(row=2, column=4, sticky=N)
		BotonBase = Button(ventana, text=' DB ', command=CrearDB, bg='lightgrey', font=("Arial", 9), width=4, height=1).grid(row=14, column=0, sticky=N)
		BotonBorrar = Button(ventana, text='Borrar', command=Borrar, bg='lightgrey', font=("Arial", 9), width=4, height=1).grid(row=14, column=4, sticky=N)
		BotonAyuda = Button(self.render, text='Ayuda', command=Ayuda, bg='lightgrey', font=("Arial", 9), width=6, height=1).grid(row=14, column=2, sticky=N)
		

if __name__ == '__main__':
	ventana = Tk()
	objeto = Administradora()
	ventana.mainloop

	mainloop()


