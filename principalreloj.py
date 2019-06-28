from reloj import*

puntualidad = Reloj()
comprobar = False
while comprobar == False:
    hora = int(input("Dame la hora: "))
    minuto = int(input("Dame los minutos: "))
    segundo = int(input("Dame los segundos: "))
    if puntualidad.comprobar_hora(hora, minuto, segundo)== True:
        comprobar = True

puntualidad.set_hora(hora, minuto, segundo)
print(puntualidad.dame_hora())

