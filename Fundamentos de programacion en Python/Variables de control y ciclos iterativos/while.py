"""a = 0 #acumulador
i = 1 #contador

n=int(input("digite cantidad de notas:"))
while n<=0:
	print("error, fuera de rango")
	n=int(input("digite cantidad de notas:"))
	
while i<=n:
	x=float(input("ingrese notas "+str (i)+ ": "))
	a=a+x
	i=i+1
p = a/n

print("promedio es:", p)"""
#contador: x=x +1
#acumulador: c = c + x


password = input("ingrese su usuario: ")
user = int(input("ingrese su contrasena: "))

while password!="andres" and user!=3144300:
    print("usuario y contraena incorrectos!")
    password = input("ingrese su usuario: ")
    user = int(input("ingrese su contrasena: "))
print("inicio de sesion exitoso!")

monda = input("ingrese un mensaje: ") #hacer que aparezca ese mismo mensaje 10 veces
for i in range(10):
    print(monda)

i = 0

while i<10:
    print("mi monda") #imprimir 10 veces ese mismo mensaje con un iterador
    i = i + 1 #por cada vuelta agrega un mensjae de mas

while True: #mejor forma para hacer un bucle while
    perra = int(input("ingresa un numero: "))
    if perra==1:
        break
    

    