#Nivel 2 - Trbajo Práctico Final - POO
#Módulo Función de Validación
import re
from tkinter import messagebox

def validarcampo(self):
	D= dict(Titulo = self.Vale1.get())
	patron = re.compile("^[A-Za-z]+(?:[ _-][A-Za-z]+)*$")

	if str(patron.match(D['Titulo'])) == ('None'):
		return patron