#operaciones entre conjuntos
#principales:  unión, intersección y diferencia.

a = {1,2,3,4}
b = {4,2,5,6}
print(a|b) #me vaa unir los conjuntos y  a retornar los elementos que se encuentran en uno de lso dos conjuntos(no se repiten)

a1={1,2,3,4}
a2={1,2,5,6}
print(a1 & a2) #me retorna los elementos repetidos de ambos conjutnos

a3={1,2,3,4}
a4={4,5,4,6,7}
print(a3 - a4) #diferencia, me retorna elementos que no estam en mi segundo conjunto o viscebersa 
print(a3 ^ a4) #diferencia simetrica: retorna un nuevo conjunto el cual contiene los elementos que pertenecen a alguno de los dos conjuntos

x = {1,2,3,4}
m = {4,1,2,34,4}
x.add("monda")
print(x)

x.discard("monda")
print(x)
print(a.issubset(m))#saber si conjunto x es un subconjunto de m

#z = frozenset({4,5,3,1})#usamos esta funcion para hacer conjunto inmutable
#z.add("python")
#print(z)

lista1= [1,4,3,1,"andres", "maria", 22,22, True, False, "maria", "pedro"]
lista2 = [1,2,3,"andres", "wez", 21,22, True, 32.134, "andres", "true eme"]

#borrar elementos repetidos de ambas listas

x= set(lista1)
y = set(lista2)

union = list(x | y)

interseccion = list(x & y) 
print(union)
print(interseccion)