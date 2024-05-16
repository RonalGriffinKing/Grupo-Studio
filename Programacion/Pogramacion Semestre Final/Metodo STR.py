# Metodo __STR__ y __REPR__ estos metodos nos permiten mostrar por pantalla el objeto creado por el usuario

#str es una representacion 


class triangulo:
    def __init__(self,base,altura):
        self.base = base
        self.altura = altura

    #Debe devolver un string que se mostrara en pantalla
    def __str__(self):
        clase=type(self).__name__
        msg="El {} con base {} y altura {} tiene un area de {}"
        return msg.format(clase,self.base,self.altura,self.area())# Format nos permite insertar variables dentro de la cadena
    
    #Metodo que calcula el area
    def area(self):
        return (self.base * self.altura) / 2
    
t=triangulo(10,5)
print(t)

class Triangulin( triangulo):
    pass
    def __str__(self):
        return "1:"+super().__str__()


tt=Triangulin(2,2)
print(tt)



class b:
    def __str__(self):
        super().__str__()
        return "b"

b = b()
print(b)