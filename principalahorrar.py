from cajahorro import*

dato = Cuenta()
titular = input("Introduza el nombre del titular: ")
cantidad = int(input("Introduzca la cantidad a ingresar: "))
dato.setdatos(titular, cantidad)
print(dato.imprimirdatos())

dato2 = PlazoFijo()
plazo = int(input("Introduzca el número de plazos: "))
interes = int(input("Introduzca el interés: "))
dato2.setdatos2(plazo, interes)
dato2.obtener_interes()
print(dato2.mostrar_informacion())

dato3 = PlazoAhorro()
dato3.aconsejar()