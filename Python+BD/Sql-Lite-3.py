import sqlite3

miConexion = sqlite3.connect("GestiondeProductos2.db")
miCursor = miConexion.cursor()

miCursor.execute("SeLECT * FROM PRODUCTOS WHERE SECCION = 'DEPORTES'")

productos=miCursor.fetchall()#Devuelve una lista de tuplas
print(productos)

productos=miCursor.fetchmany(5)#Devuelve una lista de tuplas y devuelve solo 5
print(productos)

productos=miCursor.fetchone()#|Devuelve una lista de tuplas y devuelve solo 1
print(productos)

productos=miCursor.fetchone()#|Devuelve una lista de tuplas y devuelve solo 1
while productos != None:# el while se detiene cuando no hay mas datos
    print(productos)
    productos=miCursor.fetchone()#|Devuelve una lista de tuplas y devuelve solo 1

for i in miCursor:
    print(i)

miConexion.commit()
miConexion.close()