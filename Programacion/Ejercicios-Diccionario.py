#Escribir un programa que guarde en una variable el diccionario 
#{'Euro':'€', 'Dollar':'$', 'Yen':'¥'}, pregunte al usuario por 
#una divisa y muestre su símbolo o un mensaje de aviso si la divisa no está 
#en el diccionario


#llaves={"Euro":"€", "Dollar":"$", "Yen":"¥"}
#divisa=input("Ingresa una divisa: ")
#while divisa not in llaves:
#    print("La divisa no existe")
#    break
#else:
#    print(llaves[divisa])


#Ejercicio 2
#Escribir un programa que pregunte al usuario su nombre, edad, dirección 
#y teléfono y lo guarde en un diccionario. Después debe mostrar por 
#pantalla el mensaje: <nombre> tiene <edad> años, vive en 
#<dirección> y su número de teléfono es <teléfono>.

#Llaves={"Nombre":"", "Edad":"", "Dirección":"", "Teléfono":"", "Casa":"", "Calle":""}
#largo=len(Llaves)
#for i in Llaves:
#    Llaves[i]=input(f"Ingresa tu {i}: ")
#print(Llaves)


#Escribir un programa que guarde en un diccionario los precios de las 
#frutas de la tabla, pregunte al usuario por una fruta, un número de kilos y 
#muestre por pantalla el precio de ese número de kilos de fruta. Si la fruta 
#no está en el diccionario debe mostrar un mensaje informando de ello.
#Fruta Precio
#Plátano 1.35
#Manzana 0.80
#Pera 0.85
#Naranja 0.7

#Llaves={"Platano":1.35, "Manzana":0.80, "Pera":0.85, "Naranja":0.7}

#while True:
#    try:
#        Fruta=input("Ingresa una fruta: ")
#        Llaves[Fruta]
#        break
#    except KeyError:
#        print("La fruta no existe")
#while True:
#    try:
#        Kilo=int(input("Ingresa un numero de kilos: "))
#        break
#    except KeyError:
#        print("No es un numero")
#print("El total es:",Llaves[Fruta]*Kilo)


#Ejercicio 4
#Escribir un programa que almacene el diccionario con los créditos de las 
#asignaturas de un curso {'Matemáticas': 6, 'Física': 4, 
#'Química': 5} y después muestre por pantalla los créditos de cada 
#asignatura en el formato <asignatura> tiene <créditos> créditos, 
#donde <asignatura> es cada una de las asignaturas del curso, y 
#<créditos> son sus créditos. Al final debe mostrar también el número 
#total de créditos del curso.

#Creditos={"Matemáticas":6, "Física":4, "Química":5}
#total=0
#for i in Creditos:
#    print(i, "tiene", Creditos[i], "Creditos")
#    total+=Creditos[i]

#print("El total de Creditos es:", total)


#Ejercicio 5
#Escribir un programa que cree un diccionario de traducción españolinglés. El usuario introducirá las palabras en español e inglés separadas 
#por dos puntos, y cada par <palabra>:<traducción> separados por 
#comas. El programa debe crear un diccionario con las palabras y sus 
#traducciones. Después pedirá una frase en español y utilizará el 
#diccionario para traducirla palabra a palabra. Si una palabra no está en el 
#diccionario debe dejarla sin traducir.


#print("Ingresa una palabra en Español : luego en ingles, si quieres agregar mas separalos por comas:")
#palabra=input()
#diccionario={palabra}
#print(diccionario)

#for i in diccionario:
#    print(i)
