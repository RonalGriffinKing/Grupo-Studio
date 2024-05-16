import csv

# Abre el archivo CSV
with open("informacion.csv","wt", newline='') as csv_file:
    # Crea un escritor CSV

    fieldnames=["Nombre", "Departamento", "Cumpleaños", "Mes"]


    csv_writer = csv.DictWriter(csv_file, fieldnames=fieldnames)

    # Escribe la primera fila (encabezado)

    # Escribe las siguientes filas (datos)
    csv_writer.writerow({"Nombre": "Carlos", "Departamento": "Desarrollo", "Cumpleaños": "10 de diciembre", "Mes": "diciembre"})

    csv_writer.writerow({"Nombre": "Marta", "Departamento": "Desarrollo", "Cumpleaños": "10 de diciembre", "Mes": "diciembre"})

    csv_writer.writerow({"Nombre": "Pedro", "Departamento": "Desarrollo", "Cumpleaños": "10 de diciembre", "Mes": "diciembre"})

    
