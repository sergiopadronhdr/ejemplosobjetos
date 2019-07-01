# SERGIO PADRON CRUZ

class Base_Exponente(object):

    def get_base(self):
        return self.__base

    def set_base(self, valor1):
        self.__base = valor1

    def get_exponente(self):
        return self.__exponente

    def set_exponente(self, valor2):
        self.__exponente = valor2

    def pow(self, b, exp):
        if exp <= 0:
            return 1
        else:
            return b * pow(b, exp-1)