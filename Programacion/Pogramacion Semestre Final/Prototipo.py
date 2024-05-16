
from copy import deepcopy


class Enemigo:
    def __init__(self):
        self.nombre=None
        self.vida=None
        self.fuerza=None
    def __str__(self):
        return f"{self.nombre} Tiene {self.vida} de vida  y {self.fuerza} de fuerza"
    
    def clonar(self):
        return deepcopy(self)
    
enemigo_original=Enemigo()
enemigo_original.nombre="Koopa"
enemigo_original.vida=100
enemigo_original.fuerza=100

print("Enemigo Original:",enemigo_original)

enemigo_clonado=enemigo_original.clonar()
enemigo_clonado.nombre="Orco jefe"
enemigo_clonado.vida=100
enemigo_clonado.fuerza=100

print("Enemigo Clonado",enemigo_clonado) 