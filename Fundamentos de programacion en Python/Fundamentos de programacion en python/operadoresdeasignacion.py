#OPERADORES DE ASIGNACION: consiste en asignar un valor a una variable, con "=" o con "+=", "-="
a = 5
a+= 10
print(a)

a1 = 10
a1-=5
print(a1)

a2 = 4
a2*=2
print(a2)

a3=10
a3/=5
print(a3)
#para importar todas las fucniones de un modulo usamos un asterisco, ejemplo "from math import *" me importara el modulo math con todas sus fucniones

x = bin(20) #pasar un numero a binario
print(x)

m = int("10") #pasar un string a entero
print(m)

a = 10
b = 5

a, b = b,a #intercambiar valores de una variable
print("nuevo:",a)
print("nuevo", b)