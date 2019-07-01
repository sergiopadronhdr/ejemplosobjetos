# SERGIO PADRÓN CRUZ
# PRÁCTICA "CLASES EN PYTHON"

class Libro(object):
    isbn = ""
    titulo = ""
    autor = 0

    def __init__(self, autor, titulo, isbn):
        self.autor = autor
        self.titulo = titulo
        self.isbn = isbn

    def get_autor(self):
        return self.__autor

    def set_autor(self, valor1):
        self.__autor = valor1

    def get_titulo(self):
        return self.__titulo

    def set_titulo(self, valor2):
        self.__titulo = valor2

    def get_isbn(self):
        return self.__isbn

    def set_isbn(self, valor3):
        self.__isbn = valor3

    def isbn10(self, isbn):
        while len(isbn) != 10:
            return False
        else:
            d1 = isbn[0] * 1
            d2 = isbn[1] * 2
            d3 = isbn[2] * 3
            d4 = isbn[3] * 4
            d5 = isbn[4] * 5
            d6 = isbn[5] * 6
            d7 = isbn[6] * 7
            d8 = isbn[7] * 8
            d9 = isbn[8] * 9
            if isbn[9] == "X":
                d10 = 10
            else:
                d10 = isbn[9]
            d10 = d10 * 10
            d11 = (d1 + d2 + d3 + d4 + d5 + d6 + d7 + d8 + d9 + d10)
            num = d11 % 11
            if num == 0:
                return True
            else:
                return False

    def isbn13(self, isbn):
        while len(isbn) != 13:
            return False
        else:

            sumaImpar = (isbn[0] + isbn[2] + isbn[4] + isbn[6] + isbn[8] + isbn[10])
            sumaPar = (isbn[1] + isbn[3] + isbn[5] + isbn[7] + isbn[9] + isbn[11])
            suma = sumaImpar + (sumaPar * 3)
            num = suma % 10
            if isbn[12] == 0:
                d13 = 0
            else:
                d13 = 10 - num

