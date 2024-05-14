#buffer : Nos permite cargar datos en la memoria, con esto podremos leer o escribir en el archivo

fichero=open("C:/Users/brion/OneDrive/Documentos/GitHub/Grupo-Studio/Programacion/Nueva carpeta/Fichero.txt","r")

palabra=fichero.read()
print(palabra)

Lista=[]

for linea in fichero:
    buscarto=linea.find("Holi")
    if buscarto != -1:
        Lista.append(linea)

print(Lista)

fichero.close()
