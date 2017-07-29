import sys

from diccionario import*
from contacto import*
from conjunto import*

class agendatelefonica:
	# Crea una agendatelefonica vacia 
	#
	# Parametros: -
	# Precondicion: True
	# Postcondicion: self.contactos es el diccionario que
	# guarda las claves y valores de la agendatelefonica
	def __init__(self):
		self.contactos = Diccionario(50)
	
	# Agrega un Contacto a la agendatelefonica
	#
	# Parametros: c - Contacto
	# Precondicion: True
	# Postcondicion: self.contactos es la agenda con el Contacto agregado
	def agregarContacto(self,c:Contacto):
		if not self.contactos.existe(c._nombre):
			self.contactos.agregar(c._nombre,c)
		else:
			print(c._nombre+" ya esta registrado en la Agenda")
	
	# Agrega un telefono a un Contacto existente
	#
	# Parametros: n - string; tlf - string
	# Precondicion: n existe en la agendatelefonica
	# Postcondicion: se agrega tlf al Conjunto de telefonos asociado a n
	def agregarTelefono(self,n:str,tlf:str):
		if not strBlanco(n):
			if self.contactos.existe(n):
				i=0
				while self.contactos._claves[i] != n:
					i += 1
				if not self.contactos._valores[i]._telefonos.pertenece(tlf):
					if self.contactos._valores[i]._telefonos._tam != self.contactos._valores[i]._telefonos._max:
						self.contactos._valores[i].agregarTelefono(tlf)
					else:
						print(n+' ya llego al límite maximo de telefonos')
				else:
					print(tlf+' ya esta asociado al Contacto '+n)
			else:
				print(n+' no esta registrado en la Agenda')
		else:
			print(n+' no es un nombre valido')
	# Elimina un Contacto de la agendatelefonica dado su nombre
	#
	# Parametros: nomb - string
	# Precondicion: nomb existe en la agendatelefonica
	# Postcondicion: nomb y su Contacto asociado se han eliminado de la agendatelefonica
	def eliminarContacto(self,nomb:str):
		if not strBlanco(nomb):
			if self.contactos.existe(nomb):
				self.contactos.eliminar(nomb)
			else:
				print(nomb+' no esta registrado en la Agenda')
		else:
			print(nomb+' no es un nombre valido')
	
	# Elimina un telefono dado el nombre del Contacto y el telefono
	#
	# Parametros: nomb - string; tlf - string
	# Precondicion: nomb existe en la Agenda y tlf pertenece al Conjunto
	# de telefonos del Contacto asociado a nomb
	# Postcondicion: tlf no pertenece al Conjunto de telefonos del Contacto
	# asociado a nomb
	def eliminarTelefono(self,nomb:str,tlf:str):
		if not strBlanco(nomb):
			if self.contactos.existe(nomb):
				i=0
				while nomb != self.contactos._valores[i]._nombre:
					i += 1
				if self.contactos._valores[i]._telefonos._tam == 1:
					print('Cada Contacto tiene que tener por lo menos un telefono asociado')
				else:
					if self.contactos._valores[i]._telefonos.pertenece(tlf):
						self.contactos._valores[i].eliminarTelefono(tlf)
					else:
						print(tlf+' no pertenece al Contacto '+nomb)
			else:
				print(nomb+' no esta registrado en la Agenda')
		else:
			print(nomb+' no es un nombre valido')
			
	# Busca el Contacto asociado a un nombre dado
	#
	# Parametros: nomb - string
	# Precondicion: nomb debe existir en la Agenda
	# Postcondicion: imprime el Contacto asociado a nomb
	def buscarContacto(self,nomb:str):
		if not strBlanco(nomb):
			if self.contactos.existe(nomb):
				self.contactos.buscar(nomb)
			else:
				print(nomb+" no esta registrado en la Agenda")
		else:
			print(nomb+' no es un nombre valido')
	
	# Importa los nombre y Contactos asociados de una Agenda a otra
	#
	# Parametros: d - agendatelefonica
	# Precondicion: True
	# Postcondicion: Los elementos de d.contactos cuyas claves
	# no se encuentren en la Agenda seran agregados a la Agenda
	# si caben en ella
	def importarAgenda(self,d):	
		self.contactos.unir(d.contactos)
	
	# Muestra la agendatelefonica por pantalla
	#
	# Parametros: -
	# Precondicion: True
	# Postcondicion: muestra por la salida estandar todos los nombres
	# de la agenda con su Contacto asociado
	def mostrarAgenda(self):
		for i in range(self.contactos._tam):
			print(self.contactos._claves[i]+": "+self.contactos._valores[i].__str__())