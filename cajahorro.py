# Desarrollar un programa que conste de una clase padre Cuenta y dos subclases PlazoFijo y CajaAhorro.
# Definir los atributos titular y cantidad y un método para imprimir los datos en la clase Cuenta.
# La clase CajaAhorro tendrá un método para heredar los datos y uno para mostrar la información.
# La clase PlazoFijo tendrá dos atributos propios, plazo e interés. Tendrá un método para obtener el
# importe del interés (cantidad*interés/100) y otro método para mostrar la información, datos del
# titular plazo, interés y total de interés.
# Crear al menos un objeto de cada subclase.

class Cuenta(object):
    __titular = ""
    __cantidad = 0

    def getdatos(self):
        return self.__titular
        return self.__cantidad

    def setdatos(self, valor, valor2):
        self.__titular = valor
        self.__cantidad = valor2

    def imprimirdatos(self):
        print("Titular: " + self.__titular + ". Cantidad: " + str(self.__cantidad) + " €")

class PlazoAhorro(Cuenta):
    def aconsejar(self):
        print("Ahorrar es bien")

class PlazoFijo(Cuenta):
    __total = 0
    __plazo = 0
    __interes = 0

    def getdatos2(self):
        return self.__plazo
        return self.__interes

    def setdatos2(self, valor3, valor4):
        self.__plazo = valor3
        self.__interes = valor4

    def obtener_interes(self):
        self.__total = (self.__cantidad * self.__interes) / 100

    def mostrar_informacion(self):
        print("Titular: " + self.__titular)
        print("Plazo: " + str(self.__plazo))
        print("Interés: " + str(self.__interes))
        print("Total interés: " + str(self.__total))
