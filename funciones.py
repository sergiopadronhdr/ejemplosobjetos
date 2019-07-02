def saludar():
    print("Hola, que tal?")

def funcion(nombre, apellido):
    nombre_completo = nombre + apellido
    print(nombre_completo)
# RETORNO
def avecesar(name, menssage='¡Ave, César!'):
    print(menssage, name)
# RECURSIVIDAD
def jugar(intento=1):
    respuesta = input("¿De qué color es una naranja? ")
    if respuesta != "naranja":
        if intento < 3:
            print("\nFallaste! Inténtalo de nuevo")
            intento += 1
            jugar(intento) # Llamada recursiva
        else:
            print("\nPerdiste!")
    else:
        print("\nGanaste!")