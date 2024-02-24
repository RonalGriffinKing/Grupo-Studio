## Desde el cmd ejecutar: pip install Faker

from faker import Faker
from random import choices


fake = Faker()
print(fake.name())

## El [6,8] es la probabilidad de salir el primer argumento o el segundo.
## Podeis jugar con ellos pra simular distintas temporadas del año. Más ocupación o menos
## Por ejemplo si poneis [1,0] estará todo lleno. Ya que la probabilidad de que salga el '-' es cero.
## Jugar con diferentes valores para probar.
negocio = [[["".join(choices([fake.name(), '-'], [1,0])) for _ in range(40)] for _ in range(15)] for _ in range(3)]

for i in negocio:
    print(i)

##print(negocio)

ocupadas = 0
libres = 0
for hotel in negocio:
    for planta in hotel:
        for habitacion in planta:
            if habitacion != '-':
                ocupadas += 1
            else:
                libres += 1

print("Habitaciones ocupadas:", ocupadas)
print("Habitaciones libres:", libres)

##EJERCICIOS PROPUESTOS

##Programa gestion de hoteles. Basica
##------------------------------------------
##Nivel de habitaciones ocupadas y libres en el negocio. (Dada ya por el profesor)
##
##A realizar por el alumno
##-------------------------------------------
##Calcular las ganancias totales. (Imaginamos un valor por habitacion)
##Desglose de ganancias por hoteles.
##Todo lo anterior pero dependiendo la habitación y/o hotel y/o planta vale mas o menos dinero.
##Saber que plantas son las más demandadas.
##Listado de las X habitaciones favoritas y las menos demandadas.
##Aplicar un descuento a los primeros 30 clientes de cada hotel.
##Debe salir en el precio total con el desglose de los descuentos y en que habitaciones o nombres se dio.
##Hacer registro de gente pero como si ciertas plantas y/o habitaciones, no pueden reservarse por X motivos.
##Simular distintas temporadas dependiendo de donde están los hoteles y calcular los ejercicios anteriores.
##Se trata de hacer o intentar que se parezca lo más posible a una aplicación real.
##Toda mejora o implementacion extra sera bienvenida.
##Darle vida de forma aleatoria que durante X tiempo clientes vayan y vengan e interactuen con la app.
##Modo SIMS durante X tiempo que vaya solo y al final nos de como las stats del dia.
