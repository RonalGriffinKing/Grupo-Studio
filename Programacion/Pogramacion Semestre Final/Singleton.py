
##Patrones de diseño son 5 los principales

#Patron SINGLETON
#SE USA PARA ASEGURAR QUE SOLO HAY UNA INSTANCIA DE UNA CLASE
#De la clase en todo el programa
#Es util para recursos compartidos como BD O Archivos

class Configuracion:
    __Instance=None

    def __new__(cls):
        if cls.__Instance is None:#Si la instancia es nula significa que no hay una instancia
            cls.__Instance=super().__new__(cls)#Esto crea una nueva instancia de la clase
        return cls.__Instance#Retorna la instancia
    
    def __init__(self):
        self.valor1="VALOR 1"
        self.valor2="VALOR 2"


objeto=Configuracion()#Crea una nueva instancia de la clase
objeto2=Configuracion()#Crea una nueva instancia de la clase

objeto.valor1="CAMBIO VALOR 1"
print(objeto.valor1)
print(objeto2.valor1)
print(objeto is objeto2)

#Esto nos permite solo tener una instancia y acunque generemos mas instancias solo utilizara la que se creo primera y con esa trabajar
#no generara otras
