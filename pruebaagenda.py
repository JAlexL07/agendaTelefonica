import sys
from agenda_telefonica import*

if __name__ == "__main__":
	print("Agenda_Telefónica")
	print("Cliente de Pruebas")
	print("Autores: Jean Alexander #12-10848 \nDiego Pedroza #12-11281\n")

	
	a="\n****\n"
	j=Contacto("Jean","02127317166")
	d=Contacto("Diego","02127302592")
	
	### Se crea una agenda vacía
	print("Se crea una agenda vacia")
	agem=agendatelefonica()
	agem.mostrarAgenda()
	print(a)
	
	#Se agregan contactos
	print("Se agregan contactos")
	agem.agregarContacto(j)
	agem.agregarContacto(d)
	agem.mostrarAgenda()
	print(a)
	
	#Se agrega telefonos de Jean
	print("Se agrega telefonos a un contacto")
	agem.agregarTelefono("Jean","02123721221")
	agem.agregarTelefono("Jean","04212928219")
	agem.agregarTelefono("Jean","02012212121")
	agem.agregarTelefono("Jean","02012212122")
	agem.agregarTelefono("Jean","02012212125")
	agem.mostrarAgenda()
	
	print("*\n")
	#Se trata de agregar un número a un contacto que no existe
	print("Se trata de agregar un número a un contacto que no existe")
	agem.agregarTelefono("J ean","323212")
	agem.mostrarAgenda()
	
	print(a)
	

	#Busca un contacto que existe
	print("Busca un contacto que existe")
	agem.buscarContacto("Jean")
	print(a)
	#Busca un contacto que no existe
	print("Busca un contacto que no existe")
	agem.buscarContacto("Juan")
	print(a)

	#Elimina un telefono que existe de un contacto existente
	print("Elimina un telefono que existe de un contacto existente")
	print("Jean"+", "+"04212928219\n")
	agem.eliminarTelefono("Jean","04212928219")
	agem.mostrarAgenda()
	print(a)
	
	#Elimina un telefono que no existe en un contacto que si
	print("Elimina un telefono que no existe en un contacto que si")
	agem.eliminarTelefono("Jean","021237212222")
	agem.mostrarAgenda()
	print(a)
	
	#Elimina un telefono en un contacto que no existe
	print("Elimina un telefono en un contacto que no existe")
	agem.eliminarTelefono("Juan","021237212222")
	agem.mostrarAgenda()
	print(a)	
	
	#Se Elimina todos los telefonos de Jean uno a uno
	print("Se Elimina todos los telefonos de Jean uno a uno")
	agem.mostrarAgenda()
	agem.eliminarTelefono("Jean","02127317166")
	agem.eliminarTelefono("Jean","02012212121")
	agem.eliminarTelefono("Jean","02123721221")
	agem.eliminarTelefono("Jean","02012212122")
	agem.mostrarAgenda()

	print(a)
	
	
	#Vuelvo a agrega telefonos a Jean
	print("Vuelvo a agrega telefonos a Jean")
	agem.agregarTelefono("Jean","02123721221")
	agem.agregarTelefono("Jean","04212928219")
	agem.agregarTelefono("Jean","02012212121")
	agem.agregarTelefono("Jean","02012212127")
	agem.agregarTelefono("Jean","02012212125")
	agem.agregarTelefono("Jean","02127317166")
	agem.mostrarAgenda()
	print(a)


	#Elimino un contacto
	print("Elimino un contacto:")
	agem.eliminarContacto("Jean")
	agem.mostrarAgenda()
	print(a)

	#Vuelvo a agregar un contacto que borré
	print("Vuelvo a agregar un contacto que borré")
	agem.agregarContacto(j)
	agem.mostrarAgenda()
	print(a)
	
	#Elimino un Contacto
	print("Elimino un Contacto que no existe")
	agem.eliminarContacto("Juan")
	agem.mostrarAgenda()
	print(a)
	
	#Importar agenda
	print("Importar agenda:")
	print()
	##Agenda1 antes de la importación
	print("Agenda1 antes de la importación:")
	w=Contacto("Princesa","01212122121")
	ag=agendatelefonica()
	ag.agregarContacto(w)
	ag.mostrarAgenda()
	print(a)
	
	##Importando agenda
	print("Importando agenda")
	ag.importarAgenda(agem)
	ag.mostrarAgenda()
	print(a)
	
	##Si cambio la agenda que importé
	print("Si cambio la agenda que importé no debería cambiar Agenda1:\n")
	n=Contacto("Luna","0201221211")
	agem.agregarContacto(n)
	print("Agenda0:")
	agem.mostrarAgenda()
	print("\nLuego\n")
	ag.mostrarAgenda()
	
	# Agregando más telefonos
	print("Agregando más teléfonos")
	print("Número inválido")
	agem.agregarTelefono("Luna","020a12212121")
	print(a)
	
	print("Números correctos")
	agem.agregarTelefono("Luna","02012212127")
	agem.agregarTelefono("Luna","02012212125")
	agem.mostrarAgenda()
	print("\n")
	ag.agregarTelefono("Princesa","0212212212")
	ag.agregarTelefono("Princesa","0212121221")
	ag.agregarTelefono("Diego","121221211")
	ag.mostrarAgenda()
	print(a)
	
	# Eliminando Contactos y Números
	print("Eliminando Contactos  y Números")
	agem.eliminarContacto("Luna")
	agem.mostrarAgenda()
	print("\n")
	ag.agregarTelefono("Luna","02012212127")
	ag.eliminarTelefono("Jean","04212928219")
	
	print("\n")
	agem.mostrarAgenda()
	print("\n")
	ag.mostrarAgenda()
	
	
	
	print("\nFin")
	
	

