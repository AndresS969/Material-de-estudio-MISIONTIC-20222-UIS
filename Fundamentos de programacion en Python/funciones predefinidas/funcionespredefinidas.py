suma = lambda n1, n2: n1 + n2
print(suma(2,3)) #expresion lambda: sirve para declarar de una forma corta y anonima una funcion


lista = [12,11,24,30,60,80,90,10,5,8]

def mayor(edad):
    if edad>=18:
        return True

edadesmayores = list(filter(mayor,lista))
print(edadesmayores)

texto = "mi monda sabe a ti"
print(texto.strip('mia')) #borrar caracteres de una cadena de texto

nombre = input("ingrese su nombre completo en la consola: ")
print(nombre.upper())
print(nombre.lower())
print(nombre.title()) #me devule las iniciales en mayuscula

from functools import reduce

z = range(1,6) #funcionreduceparaagregarfuncionesaobjetositerabe
funcion_reduce = reduce(lambda x,y: x*y, z)
print(funcion_reduce)

#funcion map   
lista = [1,2,3,4,5,6,7,8,9,10]

def map_funcion(m):
    return m**3

x = list(map(map_funcion, lista))
print(x)