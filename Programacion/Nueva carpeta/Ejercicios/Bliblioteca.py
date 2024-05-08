#Crear biblioteca con su nombre ciudad libro
#Libro tiene titulo y autor

class Biblioteca:

    def __init__(self,nombre,ciudad):
        self.nombre = nombre
        self.ciudad = ciudad
        self.libros = []
    
    def muestraBiblioteca(self):
        print("Nombre:",self.nombre)
        print("Ciudad:",self.ciudad)
        print("Libros:",self.libros)
    
    def AgregarLibro(self,libro):
        self.libros.append(libro)

class Libro:
    def __init__(self,titulo,autor):
        self.titulo = titulo
        self.autor = autor

    def __str__(self):
        return self.titulo

    def __repr__(self):
        return self.titulo

Biblioteca1=Biblioteca("Livraria","Medellin")
Libro1=Libro("Todas las hadas del reino", "Camila Salgado")
Libro2=Libro("Harry Potter y la camara secreta", "jk ")
Biblioteca1.muestraBiblioteca()
Biblioteca1.AgregarLibro(Libro1)
Biblioteca1.AgregarLibro(Libro2)
Biblioteca1.muestraBiblioteca()

