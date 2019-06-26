# Escribir una clase en python que convierta un número entero a número romano

class Romano(object):
    entero = 0
    romano = " "

    def __init__(self, valor):
        self.entero = valor

    def getentero(self): # Obtener valor
        return self.entero

    def setentero(self, valor):
        self.entero = valor

    def cambiar(self):
        if self.entero == 10:
            self.romano ="X"
        return self.getentero()

