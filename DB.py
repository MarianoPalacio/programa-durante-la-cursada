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
	