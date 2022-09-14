usuario = "william"
contrasena = "casa"
entrando = True

while entrando:
	intento_u = input("Ingresa el usuario: ")
	intento_c = input("Ingresa el contraseña: ")
	if intento_u == usuario and intento_c == contrasena:
		print("usuario y contraseña son correctos")
		entrando = False
	else:
		print("Usuario o contraseña incorrectos")
		
print("Ingresaste al sistema")