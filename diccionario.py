import sys
from contacto import*
from conjunto import*

class Diccionario:
	# Crea un diccionario vacio con tamaño máximo m
	#
	# Parametros: m - entero
	# Precondicion: m > 0
	# Postcondicion: Se ha creado un Diccionario vacio de tamaño maximo m
	def __init__(self, m:int):
		if m > 0:
			self._max = m
			self._tam = 0
			self._claves = [None for x in range(self._max)]
			self._valores = [None for x in range(self._max)]
		else:
			print("Error, el tamaño del diccionario debe ser mayor que cero")
			sys.exit(1)
			
	# Agrega una clave y valor al diccionario
	#
	# Parametros: clave - string; valor - Contacto
	# Precondicion: la clave no pertenece al diccionario
	# Postcondicion: la clave y el valor se agregan al final
	# del Diccionario, y se aumenta el tamaño del diccionario en 1
	def agregar(self, clave:str, valor:Contacto):
		if clave not in self._claves and self._tam != self._max:
			self._claves[self._tam] = clave
			self._valores[self._tam] = valor
			self._tam = self._tam + 1
		else:
			print(clave+' ya esta en el diccionario')
			
	# Elimina una clave del diccionario
	#
	# Parametros: clave - string
	# Precondicion: clave pertenece al diccionario
	# Postcondicion: el par clave,valor se ha eliminado
	# del diccionario y su tamaño se reduce en 1
	def eliminar(self, clave:str):
		if self.existe(clave):
			i = 0
			while self._claves[i] != clave:
				i = i + 1
			self._claves[i] = self._claves[self._tam - 1]
			self._valores[i] = self._valores[self._tam - 1]
			self._tam = self._tam - 1
		else:
			print(clave+' no esta en el diccionario')
			
	# Busca un elemento en el diccionario
	#
	# Parametros: clave - string
	# Precondicion: La clave existe en el diccionario
	# Postcondicion: Existe un valor asociado a la clave dada
	def buscar(self, clave:str):
		if self.existe(clave):
			i = 0
			while self._claves[i] != clave:
					i = i + 1
			print(self._valores[i])
		else:
			print(clave+' no esta en el diccionario')
			
	# Imprime el diccionario por la salida estándar
	#
	# Parametros: -
	# Precondicion: True
	# Postcondicion: Imprime por la salida estandar todos los
	# pares clave, valor que contiene el diccionario
	def mostrar(self):
		for i in range(self._tam):
			print(self._claves[i],self._valores[i])
			
	# Determina si existe un elemento en el diccionario.
	#
	# Parametros: clave - string
	# Precondicion: True
	# Postcondicion: La clave existe en el diccionario 
	def existe(self, clave):
		hola = False
		for i in range(self._tam):
			if self._claves[i] == clave:
				hola = True
		return hola
		
	# Realiza la union de dos diccionarios
	#
	# Parametros: d - Diccionario
	# Precondicion: True
	# Postcondicion: Los elementos (clave, valor) del diccionario de entrada "d"
	# cuyas claves no se encuentren en el diccionario seran agregados
	# al diccionario si caben en él
	def unir(self, d):
		if self._tam == self._max:
			print('El diccionario se quedo sin espacio')
		elif self._tam < self._max:
			for i in range(d._tam):
				if self._claves[i] == d._claves[i]: 
					print(d._claves[i]+'ya esta en el diccionario')
				elif self._claves[i] != d._claves[i]:
					self.agregar(d._claves[i], d._valores[i])
					if self._tam == self._max:
						break
						
	# Retorna una representacion en string del Diccionario
	def __str__(self):
		msg = ""
		for i in range(self._tam):
			msg +=  self._claves[i]+" "+self._valores[i]+"\n"
		return msg