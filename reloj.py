# SERGIO PADRÓN CRUZ

class Reloj(object):
    hora = 0
    minuto = 0
    segundo = 0

    def comprobar_hora(self, hora, minuto, segundo):
        if 0 <= hora <= 23 and 0 <= minuto <= 59 and 0 <= segundo <= 59:
            return True
        else:
            return False

    def set_hora(self, hora, minuto, segundo):
        self.hora = hora
        self.minuto = minuto
        self.segundo = segundo

    def dame_hora(self):
        return str(self.hora) + ":" + str(self.minuto) + ":" + str(self.segundo)
