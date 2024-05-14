#with open("Fichero.txt") as reader:
    #line=reader.readline()

    #while line!="":
        #print(line)
      # line=reader.readline()

   #for line in reader.readlines():
      # print(line)
    
   # for line in reader:
    #    print(line, end="")





with open("/Users/brion/OneDrive/Documentos/GitHub/Grupo-Studio/Programacion/Nueva carpeta/Fichero.txt") as reader:
    dog=reader.readlines()

with open("Fichero2.txt","wt") as writer:
    writer.writelines(dog)