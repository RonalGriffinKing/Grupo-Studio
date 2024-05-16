class Coche:

    def __init__(self, marca, modelo, precio,motor):
        self.marca = marca
        self.modelo = modelo
        self.precio = precio
        self.motor = motor
        self.encendido = False
        
    
    def __str__(self):
        return f"Coche {self.marca} {self.modelo} {self.precio} "
    
    def __repr__(self):
        return f"Coche {self.marca} {self.modelo} {self.precio}"
    
    def enceder(self):
        self.encendido = True
    def apagar(self):
        self.encendido = False
    def Estado(self):
        if self.encendido:
            return("El coche esta encendido.")
        else:
            return("El coche esta apagado")

class Motor:
    def __init__(self,cilindros,cv,potencia):
        self.cilindros = cilindros
        self.cv = cv
        self.potencia = potencia
    
    def __str__(self):
        return f"Motor {self.cilindros} {self.cv} {self.potencia}"

    def __repr__(self):
        return f"Motor {self.cilindros} {self.cv} {self.potencia}"
    

coche1 = Coche("Hyundai", "i20", 13000, Motor(5, 1, 20))
print(f"{coche1}\n{coche1.motor}\n{coche1.Estado()}")
while True:
    opcion=input("Ingresa 1 para encender el coche o 2 para apagar: ")
    if opcion == "1":
        coche1.enceder()
        print(coche1.Estado())
    elif opcion == "2":
        coche1.apagar()
        print(coche1.Estado())
    else:
        break
