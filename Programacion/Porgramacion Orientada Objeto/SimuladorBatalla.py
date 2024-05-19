from random import random, randint, choice

class Guerrero:
    def __init__(self, nombre):
        self.nombre = nombre
        self.vida = 100
        self.fuerza = randint(20, 50)
        self.precision = randint(80, 95)  # Aumentar precisión para mejorar el balance
        self.velocidad = randint(40, 70)
        self.defensa = 20

    def golpear(self, enemigo):
        probabilidad = max((self.precision - enemigo.velocidad) / 100, 0.5)  # Asegurar una probabilidad mínima de 50%
        daño = max(self.fuerza - enemigo.defensa + randint(-5, 5), 10)  # Asegurar un daño mínimo de 10
        if probabilidad >= random():
            enemigo.vida -= daño
            print(f"El guerrero {self.nombre} ha hecho un daño de {daño} a {enemigo.nombre}")
        else:
            print(f"El guerrero {self.nombre} falló el ataque contra {enemigo.nombre}.")

    def esta_vivo(self):
        return self.vida > 0

    def __str__(self):
        return f"El jugador {self.nombre} tiene {self.vida} de vida"


# Inicializar el juego
nombre_luchador1 = input("J1 Ingresa el luchador que quieres Superman, Goku, Chuck: ").capitalize()
nombre_luchador2 = input("J2 Ingresa el luchador que quieres Superman, Goku, Chuck: ").capitalize()

jugador1 = Guerrero(nombre_luchador1)
jugador2 = Guerrero(nombre_luchador2)

# Decidir quién empieza
dado = choice([True, False])  # True para jugador1, False para jugador2
print("Escogiendo quién golpea primero:")
if dado:
    print("Jugador J1 golpea ahora")
else:
    print("Jugador J2 golpea ahora")

# Simular la batalla
while jugador1.esta_vivo() and jugador2.esta_vivo():
    if dado:  # Turno de jugador1
        jugador1.golpear(jugador2)
        if not jugador2.esta_vivo():
            print(f"{jugador2.nombre} ha perdido")
            break
        dado = False  # Cambiar turno
    else:  # Turno de jugador2
        jugador2.golpear(jugador1)
        if not jugador1.esta_vivo():
            print(f"{jugador1.nombre} ha perdido")
            break
        dado = True  # Cambiar turno

# Mostrar el estado final de los jugadores
print(jugador1)
print(jugador2)
