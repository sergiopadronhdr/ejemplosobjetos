# SERGIO PADRON

class Animal(object):
    __peso = 0
    def get_peso(self):
        return self.__peso
    def set_peso(self, peso):
        self.__peso = peso
    def comer(self):
        return ("Puede comer")
    def morir(self):
        return ("Todos mueren")

class Oviparo(Animal):
    def ponerHuevos(self):
        return ("Pone huevos")

class Mamifero(Animal):
    sangreCaliente = True
    def parir(self):
        return ("Puede parir")
    def amamantar(self):
        return ("Puede amamantar")

class Delfin(Mamifero):
    def nadar(self):
        return ("Puede nadar")

class Perro(Mamifero):
    colorPelo = ""
    def ladrar(self):
        return ("Puede ladrar")
    def correr(self):
        return ("Puede correr")