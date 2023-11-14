
asignaturas=[]
notas=[]
while True:
    asignatura=input("Ingrese las asignaturas y -1 para ingresar notas:")
    if asignatura=="-1":
        break
    else:
        asignaturas.append(asignatura)
    
    
largo=len(asignaturas)

for i in range(largo):
    print(asignaturas[i])
    nota=int(input("Ingresa la nota:"))
    notas.append(nota)
    
    
for i in range(largo):
    print("Tus notas en",asignaturas[i],"es:",notas[i])
    
    
    
    