 
import random

class Persona:
    def __init__(self, nombre="Anonimo", edad=0, sexo="H", peso=0, altura=0):
        self.__nombre = nombre
        self.__edad = edad
        self.__DNI = self.__GeneraDni()
        self.__sexo = sexo
        self.__peso = peso
        self.__altura = altura
    
    def calcularIMC(self):
        imc=self.__peso/(self.__altura**2)
        if imc<20:
            return -1
        elif imc>=20 and imc<25:
            return 0
        else:
            return 1
        
    def elMayordelaEdad(self):
        if self.__edad>=18:
            return True
        else:
            return False
    
    def __ComprobarSexo(self):
        if self.__sexo=="H":
            return "H"
        elif self.__sexo=="M":
            return "M"
        else:
            return "H"
    
    def __GeneraDni(self):
        DNI=random.randint(0,99999999)#99999999 es el maximo
        return DNI

    def __str__(self):
        return f"DNI: {self.__DNI} Nombre: {self.__nombre} Edad: {self.__edad} Sexo: {self.__sexo} Peso: {self.__peso} Altura: {self.__altura}"
    
    def setNombre(self, nombre):
        self.__nombre = nombre

    def setEdad(self, edad):
        self.__edad = edad

    def setSexo(self, sexo):
        self.__sexo = sexo

    def setPeso(self, peso):
        self.__peso = peso

    def setAltura(self, altura):
        self.__altura = altura

while True:
    nombre = input("Introduce tu nombre: ")
    if nombre.isalpha():
        break
    else:
        print("Por favor, introduce un nombre válido (solo letras).")

while True:
    try:
        edad = int(input("Introduce tu edad: "))
        break
    except ValueError:
        print("Por favor, introduce una edad válida (solo números).")

while True:
    sexo = input("Introduce tu sexo (H/M): ")
    if sexo.upper() in ["H", "M"]:
        break
    else:
        print("Por favor, introduce un sexo válido (H/M).")

while True:
    try:
        peso = float(input("Introduce tu peso (en kg): "))
        break
    except ValueError:
        print("Por favor, introduce un peso válido (solo números).")

while True:
    try:
        altura = float(input("Introduce tu altura (en metros): "))
        break
    except ValueError:
        print("Por favor, introduce una altura válida (solo números).")

persona = Persona(nombre, edad, sexo, peso, altura)
Persona1 = Persona("Juan",peso= 80, altura= 25)
Persona2 = Persona()
Persona2.setNombre("Pepe")
Persona2.setEdad(20)
Persona2.setSexo("M")



print(persona)
print(Persona1)
print(Persona2)


