#obtener promedio de estudiantes con sus tres notas
"""nota1=int(input("ingresa primera nota: "))
nota2=int(input("ingresa segunda nota: "))
nota3=int(input("ingresa tercera nota: "))
print(f"su nota definitiva es: ", (nota1+nota2+nota3)/3)"""

#ejercicio2

"""correctas=int(input("ingrese cantidad de respuestas correctas: "))
incorrectas=int(input("ingrese cantidad de respuestas incorrectas: "))
blanco=int(input("ingrese cantidad de respuestas en blanco: "))
print("puntaje de respuestas correctas: ", correctas * 4)
print("puntaje de respuestas incorrectas: ", incorrectas * -1)"""

#ejercicio3: sacar su identificacion

"""dni = int(input("ingrese su ano de nacimiento: "))
nacimiento = 2022 - dni
if nacimiento<17:
    print("usted no puede sacar su dni")
else:
    print("usted puede sacar su dni")"""

"""edad1=int(input("edad hermano 1: "))
edad2=int(input("edad hermano 2: "))
if edad1>edad2:
    print("hermano 1 es mayor que hermano 2 / diferencia de edad entre ambos es:", edad1 - edad2)
else:
    print("hermano 2 es mayor que hermano 1 / diferencia de edad entre ambos es:", edad2 - edad1)"""
    
#ejercicio4: saber si un operario recibira incentivos:
"""operario = int(input("ingrese cantidad de unidades producidas durante la semana: "))
if operario>100:
    print("usted recibira un incentivo")
else:
    print("usted no recibira un incentivo")"""
    
    
  
"""#ejercicio5 determinar mayor de tres numeros
numero1=int(input("ingrese un numero: "))
numero2=int(input("ingrese otro numero: "))
numero3=int(input("ingrese un numero mas : "))
if numero1>numero2 and numero3:
    print("numero mayor es: ", numero1)
    
elif numero2>numero3 and numero1:
    print("numero mayor es: ", numero2)
    
elif numero3>numero2>numero1:
    print("numero mayor es: ", numero3)"""
    
"""romanos = int(input("ingrese un numero de 1 a 10, se convertira a romano: "))
if romanos==1:
    print("I")
if romanos==2:
    print("II")
if romanos==3:
   print("III")
if romanos==4:
    print("IV")
if romanos==5:
    print("V")
if romanos==6:
    print("VI")
if romanos==7:
    print("VII")
if romanos==8:
    print("VIII")
if romanos==9:
    print("IX")
if romanos==10:
    print("X")"""
    
#ejercicio6:
"""15	Elabore un algoritmo que permita ingresar el monto de venta alcanzado por un vendedor durante el mes, luego de calcular la bonificación que le corresponde sabiendo:"""

"""monto = int(input("monto de venta alcanzado: "))
if monto>0 and monto<1000:
    print("su bonificacion es: 0 ")
elif monto>1000 and monto<5000:
    print("su bonificacion es: 3 ")
elif monto>5000 and monto<20000:
    print("su bonificacion es: 5 ")
else:
    print("su bonificacion es: 8 ")"""
 
"""16	Elabore un algoritmo que solicite un número entero y muestre un mensaje indicando la vocal correspondiente, considerando que la vocal A = 1."""

"""ingrese2= int(input("un número entero de 1 a 5: "))
if ingrese2==1:
    print("A")
elif ingrese2==2:
    print("E")
elif ingrese2==3:
    print("I")
elif ingrese2==4:
    print("O")
elif ingrese2==5:
    print("U")
else:
    print("numero incorrecto")"""
    
#18	Elabore un algoritmo que solicite un número entero y diferente a cero, e indique si es par.

"""entero = int(input("ingrese un numero entero positivo: "))
if entero<0:
    print("numero incorrecto!")
elif entero%2==0:
    print("es par")
else:
    print("es impar")"""
    
"""while True:
    entero1 = int(input("ingrese un numero: "))
    if entero1<0:
        entero1 = int(input("ingrese un numero: "))
    elif entero1%2==0:
        print("es par")
        break
    else:
        print("es impar")
        break"""
#19	Elabore un algoritmo que contenga los número pares del 1 al 10

"""for i in range(1,11):
    if i%2==0:
        print("numeros pares son: ", i)
    else:
        print("numeros impares: ", i)"""
        
#25	Elaborar un algoritmo que solicite ingresar letras hasta que este ingrese una vocal.

""""while True:
    mete = input("ingresa una letra: ")
    if mete!="a" and mete!="e" and mete!="i" and mete!="o" and mete!="u":
        mete = input("ingresa una letra: ")
    else:
        mete=="a" and mete=="e" and mete=="i" and mete=="o" and mete=="u"
        break"""
#2Elaborar un algoritmo que solicite 2 números enteros y un operador aritmético y luego debe de mostrar el resultado de la operación correspondiente.


"""numero1= int(input("ingrese un numero entero: "))
numero2= int(input("ingrese un numero entero: "))
operador =input("ingrese un operador aritmético: ")

if operador == "+":
    print("su suma es: ", numero1 + numero2)

elif operador=="-":
    print("su resta es: ", numero1 - numero2)
 
elif operador=="/":
    print("su division es: ", numero1 / numero2)
    
elif operador=="*":
    print("su multiplicacion es: ",numero1 * numero2 )"""

"""colores = ["rojo", "verde", "azul"]
print(colores[1])"""

"""Completa el código siguiente para que diga “Coge un pastel”
siempre y cuando se introduzca Pastel. De lo contrario haz
que le ofrezca una Galleta"""

"""Escribe la línea de código que falta de forma que el programa
pregunte por el nombre, hasta que se escriba Carlos"""

"""while True:
    nombre = input("ingresa tu nombre: ")
    if nombre=="carlos":
        break"""
"""Define una función llamada agradecimiento que imprima
‘Hola’ seguido del nombre."""

#Dise˜na un algoritmo que calcule el IVA (16%) de un producto dado su precio de venta sin IVA.
"""print("producto sin iva incluido")
print()
precio = float(input("ingrese precio de producto: "))
iva = precio*0.16
print("su precio + IVA es: ", precio + iva)"""
    

"""Dise˜na un programa que, a partir del valor de los dos lados de un rect´angulo (4 y 6 metros, respectivamente), muestre
el valor de su per´ımetro (en metros) y el de su ´area (en metros cuadrados).
(El per´ımetro debe darte 20 metros y el ´area 24 metros cuadrados.)"""

"""x = 4
y = 6
print("su area es: ",x*y)
print("su perimetro es: ", 2*(x+y))"""

"""Haz un programa que pida el nombre de una persona y lo muestre en pantalla repetido 1000 veces, pero dejando un
espacio de separaci´on entre aparici´on y aparici´on del nombre. (Utiliza los operadores de concatenaci´on y repeticion.)"""
    
"""nombre = input("ingrese su nombre: ")
for i in range(101):
    print()
    print(nombre)"""
"""Dise˜na un programa que lea un n´umero flotante por teclado y muestre por pantalla el mensaje ((El n´umero es
positivo.)) s´olo si el n´umero es mayor o igual que cero."""

"""number1 = float(input("ingresa un numero: "))
if number1>=0:
    print("es positivo")
else:
    print("no es positivo")"""

"""Dise˜na un programa que lea la edad de dos personas y diga qui´en es m´as joven, la primera o la segunda. Ten en
cuenta que ambas pueden tener la misma edad. En tal caso, hazlo saber con un mensaje adecuado."""

"""edad1=int(input("ingrese su edad: "))
edad2=int(input("ingrese su edad: "))
if edad1<edad2:
    print("esta persona es mas joven! su edad es: ", edad1)
elif edad1==edad2:
    print("tiene misma edad")

else:
    print("esta persona es mas joven!, su edad es: ", edad2)"""


"""Dise˜na un programa que, dado un n´umero entero, determine si ´este es el doble de un n´umero impar. (Ejemplo: 14 es
el doble de 7, que es impar.)"""

"""ingrese = int(input("ingrese un numero entero: "))
if ingrese%2==0:
    z = ingrese/2
if z%2==0:
    print(f"{ingrese} es el doble de {z} par")
else:
    print(f"{ingrese} es el doble de {ingrese/2} impar")""" 
    

"""Dise˜na un programa Python que lea un car´acter cualquiera desde el teclado, y muestre el mensaje ((Es una MAY´USCULA))
cuando el car´acter sea una letra may´uscula y el mensaje ((Es una MIN´USCULA)) cuando sea una min´uscula. En cualquier otro
caso, no mostrar´a mensaje alguno. (Considera ´unicamente letras del alfabeto ingl´es.) Pista: aunque parezca una obviedad,
recuerda que una letra es min´uscula si est´a entre la ’a’ y la ’z’, y may´uscula si est´a entre la ’A’ y la ’Z’."""


"""caracter = input("ingrese un caracter: ")
if caracter==caracter.upper():
    print("ha ingresado un caracter en mayuscula")
else:
    print("ha ingresado un caracter en minuscula")"""
    

"""numerodeveces=int(input("numero alumnos: "))
alumnos=[]
for i in range(numerodeveces):
	alumnos.append(input("numbre del alumno %s : " % (i+1)))
 
print(alumnos)"""

"""Dise˜na un programa que calcule la menor de cinco palabras dadas; es decir, la primera palabra de las cinco en orden
alfab´etico. Aceptaremos que las may´usculas son ((alfab´eticamente)) menores que las min´usculas, de acuerdo con la tabla
ASCII."""

"""num1=input("ingrese primera palabra: ")
num2=input("ingrese segunda palabra: ")
num3=input("ingrese tercera palabra: ")
num4=input("ingrese cuarta palabra: ")

cantidad = int(len(num1))
cantidad2=int(len(num2))
cantidad3=int(len(num3))
cantidad4=int(len(num4))

if cantidad>cantidad2 and cantidad>cantidad3 and cantidad>cantidad4:
    print(f"esta palabra es mayor: {num1} tiene un total de: {cantidad} letras")
elif cantidad2>cantidad and cantidad2>cantidad3 and cantidad2>cantidad4:
    print(f"esta palabra es mayor: {num2} tiene un total de: {cantidad2} letras")
elif cantidad3>cantidad2 and cantidad3>cantidad and cantidad3>cantidad4:
    print(f"esta palabra es mayor: {num3} tiene un total de: {cantidad3} letras")
    
elif cantidad4>cantidad3 and cantidad4>cantidad2 and cantidad4>cantidad:
    print(f"esta palabra es mayor: {num4} tiene un total de: {cantidad4} letras")
    
elif cantidad==cantidad2==cantidad3==cantidad4:
    print("son iguales")"""
    
#Escribir una función que reciba un número entero positivo y devuelva su factorial.

"""from functools import reduce

x = range(1,6)
z = reduce(lambda x,y:x*y,x)
print(z)"""
  
"""def suma(x,y,a,b):
    suma_1 = x+y
    resta = a - b
    return suma_1, resta

primera_suma, segundaresta = suma(10,5,30,20)
print("suma es: ", primera_suma)
print("resta es: ", segundaresta)"""


#Escribir una función que convierta un número decimal en binario y otra que convierta un número binario en decimal.
"""def decimal_binario(b):
    x = bin(b)
    return x
print(decimal_binario(3342))
print(float(110100001110))"""


"""Escribir un programa que reciba una cadena de caracteres y devuelva un diccionario con cada palabra que contiene y su frecuencia. Escribir otra función que reciba el diccionario generado con la función anterior y devuelva una tupla con la palabra más repetida y su frecuencia."""

"""def caracteres(x):
    monda = []
    monda.append(x)
    x = len(x)
    return monda, x

lista, objetos = caracteres("mi monda sabe a ti jajaja")
print(lista)"""



"""Escribir un programa que pregunte al usuario su edad y muestre por pantalla todos los años que ha cumplido (desde 1 hasta su edad)."""

"""edad = int(input("pregunte al usuario su edad: "))
for i in range(edad):
    print(f"usted ha cumplido {i+1} años")"""


"""Escribir un programa que pida al usuario un número entero positivo y muestre por pantalla todos los números impares desde 1 hasta ese número separados por comas"""

"""positivo = int(input("número entero positivo: "))
for i in range(positivo):
    if i%2==1:
        print("numeros impares son: ", i)


for i in range(1, 11):
    for j in range(1, 11):
        print(i*j, end="\t")
    print("")"""
    
"""from matplotlib import pyplot """
    
"""x = ["andres", "pedro", "maria", "jose"]
y = [4.5, 3.4, 2.0, 3.5]
colores = ["green", "blue", "red", "yellow"]
pyplot.title("Notas de estudiantes de curso Python")
pyplot.bar(x, height=y, color=colores, width=0.7)
pyplot.show()"""


"""numerodeveces=int(input("numero alumnos: "))
alumnos=[]
for i in range(numerodeveces):
	alumnos.append(input("numbre del alumno %s : " % (i+1)))
z = alumnos
m = [4.5, 3.4, 2.0, 3.5]
colores1 = ["green", "blue", "red", "yellow"]
pyplot.title("Notas de estudiantes ")
pyplot.bar(alumnos, height=m, color=colores1, width=0.7)
pyplot.show()"""

"""Escribir un programa que muestre el eco de todo lo que el usuario introduzca hasta que el usuario escriba “salir” que terminará."""


"""while True:
    monda = input("ingrese random: ")
    if monda=="salir":
        break
print("usted salio")"""

from matplotlib import pyplot

"""print("programa para graficar notas de estudiantes")
print()

ingresa = int(input("ingresa cantidad de estudiantes: "))
coloresx = ["green", "blue", "red", "yellow","black"]
x = []
y = []
for i in range(ingresa):
    ingresa2=input(f"ingresa nombre de estudiante {i+1}: ")
    notas = int(input(f"ingresa nota de estudiante{i+1}: "))
    print("*****************************************************************")
    x.append(ingresa2)
    y.append(notas)
pyplot.title("Grafica de notas de estudiantes")
#pyplot.plot(x, y, marker="o") #recibe dos argumentos, las dos listas, muestra una grafica lineal, usamos marker para agregar puntos
pyplot.xlabel("nombres (n)") #para agregar mensajes 
pyplot.ylabel("Notas (n)")
pyplot.bar(x, height=y, color=coloresx, width=0.7) 
pyplot.xlabel("nombres (n)") #para agregar mensajes 
pyplot.ylabel("Notas (n)")
pyplot.show()"""

    

"""Dise˜na un programa que, dado un n´umero real que debe representar la calificaci´on num´erica de un examen, proporcione
la calificaci´on cualitativa correspondiente al n´umero dado. La calificaci´on cualitativa ser´a una de las siguientes: ((Suspenso))
(nota menor que 5), ((Aprobado)) (nota mayor o igual que 5, pero menor que 7), ((Notable)) (nota mayor o igual que 7, pero
menor que 8.5), ((Sobresaliente)) (nota mayor o igual que 8.5, pero menor que 10), ((Matr´ıcula de Honor)) (nota 10)."""

"""nota = float(input("ingrese su nota: "))
if nota<5:
    print("suspenso")
elif nota>=5 and nota<7:
    print("Aprobado")
elif nota>=7 and nota<8.5:
    print("Notable")
elif nota>=8.5 and nota<10:
    print("sobresaliente")
else:
    print("Matricula de Honor")"""
    
"""Queremos hacer un programa que calcule el factorial de un n´umero entero positivo. El factorial de n se denota con
n!, pero no existe ning´un operador Python que permita efectuar este c´alculo directamente. Sabiendo que"""


"""Dise˜na un programa que solicite la lectura de un n´umero entre 0 y 10 (ambos inclusive). Si el usuario teclea un
n´umero fuera del rango v´alido, el programa solicitar´a nuevamente la introducci´on del valor cuantas veces sea menester."""

"""while True:
    numero = int(input("ingrese un numero entre 0 y 10: "))
    if numero>=0 and numero<=10:
        break
    elif numero>10:
        numero = int(input("ingrese un numero entre 0 y 10: "))"""

"""Dise˜na un programa que solicite la lectura de un texto que no contenga letras may´usculas. Si el usuario teclea una
letra may´uscula, el programa solicitar´a nuevamente la introducci´on del texto cuantas veces sea preciso."""

"""while True:
    mayuscula = input("ingrese una palabra: ")
    m = mayuscula.upper()
    if mayuscula==m:
        mayuscula = input("ingrese una palabra: ")
    elif mayuscula!=m:
        break
print("exito")"""


"""Haz un programa que muestre la tabla de multiplicar de un n´umero introducido por teclado por el usuario. Aqu´ı
tienes un ejemplo de c´omo se debe comportar el programa:"""

"""ingresar = int(input("dame un numero: "))  
for i in range(11):
    print(f"{ingresar} * {i} =", i*ingresar)"""
    
    
"""from matplotlib import pyplot

x = ["uruguay", "USA", "Rusia", "china", "iran"]
y = [13, 30, 21, 45, 8]
c = ["yellow", "green", "red", "purple", "black"]
pyplot.title("Crecimiento economico durante 2021")
pyplot.xlabel("paises (p)")
pyplot.ylabel("porcentaje (%)")
pyplot.plot(x,y, marker="o")
#pyplot.bar(x, height=y, color=c, width=0.8)
pyplot.show() """

"""Haz un programa que vaya leyendo n´umeros y mostr´andolos por pantalla hasta que el usuario introduzca un n´umero
negativo. En ese momento, el programa mostrar´a un mensaje de despedida y finalizar´a su ejecuci´on."""
"""while True:
    digito = int(input("introduce un numero: "))
    if digito<0:
        print("adios")
        break"""
"""for i in range(1,11):
    for j in range(1,11):
        print(i*j, end= "\t")"""
        
#grafico de lineas
"""pyplot.figure(figsize=(15,10)) #tamano
x = ["uruguay", "USA", "Rusia", "china", "iran"]
y = [13, 30, 21, 45, 8]
c = ["yellow", "green", "red", "purple", "black"]
pyplot.title("Crecimiento economico durante 2021")
pyplot.xlabel("paises (p)")
pyplot.ylabel("porcentaje (%)")
pyplot.plot(x,y, marker="o", label="USA")#mostrar en screen
#pyplot.bar(x, height=y, color=c, width=0.8, )
pyplot.legend(loc="upper left") #para mostrar un dato en pantaa y poner su ubicacion
pyplot.savefig("prueba.png") #para guarda figura
pyplot.show()"""


#grafica de barras

#pyplot.figure(figsize=(20,10))
""" = ["uruguay", "USA", "Rusia", "china", "iran"]
y = [13000000, 30000000, 21000000, 45000000, 8000000]
c = ["red", "brown", "yellow", "purple", "blue"]"""
"""pyplot.title("Crecimiento de gente en 2020")
pyplot.bar(x1, height=y, color=c, width=0.8 )
pyplot.xlabel("paises (p)")
pyplot.ylabel("personas (p)")
pyplot.show()"""

#piecharts o graficas circulares
"""from matplotlib import pyplot

pyplot.pie(y, labels=x)
pyplot.figure(figsize=(20,10))
pyplot.show()"""

"""Dise˜na un programa que indique si una cadena le´ıda de teclado est´a bien formada como n´umero entero. El programa
escribir´a ((Es entero)) en caso afirmativo y ((No es entero)) en caso contrario."""


"""cadena = input("ingrese una cadena: ")
entero = len(cadena)
if entero%2==0:
    print("es un entero")
else:
    print("no es un entero")"""
 
"""Dise˜na un programa que, dada una cadena, muestre por pantalla todos sus prefijos. Por ejemplo, dada la cadena
’UJI’, por pantalla debe aparecer:""" 
    
"""mondana = "UJI"
print(mondana[0])
print(mondana[0:2])
print(mondana[:])"""

"""from functools import reduce

lista = [1,2,3,4,5,6,7,2,21,21,12,34] 
lista1 = [1,2,3,4,5,6,7,2,21,21,80,20,5]
z = reduce(lambda x,y: x+y, lista1)
print(z)"""




"""Haz un programa que almacene en a una lista obtenida con range(1,n), donde n es un entero que se pide al usuario
y modifique dicha lista para que cada componente sea igual al cuadrado del componente original. El programa mostrar´a la
lista resultante por pantalla."""
"""x = int(input("ingrese un numero: "))
m = range(1, x)
print(list(m))"""


"""Dise˜na un programa que lea una lista de 10 enteros, pero asegur´andose de que todos los n´umeros introducidos por
el usuario son positivos. Cuando un n´umero sea negativo, lo indicaremos con un mensaje y permitiremos al usuario repetir
el intento cuantas veces sea preciso."""



"""for i in range(10):
    montana = int(input("ingrese un numero: "))
    lista.append(montana)
print(lista)"""

"""Dise˜na un programa que lea una cadena y muestre por pantalla una lista con todas sus palabras en min´usculas. La
lista devuelta no debe contener palabras repetidas."""
"""lista = []
cadena = input("ingrese una cadena: ")
x=set(cadena.lower().split())

print(x)"""


"""Dise˜na un programa que elimine de una lista todos los elementos de ´ındice par y muestre por pantalla el resultado.
(Ejemplo: si trabaja con la lista [1, 2, 1, 5, 0, 3], ´esta pasar´a a ser [2, 5, 3].)"""

"""2onda4 = [1, 2, 1, 5, 0, 3]


def borrar_pares(x):
    if x%2==1:
        return True
    
    
borrar = list(filter(borrar_pares, monda4))
print(borrar)"""


"""def suma(x,y):
    monda3 = x + y
    resta = x - y
    return monda3, resta
    
suma1,resta2=suma(30,10)
print("suma es: ", suma1)
print("resta es: ", resta2)"""


"""Define una funci´on llamada area_circulo que, a partir del radio de un c´ırculo, devuelva el valor de su ´area. Utilizael valor 3.1416 como aproximaci´on de  o importa el valor de  que encontrar´as en el m´odulo math.
(Recuerda que el ´area de un c´ırculo es r2.)"""
"""from math import pi

def area_circulo(r):
    area = pi*(r)**2
    return area
    
print(area_circulo(3.4))"""

"""Dise˜na una funci´on que devuelva el valor absoluto de la m´axima diferencia entre dos elementos consecutivos de una
lista. Por ejemplo, el valor devuelto para la lista [1, 10, 2, 6, 2, 0] es 9, pues es la diferencia entre el valor 1 y el valor 10."""

"""def diferencia(m):
    return max(m) -1  
print(diferencia([1, 20, 2, 6, 2, 0]))"""

"""Define una funci´on que, dada una cadena x, devuelva otra cuyo contenido sea el resultado de concatenar 6 veces x
consigo misma."""
"""def cadenatexto(x):
    concatenar = x+x+x+x+x+x
    return concatenar
print(cadenatexto("mimonda"))"""


"""Dise˜na una funci´on que, dada una lista de cadenas, devuelva la cadena m´as larga. Si dos o m´as cadenas miden lo
mismo y son las m´as largas, la funci´on devolver´a una cualquiera de ellas.
(Ejemplo: dada la lista [’Pepe’, ’Juan’, ’Mar´ıa’, ’Ana’], la funci´on devolver´a la cadena ’Mar´ıa’.)"""

"""andres = ["pepe", "juan", "maria", "ana"]
def buscar(cadena):
    z = andres[0]
    q = andres[1]
    g=andres[2]
    p = andres[3]
    m =len(z)
    m1=len(q)
    m2=len(g)
    m3=len(p)
    if m>m1 or m>m2 or m>m3:
        pass
    elif m1>m or m1>m2 or m1>m3:
        return pass
    elif m2>m1 or m2>m or m2>m3:
        return m2
    elif m3>m2 or m3>m or m3>m1:
        return False
print(buscar(["monda", "pedro", "cs", "ana"]))"""

"""Dise˜na una funci´on llamada menu_generico que reciba una lista con opciones. Cada opci´on se asociar´a a un n´umero
entre 1 y la talla de la lista y la funci´on mostrar´a por pantalla el men´u con el n´umero asociado a cada opci´on. El usuario
deber´a introducir por teclado una opci´on. Si la opci"""

"""def menu_generico(opcion):
    print("\t\t\t\t\tmenu de opciones")
    print()
    print()
    print("1)saludar")
    print()
    print("2)despedirse")
    print()
    print("3)salir")
    opcion = int(input("\n¿que opcion desea escoger?: "))
    if opcion==1:
        return "\nhello world"
    elif opcion==2:
        return "\nsee you soon boi"
    elif opcion==3:
        return "\ngracias por usar nuestro servicio!"
   
    
opcion = " "     
print(menu_generico(opcion))"""


#Escribe una funci´on Python sin argumentos llamada dado que devuelva un n´umero entero aleatorio entre 1 y 6.
#import random

"""def dado():
    x = random.randint(1,6)
    if x%2==0:
       return x
    
print(dado())"""

    
"""Dise˜na una funci´on sin argumentos que devuelva un n´umero aleatorio mayor o igual que 0.0 y menor que 10.0.
Puedes llamar a la funci´on random desde tu funci´on."""

"""def aleatorio():
    x = random.randint(0,10)
    if x>=0 and x<10:
        return x
print(aleatorio())"""

#Dise˜nar una funci´on que reciba la lista de notas y devuelva el n´umero de aprobados.

"""def aprobados(t):
 
    if t>3:
        return True
def no_aprobados(y):
    if y<3:
        return True
    
m = list(filter(aprobados, [2, 5, 4, 2,2,4,5,6,1,2,3,]))
print("estudiantes aprobados: ", m)
print()
z = list(filter(no_aprobados, [2, 5, 4, 2,2,4,5,6,1,2,3,]))
print("estudiantes aprobados: ", z)"""


"""from matplotlib import pyplot"""
#grafica barras
"""x = ["uruguay", "Iran", "India", "noruega", "peru", "colombia"]
y = [15, 12,22,30,4,2]
colores = ["blue", "brown", "purple", "orange","black", "red"]
pyplot.bar(x, height=y, color=colores, width=0.9)
pyplot.title("Crecimiento economico durante 2020")
pyplot.xlabel("Paises (p)")
pyplot.ylabel("Porcentaje (%)")
pyplot.show()"""


#grafica lineal
"""pyplot.figure(figsize=(15,9))
x = ["uruguay", "USA", "Rusia", "china", "iran"]
y = [13, 30, 21, 45, 8]
#colores = ["blue", "brown", "purple", "orange","", "red"]
pyplot.plot(x,y,marker="o")
pyplot.title("Crecimiento economico durante 2020")
pyplot.xlabel("Paises (p)")
pyplot.ylabel("Porcentaje (%)")
pyplot.show()"""


#grafico de lineas
"""pyplot.figure(figsize=(15,10)) #tamano
x = ["uruguay", "USA", "Rusia", "china", "iran"]
y = [13, 30, 21, 45, 8]
c = ["yellow", "green", "red", "purple", "black"]
pyplot.title("Crecimiento economico durante 2021")
pyplot.xlabel("paises (p)")
pyplot.ylabel("porcentaje (%)")
pyplot.plot(x,y, marker="o", label="USA")#mostrar en screen
#pyplot.bar(x, height=y, color=c, width=0.8, )
pyplot.legend(loc="upper left") #para mostrar un dato en pantaa y poner su ubicacion
pyplot.savefig("prueba.png") #para guarda figura
pyplot.show()"""


"""pyplot.figure(figsize=(15,9))
x = ["uruguay", "USA", "Rusia", "china", "iran"]
y = [13, 30, 21, 45, 8]
#colores = ["blue", "brown", "purple", "orange","", "red"]
pyplot.pie(y, labels=x)
pyplot.title("Crecimiento economico durante 2020")
pyplot.show()"""


"""Dise˜na una funci´on que reciba dos listas y devuelva los elementos comunes a ambas, sin repetir ninguno (intersecci´on
de conjuntos).
Ejemplo: si recibe las listas [1, 2, 1] y [2, 3, 2, 4], devolver´a la lista [2]."""


"""def comunes(x,y):
    m = x & y
    return list(m)
    
print(comunes({1, 2, 1},{2, 3, 2, 4}))"""

"""Dise˜na una funci´on que reciba dos listas y devuelva los elementos que pertenecen a una o a otra, pero sin repetir
ninguno (uni´on de conjuntos).
Ejemplo: si recibe las listas [1, 2, 1] y [2, 3, 2, 4], devolver´a la lista [1, 2, 3, 4]."""


"""def union(m,o):
    z = m | o
    return list(z)
print(union({1, 2, 1},{2, 3, 2, 4}))"""


#Dise˜na una funci´on que, dada una lista de n´umeros, devuelva otra lista que s´olo incluya sus n´umeros impares.

"""def impares(x):
    if x%2==1:
      return x

x = list(filter(impares, [1,2,3,4,5,6,7,8,9,10,70,40,4,3,1]))
print(x)"""

"""def incrementa(a):
    a = a + 1
    return a
print(incrementa(10))"""

"""Dise˜na una funci´on que reciba una lista y devuelva otra lista cuyo contenido sea la lista original, pero con sus componentes en orden inverso. La lista original no debe modificarse."""

"""def invertir(x):
    z = x[::-1]
    return z
print(invertir([1,2,3,4,5,6,7,8,9,10,70,40,4,3,1]))"""

"""Dise˜na una funci´on que dado un registro de tipo Persona (con fecha de nacimiento) y la fecha de hoy, devuelva la
edad (en a˜nos) de la persona."""

"""def fecha_nacimiento(f):
    zeta = 2022 - f
    return zeta
    
moda5 = int(input("ingrese su fecha de nacimiento: "))
print(fecha_nacimiento(moda5))"""
"""Escribir un programa que almacene la cadena de caracteres contraseña en una variable, pregunte al usuario por la contraseña hasta que introduzca la contraseña correcta."""
"""contrasena = "andres"
monda = " "
cerrar = True
while contrasena!=monda:
    monda = input("ingrese contrasena: ")
    if monda==contrasena:
        cerrar = False"""
        
        
"""Utiliza las funciones desarrolladas en el ejercicio 307 y dise˜na nuevas funciones para construir un programa que
presente el siguiente men´u y permita ejecutar las acciones correspondientes a cada opci´on:
1) Anadir estudiante y calificacion
2) Mostrar lista de estudiantes con sus calificaciones
3) Calcular la media de las calificaciones
4) Calcular el numero de aprobados
5) Mostrar los estudiantes con mejor calificacion
6) Mostrar los estudiantes con calificacion superior a la media
7) Consultar la nota de un estudiante determinado
8) FINALIZAR EJECUCI´ON DEL PROGRAMA"""


"""Dise˜na una funci´on duplica que reciba una lista de n´umeros y la modifique duplicando el valor de cada uno de sus
elementos. (Ejemplo: la lista [1, 2, 3] se convertir´a en [2, 4, 6].)"""

"""import random
 
cantidad = int(input("introduzca cantidad total de su compra: "))

if cantidad<100:
        print("USTED NO TIENE DESCUENTO, NO PUEDE PARTICIPAR")
    
elif cantidad>=100:

    
    print()
    print("SU GASTO IGUALA O SUPER LOS $100.00 Y POR LO TANTO PARTICIPA EN LA PROMOCION!")
    print()
    print("\t\tCOLOR")  
    print("\t\tBOLA BLANCA")
    print("\t\tBOLA ROJA")
    print("\t\tBOLA AZUL")
    print("\t\tBOLA VERDE")
    print("\t\tBOLA AMARILLA")
    print()
    print("\t\tDESCUENTO")
    print("\t\tBOLA BLANCA = NO TIENE DESCUENTO") 
    print("\t\tBOLA ROJA TIENE UN DESCUENTO DE 10%")
    print("\t\tBOLA AZUL TIENE UN DESCUENTO DE 20%")
    print("\t\tBOLA VERDE TIENE UN DESCUENTO DE 25%")
    print("\t\tBOLA AMARILLA TIENE UN DESCUENTO DE 50%")
    print()



    rifa = random.randint(1,5)
if rifa==1:
    print("ALEATORIAMENTE USTED OBTUVO LA BOLA BLANCA, NO SE APPLICA DESCUENTO, GRACIAS POR JUGAR")
    
elif rifa==2:
    print("ALEATORIAMENTE USTED OBTUVO LA BOLA ROJA,TIENE UN DESCUENTO DE 10%")
    descuento = cantidad * 0.10
    print()
    print("USTED DEBERA PAGAR:", cantidad - descuento)

elif rifa==3:
    print("ALEATORIAMENTE USTED OBTUVO LA BOLA AZUL,TIENE UN DESCUENTO DE 20%")
    descuento = cantidad * 0.20
    print()
    print("USTED DEBERA PAGAR:", cantidad - descuento)
    

elif rifa==4:
    print("ALEATORIAMENTE USTED OBTUVO LA BOLA VERDE,TIENE UN DESCUENTO DE 25%")
    descuento = cantidad * 0.25
    print()
    print("USTED DEBERA PAGAR:", cantidad - descuento)
    
elif rifa==5:
    print("ALEATORIAMENTE USTED OBTUVO LA BOLA AMARILLA,TIENE UN DESCUENTO DE 50%")
    descuento = cantidad * 0.50
    print()
    print("USTED DEBERA PAGAR: ", cantidad - descuento)"""
    
  
    


"""x = input("ingrese una palabra: ")

if x[::-1]==x:
    
    print("si es una palabra palindroma!")
else:
    print("no es una palabra palindroma")"""

"""x = input("ingrese una palabra: ")
z = x.title().replace(" ", "*")
print(z)"""


"""pyplot.figure(figsize=(15,10))
x = ["peru", "USA", "Argentina"]
y = [12, 30, 1]
colores = ["red", "yellow", "blue"]

pyplot.title("Crecimiento economico durante 2020")
pyplot.bar(x, height=y, color=colores, width=0.6)
pyplot.xlabel("Paises (p)")
pyplot.ylabel("porcentaje (%)")
pyplot.legend()
pyplot.show()"""


#grafica 

"""x = ["peru", "USA", "Argentina"]
y = [12, 30, 1]
pyplot.title("Crecimiento economico durante 2020")
pyplot.pie(y, labels=x)

pyplot.show()"""

#scatterplot
"""y = [12, 30, 1, 30,20,50,10,30,10,8,4,3,1]
x = [12, 30, 1, 31,13,20,13,33,11,8,4,35,80]
pyplot.scatter(x,y)
pyplot.show()"""




#histograma

"""x = [12, 30,40,23,25,37,60,67,36,20,10, 1]
sexo = [15,20, 30, 35,1]
pyplot.hist(x, sexo)
pyplot.show()"""


    

"""z = prueba3.isalpha()
print(z)

x = prueba3.isdigit()
print(x)

m = prueba3.isupper()
print(m)"""




"""Pide una cadena y un carácter por teclado (valida que sea un carácter) y muestra cuantas veces aparece el carácter en la cadena."""

"""caracter = input("ingresa una cadena: ")
caracter1 = input("ingresa una caracter: ")

z = caracter.count(caracter1)
print(f"el caracter \"{caracter1}\" aparece {z} veces en la cadena!")"""



"""Pide una cadena y dos caracteres por teclado (valida que sea un carácter), sustituye la aparición del primer carácter en la cadena por el segundo carácter."""

"""import heapq #modulo

z = [12, 30,40,23,25,37,60,67,36,20,10, 1]
print(heapq.nlargest(2,z)) #para saber los 2 valores mas altos de una lista
print(heapq.nsmallest(4,z))#para saber los 4 valores mas pequenos de una lista
print(heapq.nsmallest(4,z))"""
        


"""Escribir un programa que pregunte el nombre del usuario en la consola y un número entero e imprima por pantalla en líneas distintas el nombre del usuario tantas veces como el número introducido."""

"""nombre = input("ingrese su nombre: ")
entero = int(input("ingrese un numero entero: "))

for i in range(entero):
    print(nombre)
    
print("DIVISOR DE NÚMEROS")
dividendo = int(input("Escriba el dividendo: "))
divisor = int(input("Escriba el divisor: "))
resto = dividendo%divisor
division = dividendo / divisor
if dividendo%divisor==0:
    print(f"si es es exacta!, su cociente es {division}")
elif dividendo%divisor!=0:
    print(f"no es es exacta!, su cociente es {division} y su resto es {resto}")"""
    
"""Escriba un programa que simule un juego en el que dos jugadores (Carmen y David) tiran dos dados. El que saque mayor puntuación total, gana. Si la puntuación total coincide, gana quien haya sacado el dado con el valor más alto. Si el valor más alto también coincide, empatan."""

import random

"""print("JUEGO DE DADOS")
print()
z = random.randint(1,6) #dadosdeandres
x = random.randint(1,6)
juan = random.randint(1,6)#dados juan
juan1 = random.randint(1,6)
suma_andres = z + x
suma_juan= juan + juan1
print("JUGADORES: ANDRES, JUAN.")
print()
print("Turno de andres: ")
print("primer dado: ", z)
print("segundo dado: ", x)
print()
print("Turno de juan: ")
print("primer dado: ", juan)
print("segundo dado: ", juan1)

if suma_andres>suma_juan:
    print()
    print("Ha ganado Andres!")
elif suma_juan>suma_andres:
    print()
    print("ha ganado juan")
elif suma_andres==suma_juan:
    print()
    print("empatados")"""

"""print("PIEDRA, PAPEL, ... ¡TIJERA!")
print()

juego = ["PIEDRA", "PAPEL","¡TIJERA!"]
a = random.choice(juego)
b = random.choice(juego)
print("ines ha sacado: ", a)
print()
print("juan ha sacado: ", b)

if a=="PIEDRA" and b=="PAPEL":
    print()
    print("Juan ha ganado!")
elif a=="¡TIJERA!" and b=="PAPEL":
    print("ines ha ganado!")
 
elif a=="PIEDRA" and b=="PIEDRA" and a=="PAPEL" and b=="PAPEL" and a=="¡TIJERA!" and b=="¡TIJERA!":
    print("EMPATE!")"""
 
"""print("LISTAS A PARTIR DE VALOR")
print()
monda9=int(input("ingresa un numero mayor que 0: "))
monda = range(0, monda9+1)
monda1 = range(0, monda9-1)
print(list(monda))
print(list(monda[::-1]))
print(list(monda1+1))

LISTAS DESDE CERO HASTA VALOR
Escriba un número entero: 9
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]"""

"""sexoduro = int(input("ingrese un numero: "))

sexori = range(0, sexoduro+1)
print(list(sexori))"""

#except ZeroDivisionError:



"""print("MAYOR, MENOR Y MEDIA ARITMÉTICA")
num = int(input("¿Cuántos valores va a introducir?"))
if num<=0:
        print("ERROR")
lista = []
for i in range(num):
    num1 = input(f"Dígame la palabra {str(i+1)}: ")
    lista.append(num1)
    
print("su lista es: ", lista)
print()
buscar = input("Dígame que palabra desea sustituir: ")
print()
buscar1 = input("por la palabra: ")
print()
lista[buscar]=buscar1
#x = list(buscar.replace(buscar, buscar1))


print("su nueva lista ahora es: ",lista)"""


"""try:
    n1 = int(input("ingrese numero 1: "))
    n2 = int(input("ingrese numero 2: "))
    print("resultado es: ", n1/n2)
except ZeroDivisionError:
        print("usted no puede dividir entre 0")"""
        
 #hcbsdbcsdhvbdsbh   
 

"""print("CONFIRME SU CONTRASEÑA")
print()
while True:
    num1 = input("Escriba su contraseña: ")
    num2= input("Escriba de nuevo su contraseña: ")
    if num1==num2:
        print("Las contraseñas coinciden! bye")
        break
    elif num1!=num2:
        print("contraseñas no coinciden!, intente de nuevo")"""
   


"""while True:
    
    intro = input("Pulse x para lanzar el dado. Pulse otra tecla  para terminar: ")
    x = random.randint(1,6)
    if intro=="x":
       print("tirada: ", x)
    else:
        break"""
#djvvsdvsd


"""while True:
    primero = int(input("32 + 47 ="))
    if primero==79:
        print("¡Respuesta correcta!")
        break
    elif primero!=79:
        print("¡Respuesta incorrecta!")
    
    segundo = int(input("65 + 42 ="))
    if segundo==107:
        print("¡Respuesta correcta!")
        break
    elif segundo!=107:
            print("¡Respuesta incorrecta!")
    
    tercero = int(input("6 + 71 ="))
    if tercero==77:
        print("¡Respuesta correcta!")
        break
    elif tercero!=77:
            print("¡Respuesta incorrecta!")"""
    
            

import time

"""start = time.time()

prueba = int(input("cuanto es 1 + 1 = "))
print()

end = time.time()

print(f"usted ha tardado:  {round(end - start,0)} segundos")"""


import random
import string

"""def generar_contrasena():
    caracter = string.ascii_lowercase + string.digits + string.punctuation + string.ascii_uppercase

    contrasena = []

    while (len(contrasena) < 16):
        caracteres=random.choice(caracter)    
        contrasena.append(caracteres)

    contrasena = "".join(contrasena)
    return contrasena

def run():
    contrasena = generar_contrasena()
    print('Tu nueva contraseña es: '+ contrasena)

if __name__ == "__main__":
    run()"""
    


"""def palindromo(palabra):
    palabra = palabra.replace(' ', '')
    palabra = palabra.lower()
    palabra_invertida = palabra[::-1]
    if palabra == palabra_invertida:
        return True
    else:
        return False


def run():
    palabra = input('Escribe una palabra: ')
    es_palindromo = palindromo(palabra)
    if es_palindromo == True:
        print('Es palíndromo')
    else:
        print('No es palíndromo')


if __name__ == '__main__':
    run()"""
    
    
import heapq 

"""uno = [1,2,3,4,5,6,7,8,9,10]
x = heapq.nsmallest(2,uno)

z = heapq.nlargest(2,uno)
print("dos numeros mas largos: ", z)
print("dos numeros mas pequenos: ", x)
print(abs(-8))"""


"""ingreso = int(input("¿Cuántos valores va a introducir?" ))
acumu = 0
for i in range(ingreso):
    ingrese1 = int(input("Escriba un número: "))
    acumu = acumu + ingrese1
print("producto es: ", acumu)"""

"""Escriba un programa que pida primero cuántos números se van a escribir, que pida a continuación esa cantidad de números y al final diga tanto la suma de los números pares introducidos como la suma de los números impares introducidos. El programa no necesita comprobar que los valores introducidos sean positivos."""

"""ingreso = int(input("¿Cuántos valores va a introducir?" ))
acumu = 0
acumu1 = 0
for i in range(ingreso):
    ingrese1 = int(input(f"Escriba un número {str(i+1)}: "))"""


"""def crear():
    lista = []
    cantidad = int(input("Dígame cuántas palabras tiene la lista: "))
    for i in range(cantidad):   
        word = input(f"Dígame la palabra {str(i+1)}: ")
        lista.append(word)
    print("sus nueva lista es: ", lista)   

crear()"""

"""def Generador_de_listas():
    print("\t\t***********************Generador de listas*******************")
    print()

cantidad = int(input("¿Cuántas listas quiere escribir?: "))
print()
lista = []
lista1 = []
for i in range(cantidad):
    words = int(input(f"Dígame cuántas palabras tiene la lista {i+1}: "))
    print()
    lista.append(words)
    
    for j in range(words):
        print()
        words1 = input(f"Dígame la palabra {str(j+1)}: ")
        print()
        lista1.append(words1)
    

print("La lista es: ",lista)
print("La lista es: ",lista1)

Generador_de_listas()"""
"""Se quiere realizar un programa que lea por teclado las 5 notas obtenidas por un alumno (comprendidas entre 0 y 10). A continuación debe mostrar todas las notas, la nota media, la nota más alta que ha sacado y la menor."""
"""from functools import reduce
lista = []
for i in range(5):
   decidir = int(input(f"ingrese nota {str(i+1)}: "))
   lista.append(decidir)
   z = reduce(lambda x,y: x+y,lista)
print("su media es: ", z/5)
print("nota superior es: ", max(lista))  
print("nota inferior es: ", min(lista))  
print("sus notas son: ", lista)"""

"""z = [2,3,4,5,6,1,9,7,8]

z.sort()
print(z)

z1 = sorted(z) #me retorna una copia de una lista
print(z1)"""


"""monda = "andres felipe silvera llanos"

x = len(monda.replace(" ",""))
print(x)

prueba = input("ingresa tu nombre: ")
contador = 0

for i in prueba:
    contador+=1
    
print(f"mi nombre tiene {contador} letras")"""

"""import string
try:

    ingreso = int(input("ingrese un numero menor o igual a 26: "))

    x = list(string.ascii_uppercase)
    print(f"su numero ingresado {ingreso} equivale a la letra '{x[ingreso-1]}' en el abecedario!")
except IndexError:
        print("error, debio ingresar un numero menor o igual que 26!")"""
    


import heapq

"""a = [2,3,4,5,6,1,9,7,8]
print(heapq.nsmallest(2,a))"""

"""zeta= [9,8,7,6,5,4,3,2,1]
zeta.sort()
print(zeta)

copia = sorted(zeta)

print(copia)"""


"""def sin_retorno(x,y): #parametros
    
   
    return x * y
    
print(sin_retorno(2,4)) #argumentos


def rectangu(a,b):
    a = int(input("ingrese ancho: "))
    b = int(input("ingrese alto: "))
    return (a, """
    
    

"""a = 8

def prueba():
    a = 7
    print(type(a))
    
prueba()
print(type(a))

x = "9"
print(ord(x))


for i in range(0,11):
    if i%2==0:
        continue
    print(i)
    
for i in range(0,11):
    if i%2==0:
        pass
    print(i)"""
    
    
"""a = 8

def prueba():
    a = 8
    x = "q"
    print(ord(x))
    
    
print(type(a))
prueba()"""

#poo

#una clase no es mas que un contenedor o molde donde vamos almacenar difernetes objetos

"""class Auto:
    marca = "Nissa "
    modelo = 2004
    placa = " 1345"
    
taxi = Auto()
print(taxi.placa)



class Persona:
    doctor = "andres"
    
print(Persona.doctor)



class Jugadores:
    j1 = "messi"
    j2 = "iniesta"
    
    
    
class Jugadores_1:
    j3 = "perro"
    j1 = "sexo"
    
print(Jugadores.j2)
    
    
class nombre:
    pass
    
victor = nombre()
narem = nombre()

victor.edad = 18
victor.sexo = "trans"
victor.pais = "US"


narem.edad = 30
narem.sexo = "femenino"
narem.pais = "peru"

print(victor.edad)
print(narem.sexo)"""


"""print()

acumulador = 0
acumulador1 = 0
while True:
    x = float(input("Ingrese el valor unitario del producto: "))
    print()
    y = input("¿El producto cuenta con IVA? S/N: ")
    print()
    z = int(input("ingrese cantidad de productos a llevar: "))
    print()
    print("****************************************************")
    
    if y=="S":
        acumulador = (x + 0.19 * x) * z
        print("Porducto con IVA")
        print()
        print("Subtotal es: ", acumulador)
        print()
        print("**************************************************")
        
    
    elif y=="N":
         acumulador1 = (acumulador1 + x) * z
         print("Producto sin IVA")
         print()
         print("SuTotal es: ", acumulador1)
         print()
         print("**************************************************")
    mas = input("¿Desea agregar mas productos a su compra? S/N ")
    if mas=="N":
        print("Precio total es: ",acumulador1 )
        print()
        print("gracias por usar nuestro servicio!")
        
        break
    elif mas=="S":
        x = float(input("Ingrese el valor unitario del producto: "))
        print()
        y = input("¿El producto cuenta con IVA? S/N: ")
        print()
        z = int(input("ingrese cantidad de productos a llevar: "))
        print()
        print("****************************************************")
    elif y=="S":
        acumulador1 = (x + 0.19 * x) * z
        print("Porducto con IVA")
        print()
        print("Subtotal es: ", acumulador1)
        print()
        print("**************************************************")"""
"""acumulador = 0
acumulador1 = 0
x = int(input("ingrese cantidad de productos: "))       
for i in range(x):
    print()
    x = float(input("Ingrese el valor unitario del producto: "))
    print()
    y = input("¿El producto cuenta con IVA? S/N: ")
    print()
    z = int(input("ingrese cantidad de productos a llevar: "))
    print()
    print("****************************************************")
    if y=="S":
        acumulador = (x + 0.19 * x) * z
        print("Porducto con IVA")
        print()
        print("Subtotal es: ", acumulador)
        print()
        print("**************************************************")
        
    
    elif y=="N":
         acumulador1 = (acumulador1 + x) * z
         print("Producto sin IVA")
         print()
         print("SuTotal es: ", acumulador1)
         print()
         print("**************************************************")

print("precio total de su compra es: ",acumulador + acumulador1)"""

"""lista = [i**2 for i in range(1,21) if i%2==0]
print(lista)
    
#funcion map   
lista = [1,2,3,4,5,6,7,8,9,10]

def map_funcion(m):
    return m**3

x = list(map(map_funcion, lista))
print(x)"""

#funcion filter
"""lista = [1,2,3,4,5,6,7,8,9,10]

def filter_funcion(prueba):
    if prueba>=5:
        return True

z = list(filter(filter_funcion, lista ))
print(z)"""

#funcion reduce

"""from functools import reduce

lista = [1,2,3,4,5,6,7,8,9,10]

def reduce_funcion(m,n):
    return m+n

a = reduce(lambda m,n: m+n,lista)
print(a)"""



#lista = [i for i in range(1,20) if i%2==0 else: i%2==1]
#print(lista)

"""z = list(range(1,21))
print(z)


def excepciones():
    try:
        num1 = int(input("ingrese un numero:"))
        print()
        num2 = int(input("ingrese otro numero:"))
        r = num1/num2
        print("su division es: ", r)
    except ZeroDivisionError:
            print("no puedes dividir entre cero!")
    except ValueError:
            print("debes igresar un digito!")
        
excepciones()"""


""""a = [3, 2, 4, 1]
x =a.sort(reverse=True)
print(a)

b = [i for i in a ]
print(b)"""

"""class Auto:
    def __init__(self, color, tamano):
        self.color = color
        self.tamano = tamano
        
mi_auto = Auto("red",14)
mi_auto = Auto()
print(mi_auto.color)
print(mi_auto.tamano)"""

"""t = [i for i in range(1,101) if i%2!=0]
print(t)


def recorrer(x):
    return x**2
    
z = list(map(recorrer, t))
print(z)"""


"""class Persona:
    def __init__(self,edad): #si quiero cambiar edad de pedro agrego un nuevo parametro
        self.edad=edad
        #self.edad=20
        self.sexo="femenino"
        self.origen="european"
    
    def hablar(self, mensaje):
        print(mensaje)
        
pedro = Persona(25)
juan = Persona(30)

print("soy pedro y mi edad es: ",pedro.edad)
print("soy juan y mi edad es: ",juan.edad)


pedro.hablar("soy pedro y puedo comunicarme")"""

#herencia en python   
"""class Estudiante:
    #def __init__(self):
        nombre= "andres"
        edad=22
        
        
        
        def Caminar(self,x):
            print(x)
        
    
    
class Profesor(Estudiante):
    curso = "Java"
    numero = 60
    
    
maestro = Profesor()

print(maestro.nombre)
print(maestro.curso)
maestro.Caminar("Si, puedo caminar")"""
    
"""class Perro:
    def __init__(self, nombre, edad, raza):
        self.nombre=nombre
        self.edad=edad
        self.raza=raza
    
    def Caminar(self):
        print("si, puedo caminar")
        
Perro("turbo", "sexo", "pitbu")"""  

import os 

"""while True:
    bomba_logica = "Probando"
    if bomba_logica.startswith("s"):
        break
    else:
        print("0 1 0 1 1 1 0 1 11 01 ",end="")
print("Fuera del bucle!")"""



"""import heapq

x = [1,2,3,4,5,60,120,40,65]
print(heapq.nsmallest(2,x))"""




class Padre:
    def __init__(self,brazos,piernas,cabeza,torso):
        self.brazos = brazos  
        self.piernas =piernas
        self.cabeza = cabeza
        self.torso = torso
        
    def herencia(self):
        print(f" mi nombre es padre {self.brazos}, {self.piernas}, {self.cabeza}, {self.torso}")
    
Juan = Padre("tengo brazos", "tengo", "piernas", "tengo torso")

Juan.herencia()

class Hijo (Padre):
    def __init__(self, brazos, piernas, cabeza, torso, piel, cabello, ojos):
        super().__init__(brazos, piernas, cabeza, torso)
        self.piel=piel
        self.cabello=cabello
        self.ojos=ojos
    def Herencia(self):
        print(f" mi nombre es Hijo {self.brazos}, {self.piernas}, {self.cabeza}, {self.torso} mi color de piel es {self.piel} mi cabello es {self.cabello} mis ojos son {self.ojos}")
     
    

andres = Hijo("tengo brazos", "tengo piernas", "tengo cabeza" , "tengo torso", "marron", "negro", "verdes")


andres.Herencia()


def decorador(funcion):
    def nuvea_funcion():
        print("primero hago esto ")
        
    funcion()
    print("despues hago esto")
    return nuvea_funcion
@decorador  
def suma():
    print("ejecutame")


suma()    

def prueba(*args):
    return args
    
print(prueba("sexo", 12, True, 1,2))
    
    
def otro(**kwargs): #me retorna un diciconario, 
    return kwargs
    
print(otro(x=True, y="vacio", z=12))


def resta(m=10,c=5):
    return m-c
    
print(resta())
"""
n = 8

z = n * (n + 1)/2
print(z)

fact = [1,2,3,4,5]

from functools import reduce
def fact_num(x,y):
    return x*y

r = reduce(list(lambda m,n: m*n, ))
print(z)"""


"""from functools import reduce

n = [1,2,3,4,5]

def ran(e,w):
    return e*w

funcion = reduce(ran,  n)
print(funcion)


def cuadrado(m):
    return m**2
    
prueba = list(map(cuadrado, n))
print(prueba)

n = [i for i in range(1,101) if i%2!=0]
print(n)


def filtrar(f):
    if f>20:
        return True
        
p = list(filter(filtrar, n))
print(p)

contador = 0
acumulador = 0
for i in range(6):
    num1 = int(input(f"ingresa numero {i+1}: "))
    if num1%2==0:
        contador+=1
    else:
        acumulador+=num1
print("numeros pares ingresados: ", contador)
print("suma de numeros impares ingresados: ", acumulador)"""


"""class papa:
    def __init__(self,cabello, ojos, nariz):
        self.cabello=cabello
        self.ojos=ojos
        self.nariz=nariz
    
    def Herencia(self):
        print(f"mi nombre es pedro tengo cabello{self.cabello} mis ojos son de color {self.ojos} mi tipo de nariz es {self.nariz}")
        print()
        
pedro = papa("rubio", "red", "grande")
pedro.Herencia()


class Hijo(papa):
    def __init__(self,cabello, ojos, nariz, herencia_monetaria, negocio, computador):
        super().__init__(cabello, ojos, nariz)
        self.herencia_monetaria=herencia_monetaria
        self.negocio=negocio
        self.computador=computador
        
    def heredo(self):
        print(f"mi nombre es andres, mi tipo de cabello es {self.cabello} mi color de ojos es {self.ojos} mi tipo de nariz es {self.nariz} mi papa me heredo una herencia de {self.herencia_monetaria} y un negocio de {self.negocio} y un computador de marca {self.computador}")
        return self.herencia_monetaria + 1000000
    
    
    
andres = Hijo("rubio", "marron", "grande", 1.500000, "tienda", "intel")

andres.heredo()"""



"""class Padre:
    def __init__(self, name, edad,sexo):
        self.name=name
        self.edad=edad
        self.sexo=sexo

    def Presentarme(self):
        print(f"mi nombre es {self.name} tengo {self.edad} anos, sexo {self.sexo}")

juan = Padre("pedro", 50, "femenino")
print()
print("************************************************************************")


class Hijo(Padre):
    def __init__(self, name, edad,sexo, nacionalidad, ID, sangre, estrato):
        self.nacionalidad=nacionalidad 
        self.ID=ID
        self.sangre=sangre
        self.estrato=estrato
        super().__init__(name, edad,sexo)
    def introduccion(self):

        print(f"mi nombre es {self.name} tengo {self.edad} anos, mi nacionalidad es {self.nacionalidad},mi  ID es {self.ID}, mi tipo de sangre es {self.sangre}, estrato {self.estrato}")
        

mario = Hijo("mario", 31, "hombre", "peruano", 3243242, "b+", 5)

mario.introduccion()



def suma(**KWORDS):
    return KWORDS
    
print(suma(sexo=True, nombre="andres", edad=30))"""

"""print("Generador de listas")
print()
lista= []

generador = int(input("¿Cuántas listas quiere escribir?")) 
print()

for i in range(generador):

    choose = int(input(f"Dígame cuántas palabras tiene la lista {i+1}: " ))
    for n in range(choose):
        
        word = input(f"Dígame la palabra {n+1}: ")
       
        lista.append(word)
        
        
        
print(f"la lista {i+1} es: ", lista)"""
    
 

        
"""class Persona:
    def __init__(self, nombre,edad, DNI):
        self.nombre=nombre
        self.edad=edad
        self.DNI=DNI
        
    def Mayor(self,edad):
        if edad>=18:
            return True
        else:
            return False
       
            
    def Mostrar(self):
        print(f"mi nombre es {self.nombre}, tengo {self.edad} anos mi DNI es {self.DNI}")
  
andres = Persona("andres", 18, "342342")
andres.Mostrar()
print("puede ingresar? ", andres.Mayor(10))
print(andres.edad)

https://www.niu.edu/writingtutorial/punctuation/quizzes/comma.htm"""
     
"""lista= []
lista1 = []  
z = int(input("Dígame cuántas palabras tiene la lista: "))
for i in range(z):

    num = input(f"Dígame la palabra {i + 1}: ")
    lista.append(num)

print("La lista creada es: ", lista)

x = int(input("Dígame cuántas palabras tiene la lista de palabras a eliminar: "))
for m in range(x):
    word = input(f"ingrese palabra {m+1}: ")
    lista.remove(word)
print("La lista de palabras a eliminar es: ",lista)
print("La lista nueva es: ", lista)"""
    
 
"""class Persona:
    def __init__(self, nombre,edad,sexo,ID,origen):
        self.nombre=nombre
        self.edad=edad
        self.sexo=sexo
        self.ID=ID
        self.origen=origen
        
    def Presentarme(self):
        print(f"mi nombre es {self.nombre}, mi edad es {self.edad} anos mi sexo es {self.sexo} mi ID ES{self.ID}, mi pais de orifen es {self.origen}")
        
andres = Persona("andres", 22, "femenino", "453453", "peruano")
andres.Presentarme()
print()
print("mi ID ES: ",andres.ID)
print("*********************************************************************************")

class Trabajador(Persona):
    def __init__(self, nombre,edad,sexo,ID,origen, sueldo, cargo, horario, empresa):
      super().__init__(nombre,edad,sexo,ID, origen)
      self.sueldo=sueldo 
      self.cargo=cargo
      self.horario=horario
      self.empresa=empresa
      
      
    def introduccion(self):
        print(f"mi nombre es {self.nombre}, mi edad es {self.edad} anos mi sexo es {self.sexo}, mi ID ES{self.ID}, mi pais de orifen es {self.origen} mi sueldo es {self.sueldo} mi cargo es {self.cargo}, mi horario es {self.horario}, trabajo en {self.empresa} ")
        
Juan = Trabajador("juan", 30, "hombre", "534543", "mexicano", 5.000000, "programador", "7-12pm", "amazon")

Juan.introduccion()"""


"""mierda = input("ingrese una frase: ")
mierda = mierda.replace(" ", "")

if mierda==mierda[::-1]:
    print("si es palindromo")
else:
    print("no es palindromo")"""
    
#Realizar un programa que conste de una clase llamada Alumno que tenga como atributos el nombre y la nota del alumno. Definir los métodos para inicializar sus atributos, imprimirlos y mostrar un mensaje con el resultado de la nota y si ha aprobado o no.´
    
"""class Alumno():
    def __init__(self, nombre, edad):
        self.nombre=nombre 
        self.edad=edad
        
    def Atributos(self):
        if self.edad>=18:
            return "es mayor de edad"
        else:
            return "no es mayor de edad"
            
    def presentarme(self):
        print(f"mi nombre es {self.nombre} mi edad es {self.edad}")
    
Andres = Alumno("andres", 15)
Andres.presentarme()
print(f"estudiante Andres es {Andres.Atributos()}")
print()
print("************************************************")

juan = Alumno("juan", 20)
juan.presentarme()
print(f"estudiante juan {juan.Atributos()}")"""

#Realizar un programa en el cual se declaren dos valores enteros por teclado utilizando el método __init__. Calcular después la suma, resta, multiplicación y división. Utilizar un método para cada una e imprimir los resultados obtenidos. Llamar a la clase Calculadora.

class Calculadora():
    def __init__(self):
        self.x=int(input("ingrese primer numero: "))
        print()
        self.y=int(input("ingrese segundo numero: "))
    
    def Suma(self):
        return self.x + self.y
        
    def mostrar(self):
        print(f"suma de {self.x} y {self.y}")
        
    def Resta(self):
        return self.x - self.y
        
    def Mostrar_resta(self):
        print(f"resta de {self.x} y {self.y}")
    
    def multiplicación(self):
        return self.x * self.y
        
    def presentar(self):
        print(f"multiplicación de {self.x} y {self.y}")
        
    def división(self):
        return self.x // self.y
        
    def shit(self):
        print(f"division de {self.x} y {self.y}")
        
print()
print("se creo un objeto SUMA") 
print()    
Probar = Calculadora()
Probar.mostrar()
print("suma es: ", Probar.Suma())
print()
print("********************************")
Probar.Mostrar_resta()
print("resta es: ", Probar.Resta())
print()
print("********************************")
Probar.presentar()
print("multiplicación es: ", Probar.multiplicación())
print("********************************")
print()
Probar.shit()
print("division es: ", Probar.división())



"""En un banco tienen clientes que pueden hacer depósitos y extracciones de dinero. El banco requiere también al final del día calcular la cantidad de dinero que se ha depositado.

Se deberán crear dos clases, la clase cliente y la clase banco. La clase cliente tendrá los atributos nombre y cantidad y los métodos __init__, depositar, extraer, mostrar_total.

La clase banco tendrá como atributos 3 objetos de la clase cliente y los métodos __init__, operar y deposito_total."""


 
