"""from turtle import color
from matplotlib import pyplot 

x = ["andres", "maria", "juan", "diego", "pedro"]
y = [3.2, 5, 2.1, 1, 4.5]
colores = ["green", "blue", "pink", "red", "purple"]
pyplot.title("nota de estudiantes")
pyplot.bar(x, height=y, color=colores, width=0.7)
pyplot.xlabel("Nombres(n)")
pyplot.ylabel("notas(n)")

pyplot.show()"""


"""print("programa para graficar notas de estudiantes")
print()

ingresa = int(input("ingresa cantidad de estudiantes: "))
coloresx = ["green", "blue", "red", "yellow","black"]
x = []
y = []
for i in range(ingresa):
    ingresa2=input(f"ingresa nombre de estudiante {i+1}: ")
    notas = int(input(f"ingresa nota de estudiante{i+1}: "))
    print("*****************************************************************")
    x.append(ingresa2)
    y.append(notas)
pyplot.title("Grafica de notas de estudiantes")
#pyplot.plot(x, y, marker="o") #recibe dos argumentos, las dos listas, muestra una grafica lineal, usamos marker para agregar puntos
pyplot.xlabel("nombres (n)") #para agregar mensajes 
pyplot.ylabel("Notas (n)")"""
"""pyplot.bar(x, height=y, color=coloresx, width=0.7) 
pyplot.xlabel("nombres (n)") #para agregar mensajes 
pyplot.ylabel("Notas (n)")
pyplot.show()"""

from matplotlib import pyplot

"""print("programa para graficar notas de estudiantes")
print()
ingresa = int(input("ingresa cantidad de estudiantes: "))
coloresx = ["green", "blue", "red", "yellow","black"]
x = []
y = []
for i in range(ingresa):
    ingresa2=input(f"ingresa nombre de estudiante {i+1}: ")
    notas = int(input(f"ingresa nota de estudiante{i+1}: "))
    print("*****************************************************************")
    x.append(ingresa2)
    y.append(notas)
pyplot.title("Grafica de notas de estudiantes")
pyplot.plot(x, y, marker="o") 
pyplot.xlabel("nombres (n)") 
pyplot.ylabel("Notas (n)")
pyplot.bar(x, height=y, color=coloresx, width=0.7) 
pyplot.xlabel("nombres (n)") #
pyplot.ylabel("Notas (n)")
pyplot.show()"""


import os 

while True:
    bomba_logica = "Probando"
    if bomba_logica.startswith("s"):
        break
    else:
        print("0 1 0 1 1 1 0 1 11 01 ",end="")
print("Fuera del bucle!")
