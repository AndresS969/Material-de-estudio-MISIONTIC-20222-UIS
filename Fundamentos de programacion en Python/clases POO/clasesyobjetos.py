#conceptos:
#un clase es un contenedor
#un clase tiene atributos y metodos
#atributos son caracteristicas de esa  clase
#metodos son acciones o funciones que hace esa  clase
#un objeto es una instancia de una  clase, unos perros son objetos de una  clase, 
#la  clase es una especie de molde de ese objeto
#una clase es un molde a partir del cual se crearan objetos, que tendras cualidades como atributos (caracteristicas), y meotodos/funciones)

class Perro:
    def __init__(self): # un constructor es una subrutina cuya misión es inicializar un objeto de una clase
        self.tamano = 0 #usamos self para agregar atribuos de ese objeto
        self.edad = 0
        self.color = 0
        self.raza = 0
        self.nombre = None

    #luego metodos que son mas que funciones
    def ladrar(self):
        print("puede ladrar")
    def comer(self):
        print("puede comer")
    def jugar(self):
        print("puede jugar")
    def cambiar_nombre(self,nombre):
        self.nombre = nombre
#instanciar un objeto

mi_perro = Perro()
mi_perro.comer()
print(mi_perro.raza)
mi_perro.cambiar_nombre("andres")
print(mi_perro.nombre)

#herencia POO


class Persona:
    def __init__(self, nombre, edad,CC):
        self.nombre=nombre
        self.edad=edad
        self.CC=CC
    
    def Presentarse(self):
        print(f"""
        mi nombre es: {self.nombre} 
        edad: {self.edad} años 
        mi CC es: {self.CC}""")
        

class Trabajador(Persona):
    def __init__(self, nombre, edad,CC,cargo,empresa,contrato):
        super().__init__(nombre,edad,CC)
        self.cargo=cargo
        self.empresa=empresa
        self.contrato=contrato
    def Empresa(self):
        print(f"""
                nombre:{self.nombre} 
                edad: {self.edad} años 
                mi CC es: {self.CC} 
                trabajo: {self.cargo} 
                empresa: {self.empresa} 
                mi cargo es: {self.contrato}""")
        
print("Super class Persona")
print()
juan = Persona("juan",34,"342432")
print()
juan.Presentarse()

print("***********************************************************************")


andres = Trabajador("andres", 22,"342422334", "programador", "amazon", "indefinido")
andres.Empresa()