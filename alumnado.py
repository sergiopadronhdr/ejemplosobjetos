# El alumnado tendrá que realizar un programa que conste de una clase llamada Alumno
# que tenga como atributos el nombre y la nota del alumno. Definir los métodos para
# inicializar sus atributos, imprimirlos y mostrar un mensaje con el resultado de la
# nota y si ha aprobado o no.

class Alumnado(object):
    __nombre = ""
    __nota = 0

    def getdatos(self, nombre, nota):
        return self.__nombre
        return self.__nota

    def setdatos(self, valor, valor2):
        self.__nombre = valor
        self.__nota = valor2

    def notamedia(self, valor2, valor):
        if valor2 < 5:
            print(valor + " tiene una nota de " + str(valor2) + " y está SUSPENDIDO")
        else:
            print(valor + " tiene una nota de " + str(valor2) + " y está APROBADO")