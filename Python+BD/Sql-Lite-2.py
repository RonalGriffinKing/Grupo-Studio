import sqlite3

miConexion = sqlite3.connect("GestiondeProductos2.db")

miCursor = miConexion.cursor()

VariosProductos = [
    ("Camara",20,"FOTOGRAFIA"),
    ("PANTALLA",40,"TELEFONIA"),
    ("TELEVISOR",100,"TELEFONIA")
]

miCursor.executemany("INSERT INTO PRODUCTOS VALUES (?,?,?)",VariosProductos)
miConexion.commit()
miConexion.close()