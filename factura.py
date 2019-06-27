# SERGIO PADRON CRUZ

class Factura:
    __tasa = 19

    def __init__(self, unidad, precio):
        self.unidad = unidad
        self.precio = precio

    def a_pagar(self):
        total = self.unidad * self.precio
        impuesto = total * Factura.__tasa / 100
        return(total + impuesto)

compra1 = Factura(12, 110)
print(compra1.unidad)
print(compra1.precio)
print(compra1.a_pagar(), "euros")
print(Factura.__tasa)   # Error:

# AttributeError: tyoe object "Factura" has no attribute "__tasa"