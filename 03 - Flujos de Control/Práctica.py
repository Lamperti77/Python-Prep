

from math import factorial


variable = 5

if (variable > 0):
    print ('es mayor que cero')
else:
    print ('es menor que cero')






entero = 20

flotante = 20.5

if (type (entero) == type (flotante)):
    print ('son del mismo tipo de dato')
else:
    print ('no son el mismo tipo de dato')



for i in range (1, 21):
    if (i % 2 == 0):
        print (i, 'es par')
    else:
        print (i, 'no es par')






for i in range (0, 6):
    print (i**3)








cinco = 5
for i in range (cinco):
    print(i)






numero = 5
if numero > 0:
    if (type (numero) == int):
        factorial = numero
        while (numero > 2):
            numero = numero - 1
            factorial = factorial * numero
        print (factorial)
    else:
        print ('no es un numero entero')
else:
    print ('no es mayor que cero')