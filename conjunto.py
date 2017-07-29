import sys

class Conjunto:
	# Crea un Conjunto de tamaño maximo m
	#
	# Parametros: m - int
	# Precondicion: m > 0
	# Postcondicion: Se ha creado un Conjunto vacio de tamaño maximo m
	def __init__(self, m: int):
		if m > 0:
			self._max = m
			self._tam = 0
			self._elems = [None for i in range(self._max)]
		else:
			print('Error en el tamaño maximo del conjunto, debe ser mayor que 0')
			sys.exit(1)
	
	# Agrega un elemento dado al conjunto
	#
	# Parametros: elem - string
	# Precondicion: elem no pertenece al Conjunto
	# Postcondicion: agrega a elem al final del Conjunto y aumenta su tamaño en 1 
	def agregar(self, elem: str):
		hola = self.pertenece(elem)
		if hola == False and self._max != self._tam:
			self._elems[self._tam] = elem
			self._tam = self._tam + 1
		else:
			print(elem+' ya pertenece al conjunto')
			
	# Elimina un elemento dado del conjunto
	#
	# Parametros: elem - string
	# Precondicion: elem pertenece al Conjunto
	# Postcondicion: elem no pertenece al Conjunto y su tamaño se reduce en 1
	def eliminar(self, elem: str): 
		if self.pertenece(elem):
			i = 0
			while self._elems[i] != elem:
				i = i + 1
			self._elems[i] = self._elems[self._tam-1]
			self._tam = self._tam - 1
		else:
			print(elem+' no esta en el conjunto')
	
	# Dice si un elemento dado pertenece al conjunto
	#
	# Parametros: elem - string
	# Precondicion: True
	# Postcondicion: elem pertenece al Conjunto
	def pertenece(self, elem: str)->bool:
		return any(elem == self._elems[i] for i in range(self._tam))
		
	# Retorna una representacion en string del Conjunto
	def __str__(self):
		msg = ""
		for i in range(self._tam):
			msg += self._elems[i]+","
		msg = "["+msg[:-1]+"]"
		return msg
