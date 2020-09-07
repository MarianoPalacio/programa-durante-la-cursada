#Nivel 2 - Trbajo Práctico Final - POO
#Módulo Función de Validación
import re

def validarcampo(e1, Label, ventana, W,):
	D= dict(Titulo = e1.get())
	patron = re.compile("^[A-Za-z]+(?:[ _-][A-Za-z]+)*$")

	if str(patron.match(D['Titulo'])) == ('None'):
		 Validar = Label(ventana, text='El Dato ingresado no es Válido', fg='red')
		 Validar.grid(row=14, column=0, sticky= W)

	else:
		Validar = Label(ventana, text='  El Dato ingresado es Válido ', fg='green')
		Validar.grid(row=14, column=0, sticky= W)
		 