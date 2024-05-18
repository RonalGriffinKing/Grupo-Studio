class Estudiante:
    def __init__(self,DNI,Nombre,Grupo):
        self.__DNI=DNI
        self.__Nombre=Nombre
        self.__Grupo=Grupo
        self.__Notas={}

    def Matricula(self,Asignatura):
        if Asignatura in self.__Notas.keys():
            return False
        else:
            self.__Notas[Asignatura]=[]
            return True
    
    def PonerNota(self,Asignatura,Nota):
        if Asignatura in self.__Notas.keys():
            self.__Notas[Asignatura].append(Nota)
            return True
        else:
            return False
        
    def NotaMedia(self,Asignatura):
        if Asignatura in self.__Notas.keys():
            Total=0
            for Nota in self.__Notas[Asignatura]:
                Total+=Nota
            media=Total/len(self.__Notas[Asignatura])
            return media
        else:
            return None
        
    def AsignaturasMatriculadas(self):
        print(f"Las asignaturas contratadas son:{list(self.__Notas.keys())}")
    
    def __str__(self):
        return f"El estudiante {self.__Nombre} con grupo {self.__Grupo} Tiene estas asignaturas {list(self.__Notas.keys())}"

Estudiante1=Estudiante("Z1069859L","Ronal","Daw")
Estudiante1.Matricula("PRG")
Estudiante1.Matricula("ALG")
Estudiante1.AsignaturasMatriculadas()
Estudiante1.PonerNota("PRG",10)
Estudiante1.PonerNota("PRG",7)
print("Tu media en PRG: ",Estudiante1.NotaMedia("PRG"))


print(Estudiante1)


