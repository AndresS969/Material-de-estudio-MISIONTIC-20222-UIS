#listasssss
lista2 = [1,2,3,3,4,5,6]
lista3 = [7,8,9,10,11,12,13]
print("java" in lista2) #saber si un hay un dato en una lista
print(lista2 [0]) #acceder al elemento de  la lista por su indice
print(sum(lista2)) #suma elementos de una lista
print(lista2 [2:6]) #escoger varios elementos de una lista(esto se le conoce como slicing)
print(len(lista2)) #saber cantidad de elementos de una lista
print(max(lista2)) #saber maximo de elementos de una lista
print(min(lista2)) #saber minimo de elementos de una lista
print(lista2.count(3))#saber cantidad de veces que se repite un elemento de una lista
lista2.extend(lista3) #anade datos al final de una lista
print(lista2)
lista2.append("Chat") #agrega un dato al final de una lista
print(lista2)

"""Crea una estructura con los meses del año.
 pide números al usuario, si el numero esta entre 1 y la longitud máxima de la estructura
 , muestra el contenido de esa posición sino muestra un mensaje de error. 
 El programa termina cuando el usuario introduce un cero"""

"""meses = ["Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio", "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre"]
salir = 0
while (salir == 0):
    numero = int(input("Escriba su número: "))
    if numero>=1 and numero<=len(meses):
        print(meses[numero-1])
    elif(numero == 0):
        salir = 1
    else:
        print("ERROR! Ingrese un número entre [1-12]")
print("Fin del programa")"""

asignaturas = ["Matemáticas", "Física", 1,2,3]*3 #esto hara que se repitan esos mismos elementos tres veces dentro de la lista
print(asignaturas)

asignaturas1 = [9,3,5,8,7,6,1,0]
asignaturas1.sort(reverse=True) #primero me ordena y despues de mayor a menor
print(asignaturas1)


x = ["andres", "maria", 22,22, True, False, "maria", "pedro"]
m = set(x)
cambiar =list(m) #eliminar items repetidos en una lista, primero pasamos esa lista a un conjunto, y automaticamanete se borran
print(cambiar)


lista = range(1,51) #agregar numeros que queramos a una lista de manera automatizada
print(list(lista))

#lista por comprension 
lista = [i**2 for i in range(1,21) if i%2==0]
print(lista)
    
