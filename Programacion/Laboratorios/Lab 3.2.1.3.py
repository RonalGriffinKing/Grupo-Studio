secret_number = 777

print(
"""
+==================================+
| ¡Bienvenido a mi juego, muggle!  |
| Introduce un número entero       |
| y adivina qué número he          |
| elegido para ti.                 |
| Entonces,                        |
| ¿Cuál es el número secreto?      |
+==================================+
""")
liberador=1

ingresado=int(input())
while liberador==1:
    if  ingresado==secret_number:
        print("Bien eres libre ahora")
        print("Tu numero es:",ingresado)
        liberador=0
    else:
        print("Estas atrapado en mi bucle")
        ingresado=int(input())
        