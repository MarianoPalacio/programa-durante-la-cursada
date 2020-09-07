#Nivel 2 - Unidad 4 - POO
#Módulo Base de Datos
import sqlite3

#Crear Base 
def crearbase():
	try:
		Base = sqlite3.connect('DBModuloUnidad4.db')

	except Error: pass

	finally:
		Base.close()

#Conexion de Base
def conectar():
	try:
		Base = sqlite3.connect('DBModuloUnidad4.db')
		return Base
	except Error: pass

#Tabla
def tabla():
	Base = sqlite3.connect('DBModuloUnidad4.db')
	ctabla = Base.cursor()
	ctabla.execute("CREATE TABLE producto (id integer PRIMARY KEY AUTOINCREMENT NOT NULL, Titulo Varchar(128) NOT NULL, Descripcion text NOT NULL)")
	Base.commit()

def create_connection():

    conn = None
    try:
        conn = sqlite3.connect('DBModuloUnidad4.db')
    except Error as e:
        print(e)

    return conn


def mostrar(tree):
    # limpieza de tabla 
    records = self.tree.get_children()
    for element in records:
        self.tree.delete(element)
    # Consiguiendo datos
    sql = 'SELECT * FROM producto ORDER BY id ASC'

    conn = create_connection()
    cur = conn.cursor()
    cur.execute(sql)

    resultado = cur.fetchall()

    for fila in resultado:
        print(fila)
        self.tree.insert('', 0, text = fila[0], values = (fila[1],fila[2]))

	
def eliminardatos(tree):
    id = self.tree.focus()
    a = tree.item(id)
    item = a['text']

    self.tree.delete(id)
    
    conn = create_connection()
    cur = conn.cursor()
    sql = "DELETE from producto where Id =" + str(item)
    cur.execute(sql)
    conn.commit()   
    
    mostrar(self.tree)