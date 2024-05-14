import mysql.connector

# Establecer la conexión
conexion = mysql.connector.connect(
    host="localhost",
    user="root",
    password="1234",
    database="apple"
)

if conexion.is_connected():
    print("Conexión exitosa")

# Realizar operaciones con la base de datos
# Por ejemplo, ejecutar una consulta
cursor = conexion.cursor()
cursor.execute("SELECT * from iphones")

# Recuperar los resultados
resultados = cursor.fetchall()
for fila in resultados:
    print(fila)

# Cerrar el cursor y la conexión
cursor.close()
conexion.close()
