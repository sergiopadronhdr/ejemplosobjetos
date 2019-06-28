from herencia import*

Flipper = Delfin()
Flipper.set_peso(1800)
print("Flipper Pesa " + str(Flipper.get_peso()) + " kg")
print("Flipper " + Flipper.nadar())

Chueca = Oviparo()
Chueca.set_peso(1)
print("Chueca Pesa " + str(Chueca.get_peso()) + " kg")
print("Chuca " + Chueca.comer() + " y " + Chueca.ponerHuevos())

Toby = Perro()
print("Toby " + Toby.comer() + ", " + Toby.ladrar() + " y " + Toby.correr())
