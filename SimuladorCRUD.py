"""estudiantes = int(input("ingrese la cantidad de estudiantes que desea agregar a la base de datos: "))
        
lista3 = []
lista2 = []
for i in range(estudiantes):
    
    e = input(f"ingrese estudiante numero {i+1}: ")
    lista3.append(e)
    print()
   
print("estudiantes agregados a la base de datos: ", lista3)
print()
eliminar = int(input("¿cuantos estudiantes desea eliminar de la base de datos? "))
print()
if eliminar>len(lista3):
    print("error, numero ingresado esta por encima del rango de la lista!")
    print()
    bandera = True
    while bandera:
        eliminar = int(input("¿cuantos estudiantes desea eliminar de la base de datos? "))
        print()
        if eliminar<len(lista3):
            print()
            print("el numero ingresado si esta en el rango de la  datos")
            bandera = False
        else:
            print()
            print("error, numero ingresado esta por encima del rango de la lista!") 
print()
try:
    for n in range(eliminar):
        delete = input(f"ingrese estudiante {n+1}: ")
        print()
        lista3.remove(delete)
        lista2.append(delete)
        if delete in lista2:
            print("estudiante eliminado de la base de datos!")
            print()
except ValueError:
    print(f"estudiante '{delete}' no se encuentra en la base de datos!")

print()
print("su nueva base de datos actualizada es: ", lista3)
print()
print("estudiantes eliminados de la base de datos: ",lista2 )"""



    