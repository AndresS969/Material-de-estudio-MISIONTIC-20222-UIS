import random #etse modulo provee herramientas para generacion de elementos aleatorio

x = 8
b = 10
#print(random.uniform(x,b)) #para obtener un valor decima

lista = [12,11,24,30,60,80,90,10,5,8]
#print(random.choice(lista)) #este metodo me arroja un item aleatorio de la lista

from random import shuffle
x = ['Skyrim', 'Pertenece', 'A', 'Los', 'Nórdicos']
shuffle(x) #obtener objetos aleatorios 
#print(x)

"""jugador1 = input("presione X para jugar!: ")
lista1 = ["piedra","papel", "tijera"]
print(random.choice(lista1))
jugador2 = input("presione X para jugar!: ")
print(random.choice(lista1)) """


"""x = random.randint(0,200) #me devuelve un valor aleatorio entre 0 y 200
print(x)

digite = int(input("digite un numero de 1 a 200: "))
for i in range(digite):
    print(i)"""

import string
import random

def seguridad():
    print("generador de contraseñas segura")
    print()
    x = string.ascii_lowercase
    m = string.digits
    y = string.ascii_uppercase
    z = string.punctuation

    combinacion_contraseña = x+m+y+z
    longitud_contraseña = int(input("ingrese la longitud de la contraseña: ")) 

    password = "".join(random.sample(combinacion_contraseña,longitud_contraseña))
    print()
    print("Mi nueva contraseña es: ", password)
    

if __name__=="__main__":
    seguridad()
    
