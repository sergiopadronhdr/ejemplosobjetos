# Calcular Salario

monto_bruto = 175
tasa_interes = 12
monto_interes = monto_bruto * tasa_interes / 100
tasa_bonificacion = 5
importe_bonificacion = monto_bruto * tasa_bonificacion / 100
monto_neto = (monto_bruto - importe_bonificacion) + monto_interes
print(monto_neto)

# Operadores

# Símbolo Significado Ejemplo Resultado
"""+ Suma             a = 10 + 5 a es 15
   - Resta            a = 12 - 7 a es 5
   - Negación         a = -5 a es -5
   * Multiplicación   a = 7 * 5 a es 35
   ** Exponente       a = 2 ** 3 a es 8
   / División         a = 12.5 / 2 a es 6.25
   // División entera a = 12.5 / 2 a es 6.0
   % Módulo           a = 27 % 4 a es 3"""

# Operadores relacionales (de comparación)

"""Símbolo     Significado         Ejemplo            Resultado

     ==         Igual que          5 == 7              Falso

     !=       Distinto que rojo    != verde           Verdadero

     <          Menor que          8 < 12             Verdadero

     >         Mayor que           12 > 7              Falso

     <=       Menor o igual que     12 <= 12           Verdadero

     >=       Mayor o igual que     4 >= 5               Falso"""

# Operadores Lógicos

"""Operador            Ejemplo               Resultado*
   and (y)        5 == 7 and 7 < 12            0 y 0      Falso

                  9 < 12 and 12 > 7            1 y 1    Verdadero

                  9 < 12 and 12 > 15           1 y 0      Falso

   or (o)         12 == 12 or 15 < 7           1 o 0    Verdadero

                  7 > 5 or 9 < 12              1 o 1    Verdadero

   xor            4 == 4 xor 9 > 3             1 o 1      Falso

(o excluyente)    4 == 4 xor 9 < 3             1 o 0    Verdadero"""

# Comentarios

# Esto es un comentario de una sola línea
mi_variable = 15
"""Y este es un comentario
de varias líneas"""
mi_variable = 15
mi_variable = 15  # Este comentario es de una línea también

# TODO

"""En los comentarios, pueden incluirse palabras que nos ayuden a identificar además, el
subtipo de comentario:"""
# TODO esto es algo por hacer
# FIXME esto es algo que debe corregirse
# XXX esto también, es algo que debe corregirse (este no funciona)

# Tuplas
"""Una tupla es una variable que permite almacenar varios datos inmutables (no pueden
ser modificados una vez creados) de tipos diferentes:"""
mi_tupla = ('cadena de texto', 15, 2.8, 'otro dato', 25)  # Son valores inmutables estan entre paréntesis

"""Se puede acceder a cada uno de los datos mediante su índice correspondiente, siendo 0
(cero), el índice del primer elemento:"""
print(mi_tupla[1])  # Salida: 15

# STR

mi_variable = 15
print("Texto y ", mi_variable)  # No funciona si no tiene str, probar en console.
print("Texto y " + str(mi_variable))  # Usa str para poder concatenar
print("Hola" + " adios " + "que tal")  # Concatenar 3 palabras
print("Hola" " adios " "pepe")  # Tambien concatena sin el +

# Escape

print("C:\algun\nombre")  # Este tento no sale bien, comprobar en la consola
print("C:\\algun\\nombre")  # Se soluciona añadiendo otra "\"

# Escape 2

# Hay varias maneras de usar los saltos de línea,

print(
    "Uso: algo [OPTIONS]\n \t \t \t -h \t \t \t Muestra el mensaje de uso \n \t \t \t -H nombrehost \t \t \t Nombre del host al cual conectarse")

print("""Uso: algo [OPTIONS]
       -h            Muestra el mensaje de uso 
       -H nombrehost               Nombre del host al cual conectarse""")

# Rebanar

palabra = 'Python'

palabra[0]  # caracter en la posición 0

print(palabra[0:2])
print(palabra[-1])  # va a la última letra en este caso mostrará por consola "n"
print(palabra[-2:])  # Para recorrer la palabra, pero no le puedes decir donde para.

print("P", palabra[1:])  # Sale por consola P ython
print(palabra[:2] + "py")  # Sale PyPy jijijijijijiji

# Lista

s = "supercalifragilisticoespialidoso"
print(len(s))  # Recorrer la cadena

cuadrados = [1, 4, 9, 16, 25]
print(cuadrados[-3:])  # Sale [9, 16, 25]

print(cuadrados + [36, 49, 64, 81, 100])

# Bobas

mi_lista = ['cadena de texto', 15, 2.8, 'otro dato', 25]

# A las listas se accede igual que a las tuplas, por su número de índice:
print(mi_lista[1])  # Salida: 15
print(mi_lista[1:4])  # Devuelve: [15, 2.8, 'otro dato']
print(mi_lista[-2])  # Salida: otro dato

"""Las lista NO son inmutables: permiten modificar los datos una vez creados:
mi_lista[2] = 3.8 # el tercer elemento ahora es 3.8"""

# Las listas, a diferencia de las tuplas, permiten agregar nuevos valores:
mi_lista.append('Nuevo Dato')

# Diccionario

"""Mientras que a las listas y tuplas se accede solo y únicamente por un número de índice,
los diccionarios permiten utilizar una clave para declarar y acceder a un valor:"""

mi_diccionario = {'clave_1': 1, 'clave_2': 2, 'clave_7': 7}  # Los numeros son los valores.

print(mi_diccionario['clave_2'])  # Salida: 2

# Un diccionario permite eliminar cualquier entrada:

del (mi_diccionario['clave_2'])  # Elimina un elemento de la lista
print(mi_diccionario)  # al haber eliminado saldrá solo por la lista {'clave_1': 1, 'clave_7': 7}

# Al igual que las listas, el diccionario permite modificar los valores

mi_diccionario['clave_1'] = 'Nuevo Valor'

print(mi_diccionario)  # Al darle nuevo valor saldrá por consola {'clave_1': 'Nuevo Valor', 'clave_7': 7}

# -------------------------------Identación--------------------------------

"""Una identación de 4 (cuatro) espacios en blanco, indicará que
las instrucciones identadas, forman parte de una misma
estructura de control.!!!!!!!!!!!!ALERTA!!!!!!!!!! ""SI USAMOS TABULADOR NO FUNCIONA""!!!!!!!!!!!!ALERTA!!!!!!!!!!"""


def mover():
    nom = 3
    nom2: int = 4
    print(nom, nom2)


# If, Elif, Else

semaforo = "verde"
if semaforo == "verde":
    print("Cruzar la calle")
elif (semaforo == "azul") and (semaforo == "blanco"):
    print("Esperar")

# While

"""Este bucle, se encarga de ejecutar una misma acción “mientras que” una determinada
condición se cumpla:"""

# Actividad

"""Mientras que año sea menor o igual a 2012, imprimir la frase
“Informes del Año año”"""

year = 1989

while year <= 2012:
    print("Years report ", str(year))
    year += 1  # Para que te salga cada año desde 1989 sino entra en bucle infinito 1993

"""Pero ¿Qué sucede si el valor que condiciona la iteración no es numérico y no puede
incrementarse? En ese caso, podremos utilizar una estructura de control condicional,
anidada dentro del bucle, y frenar la ejecución cuando el condicional deje de cumplirse,
con la palabra clave reservada break:"""

while True:
    name = input("Enter your name: ")
    if name:
        break
print("Your name is", name, ",and this is a very beauty name, a name of a princess, of a Goddess ouuuuuhhh RIGHT!!.")

num1 = int(input("Enter first number: "))
num2 = int(input("Enter the second number: "))

result = num1 + num2
print(result)

# -----------------------------------Bucle For------------------------------------

my_list = ["Juan", "Antonio", "Pedro", "Herminio"]
for name in my_list:  # Se le va dando el valor a name de todos los nombres
    print(name)

# Otra forma de iterar con el for es usar "in range"

"""Por cada año en el rango 2001 a 2013, imprimir la frase
“Informes del Año año”"""

for year in range(2002, 2013):
    print("Years Report", str(year))

# Módulos Empaquetados

"""En Python, cada uno de nuestros archivos .py se denominan módulos. Estos módulos, a
la vez, pueden formar parte de paquetes. Un paquete, es una carpeta que contiene
archivos .py. Pero, para que una carpeta pueda ser considerada un paquete, debe
contener un archivo de inicio llamado __init__.py. Este archivo, no necesita contener
ninguna instrucción. De hecho, puede estar completamente vacío."""

"""└── paquete
    ├── __init__.py
    ├── modulo1.py
        └── subpaquete
            ├── __init__.py
            ├── modulo1.py
            └── modulo2.py"""

# Importanto módulos enteros

"""El contenido de cada módulo, podrá ser utilizado a la vez, por otros módulos. Para ello, es
necesario importar los módulos que se quieran utilizar. Para importar un módulo, se
utiliza la instrucción import, seguida del nombre del paquete (si aplica) más el nombre
del módulo (sin el .py) que se desee importar."""


# import modulo # importar un módulo que no pertenece a un paquete
# import paquete.modulo1 # importar un módulo que está dentro de un paquete
# import paquete.subpaquete.modulo1"""