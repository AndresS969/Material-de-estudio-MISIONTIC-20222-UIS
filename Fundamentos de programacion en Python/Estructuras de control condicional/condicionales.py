
"""#estructuras de control condicional
numero_dehoras = float(input("ingrese numero de horas trabajdas:"))
coste_porhoras = float(input("ingrese coste x horas:"))
paga = numero_dehoras * coste_porhoras
print("su suedo es:", paga)

#otro

nombre = input("ingrese su nombre:")
edad = int(input("ingrese su edad"))
if edad < 18:

    print("usted es menor de edad!")

else:

   print("usted es mayor de edad")

#otro
choose = int(input("ingrese un numero: "))
if choose>0: #un numero positivo es mayor a 0, menor a 0 es negarivo
    print("es positivo")
elif choose==0:
    print("es cero")
else:
    print("no es positivo")


#otro 
#codicional anidados: un if dentro de otro if, una condicion dentro de oyra condicion

choose2 = int(input("ingrese su edad: "))
if choose2>0:
    print("edad correcta!")
    if choose2>=18:
        print("usted es mayor de edad!")
else:
    print("edad incorrecta")"""



print("\t\t\tcajero automatico")

saldo = 100000
print("menu de opciones:")
print("1)ingresar dinero en la cuenta")
print("2)retirar dinero de la cuenta ")
print("3)mostrar dinero disponible")
print("4)salir")

choose = int(input("escoga una opcion: "))
if choose==1:
    choose2 = int(input("¿cuanto dinero desea ingresar a su cuenta?"))
    total = choose2 + saldo
    print(f"total dinero en su cuenta: ", total)
elif choose==2:
    choose3 = int(input(f"¿cuanto dinero desea retirar de su cuenta?: "))
    total1 = saldo  - choose3
    print(f"usted ha retirado: {choose3}")
    print(f"saldo restante:{total1}")
elif choose==3:
    total2 = saldo
    print(total2)
elif choose==4:
    print("gracias por su cooperacion")