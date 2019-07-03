from alumnado import *

dato = Alumnado()
alum = input("Introduzca el nombre del alumno: ")
media = int(input("Introduzca la nota del alumno: "))
dato.setdatos(alum, media)
dato.notamedia()
