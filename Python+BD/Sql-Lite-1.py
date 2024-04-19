import sqlite3

miConexion = sqlite3.connect("GestiondeProductos2.db")
#Tratara de conectarse a esta base de datos y si no eciste la crea

miCursor = miConexion.cursor()
#Nos permite ejecutar comandos SQL en la base de datos cursor indica que vamos a trabajar con una base de datos

#borrar la tabla
miCursor.execute("DROP TABLE IF EXISTS PRODUCTOS")


#Trataremos de crear tablas con try
try:
    miCursor.execute('''
        CREATE TABLE PRODUCTOS(
        ID INTEGER PRIMARY KEY AUTOINCREMENT,
        NOMBRE_Articulo VARCHAR(50) UNIQUE,
        Precio INTEGER,
        Seccion VARCHAR(20))
    ''')
except sqlite3.OperationalError:
    print("La  tabla ya existe")
    
    


#Limpiaremos la tabla de productos
    miCursor.execute("DELETE FROM PRODUCTOS")

#Trataremos de insertar datos con try
try:
    miCursor.execute("INSERT INTO PRODUCTOS VALUES(NULL,'BALON',15,'DEPORTES')")
    miCursor.execute("INSERT INTO PRODUCTOS VALUES(NULL,'CABLE',10,'CABLES')")
    miCursor.execute("INSERT INTO PRODUCTOS VALUES(NULL,'LAPTOP',20,'COMPUTACION')")
    miCursor.execute("INSERT INTO PRODUCTOS VALUES(NULL,'TECLADO',5,'COMPUTACION')")
    miCursor.execute("INSERT INTO PRODUCTOS VALUES(NULL,'CELULAR',15,'TELEFONIA')")

    miConexion.commit()#Guarda los datos en la base de datos

except sqlite3.OperationalError:
    print("La base de datos ya existe")
#Trataremos de insertar varios datos con try





try:
    miCursor.executemany("INSERT INTO PRODUCTOS VALUES (NULL,?,?,?)",( 
        ("Camara",20,"FOTOGRAFIA"),
        ("PANTALLA",40,"TELEFONIA"),
        ("TELEVISOR",100,"TELEFONIA")
    ))

    miConexion.commit()#Guarda los datos en la base de datos

except sqlite3.OperationalError:
    print("La base de datos ya existe")




miConexion.close()