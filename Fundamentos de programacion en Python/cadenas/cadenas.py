from importlib.resources import Package
from msilib.schema import PublishComponent


print("mi nombre es \"andres\" ") #poner comialls dobles a una cadena
print(r"quiero \nsexo") #con r de raw no procesa nada dentro de esa cadena, se usa para ingresar rutas especificas para abrir archivos
print("""esta es una cadena
multilinea 
puede escribir varias lineas de 
codigo en las que
quiera""")

x = "100".isdigit() #esta funcion me arrojara un booleano si dicha cadena contiene solo  digitos
print(x)

x1 = "aacsac".isalpha() #esta funcion me arrojara un booleano si dicha cadena contiene  solo letras de A a Z
print(x1)

x2 = "aacsac".isalnum() #esta funcion me arrojara un booleano si dicha cadena contiene  solo letras y numeros 
print(x2)

x3 = "aacsac".islower() #esta funcion me arrojara un booleano si dicha cadena contiene  solo letras en minusculas
print(x3)

x4 = "acsac".isupper() #esta funcion me arrojara un booleano si dicha cadena contiene  solo letras en mayusculas
print(x4)

cadena1 = ",".join("mi monda sabe a ti") #metodo join me va aseparar cada elemento de mi cadena con una coma, dependiendo con que quiera separar dicho elemento
print(cadena1)

cadenax = "   mi    ".strip() #me borra espacios tanto adelante como por dentras de mi cadena
print(cadenax)
