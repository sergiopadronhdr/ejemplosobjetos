# OBJETOS

# Propiedades
class Antena(object):
    color = ""
    longitud = ""

class Pelo(object):
    color = ""
    textura = ""

class Ojo(object):
    forma = ""
    color = ""
    tamanio = ""

class Objeto(object):
    color = ""
    tamanio = ""
    aspecto = ""
    antenas = Antena()  # propiedad compuesta por el objeto objeto Antena
    ojos = Ojo()        # propiedad compuesta por el objeto objeto Ojo
    pelos = Pelo()      # propiedad compuesta por el objeto objeto Pelo

# Métodos
class Objeto(object):
    color = "verde"
    tamanio = "grande"
    aspecto = "feo"
    antenas = Antena()
    ojos = Ojo()
    pelos = Pelo()

    def flotar(self):
        return True

class Dedo(object):
    longitud = ""
    forma = ""
    color = ""
    def flotar(self):
        return True
    def saltar(self):
        return False
class Pie(object):
    forma = "chunga"
    color = "paliducho"
    dedos = Dedo()
    def OlerMal(self):
        return ("Apestas!")

# NuevoObjeto si hereda de otra clase: Objeto
class NuevoObjeto(Objeto):
    pie = Pie()

    def saltar(self):
        return False