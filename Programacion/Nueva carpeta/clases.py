class Pastel:
    #Creacion de clase y su constructor
    def __init__(self,sabor,ingredientes):
        self.sabor = sabor
        self.ingredientes = ingredientes

    #Metodo de la clase
    def mostrar(self):
        print("Sabor:",self.sabor)
        print("Ingredientes:",self.ingredientes)
    
    #Creacion de objetos

class Entregar:
    #Creacion de clase y su constructor
    def __init__(self,direccion,fecha,cliente):
        self.direccion = direccion
        self.fecha = fecha
        self.cliente = cliente

    #Metodo de la clase
    def mostrar(self):
        print("Direccion:",self.direccion)
        print("Fecha:",self.fecha)
        print("Cliente:",self.cliente)

p1 = Pastel("Fresa",["Masa","Crema","Fresa"])#Primero se crea el objeto p1 y a este se le asigna la clase Pastel con sus atributos
p1.mostrar()

e1 = Entregar("Calle 1","10/10/2022","Juan")#Segundo se crea el objeto e1 y a este se le asigna la clase Entregar con sus atributos
e1.mostrar()




