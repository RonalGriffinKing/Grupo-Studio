from faker import Faker

def printeador(nombre, apellido):
    print(f"Hola {nombre} tu apellido es {apellido}")
for i in range(20):
    printeador(Faker("es_Es").first_name(),Faker("es_Es").last_name())
