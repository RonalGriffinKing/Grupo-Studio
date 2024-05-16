import csv

# Abre el archivo CSV
with open("informacion.csv", newline='') as csv_file:
    # Lee el archivo como un diccionario
    csv_reader = csv.DictReader(csv_file, delimiter=",")
    
    # Inicializa el contador de líneas
    line_count = 0
    
    # Itera sobre cada fila en el archivo CSV
    for row in csv_reader:
        # Si es la primera fila (encabezado)
        if line_count == 0:
            # Imprime los nombres de las columnas
            print(f"Las columnas del CSV son: {', '.join(row)}")
        
        # Si no es la primera fila (datos)
        msg = "{} que trabaja en el departamento {} cumple años el mes {} de {}" 
        print(msg.format(row["Nombre"], row["Departamento"], row["Cumpleaños"], row["Mes"]))
        
        # Incrementa el contador de líneas
        line_count += 1

# Imprime el número total de líneas leídas
print("Se han leído {} líneas".format(line_count))
