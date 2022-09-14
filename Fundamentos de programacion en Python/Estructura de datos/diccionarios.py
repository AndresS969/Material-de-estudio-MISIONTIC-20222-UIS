
telefonos={"andres":3142354675, "juan":3212354675,"pedro":3162354675,"gato": 3132354675}
print(telefonos["juan"]) #diciconarios, acceder a un valo atraves de su clave

telefonos["wez"]=3145779144
print(telefonos) #agregar una nueva clave y valor

print(telefonos.keys()) #acceder claves diccionario
print(telefonos.values())#acceder valor diccionario
print(telefonos.items())#acceder claves y valroes diccionario

print(telefonos.get("andres")) #obtener un valor atraves de su clave
for i in telefonos.values(): #iterar sobre dicicionario y acceder a todos los valores, tambien podemos acceder a sus claves
    print(i)

claves = ["nombre","curso","ciclo"]
Valor = ["andres", "pyhton",3]
diccionario = dict(zip(claves, Valor)) #pasar de una lista a un diccionario
print(diccionario)

monda = {"monda":3,"encendido":True, "promedio":3.2}
z = list(monda)
print(z) #pasar diccionario a una lista

print("andres" in telefonos)
print("andres" not in telefonos)

diccionario1 = {"Euro":"€","Dollar":"$","Yen":"¥"}
divisa = input("ingrese una divisa: ")
if divisa=="Euro":
    print(diccionario1.get("Euro"))
elif divisa=="Dollar":
    print(diccionario1.get("Dollar"))
elif divisa=="Yen":
    print(diccionario1.get("Yen"))
else:
    print("divisa ingresada no se encuentra disponible!")


monda4 = {"monda":3,"encendido":True, "promedio":3.2}
del(monda4["monda"]) #para borrrar clave y valor de un diccionario
print(monda4)

prueba = {"andres":{"edad":22, "curso": "python"}, "java":12.4, }
print(prueba.get("adriana", "no existe esa monda")) #podemos asignar un mensaje si no existe una clave en nuestro dicicionario