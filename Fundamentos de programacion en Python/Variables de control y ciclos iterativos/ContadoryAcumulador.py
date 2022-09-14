cont = 0
for var in range(1,4):
	num = int(input("ingrese numero de paquetes: "))
	if num % 2 == 0:
		cont = cont + 1
print("Has introducido ",cont," números pares.")
#ejercicioconcontador




#ejercicioconacumulador
suma = 0
for var in range(1,5):
	num = int(input("Dime un número:"))
	if num % 2 == 0:
		suma = suma + num
print("suma de # pares es:",suma)