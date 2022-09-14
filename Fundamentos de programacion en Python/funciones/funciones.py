def numeroentero(): #funcion sin parametros
    print("python")

numeroentero()

def suma(x,y): #funcionconparametros
    return x+y
print(suma(4,6))

def suma(x,y,a,b):
    suma = x+y
    resta = a - b
    return suma, resta #retornar dos valores

primera_suma, segundaresta = suma(10,5,30,20) 
print("suma es: ", primera_suma)
print("resta es: ", segundaresta)

print(bin(12323))