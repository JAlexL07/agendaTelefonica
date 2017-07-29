import sys
from conjunto import*

#Determina si s es vacio
def strBlanco(s:str)->bool:
	return s=='' 

#Determina si s esta compuesto unicamente por numeros
def strNumerico(s:str)->bool:
	return s.isdigit()

class Contacto:
	# Crea un Contacto dados un nombre y un telefono
	# 
	# Parametros: n - str; tlf - str
	# Precondicion: n es no vacio y tlf son unicamente numeros
	# Postcondicion: n es el nombre del Contacto y tlf su telefono
	def __init__(self,n:str,tlf:str):
		if not strBlanco(n):
			if strNumerico(tlf):
				self._nombre=n
				self._telefonos=Conjunto(5)
				self._telefonos.agregar(tlf)
			else:
				print(tlf+' no es un telefono valido')
		else:
			print(n+' es un nombre no valido')
	
	# Muestra el nombre del Contacto
	#
	# Parametros: -
	# Precondicion: True
	# Postcondicion: self._nombre es el nombre del Contacto
	def obtenerNombre(self)->str:
		return self._nombre
	
	# Muestra los telefonos asociados al Contacto
	#
	# Parametros: -
	# Precondicion: True
	# Postcondicion: self._telefonos es el Conjunto de los telefonos del Contacto
	def obtenerTelefonos(self)->Conjunto:
		return self._telefonos
	
	# Elimina un telefono dado del Contacto
	#
	# Parametros: tlf - string
	# Precondicion: tlf pertenece al Conjunto de telefonos del Contacto
	# Postcondicion: tlf no pertenece al Conjunto de telefonos del Contacto
	def eliminarTelefono(self,tlf:str):
		if strNumerico(tlf):
			if tlf in self._telefonos._elems:
				self._telefonos.eliminar(tlf)
			else:
				print("El telefono no pertenece al Contacto")
		else:
			print(tlf+' no es un telefono valido')
			
	# Agrega un telefono dado al Contacto
	#
	# Parametros: tlf - string
	# Precondicion: tlf no pertenece al Conjunto de telefonos del Contacto
	# Postcondicion: tlf pertenece al Conjunto de telefonos del Contacto
	def agregarTelefono(self,tlf:str):
		if strNumerico(tlf):
			if not self._telefonos.pertenece(tlf):
				self._telefonos.agregar(tlf)
			else:
				print(tlf+" ya esta asociado al Contacto")
		else:
			print(tlf+" no tiene un formato correcto")
			
	# Retorna una representacion en string del Contacto
	def __str__(self):
		msg,msg2 = "",""
		msg =  self._nombre
		msg2 = self._telefonos.__str__()
		return msg+"->"+msg2