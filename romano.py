# SERGIO PADRON CRUZ

class Entero_Romano(object):
    __entero = 0
    romano = ["I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX", "X"]

    def get_entero(self):
        return self.__entero

    def set_entero(self, valor):
        self.__entero = valor

    def convertir(self, valor):
        for i in range(len(self.romano)):
            if valor == i+1:
                print(self.romano[i])