class Pelicula:
    opciones = ["opcion 1", "opcion 2"]
    def mostrar():
        print("Soy una pelicula")

    def add_option(self, option):
        self.opciones.append(option)
     
    def __init__(self, titulo, duracion, lanzamiento):
        self.titulo = titulo
        self.duracion = duracion
        self.lanzamiento = lanzamiento
        print(f"Nueva Pelicula: {titulo}")

    def __str__(self):
        return f"{self.titulo} ({self.lanzamiento})"

class CTALOGO:
    nombreCatalogo = ""
    peliculas = []

    def __init__(self, nombre, peliculas=[]):
        self.nombre = nombre
        self.peliculas = peliculas

    def agregar(self, p):
        self.peliculas.append(p)

    def printName(self):
        print(self.nombre)

    def mostrar(self):
        description = ""
        for p in self.peliculas:
            description += (f"{p}" + '\n' if p != self.peliculas[-1] else '' )
            return description

    def year_query(self, year):
        # self.peliculas.filter((x) => x.lanzamiento === year)
        return filter(lambda x: x.lanzamiento == year, self.peliculas)
        nueva_lista = []
        for p in self.peliculas:
            if p.lanzamiento == year:
                nueva_lista.append(p)
        return nueva_lista

p = Pelicula("El padrino", 175, 1972)
c= Catalogo("Cat1", [p])
c.printName()
c.mostrar()
print(c)
c.agrefar(Pelicula("El padrino 2", 200, 1974))
print(c)
print("----------------------------------")

print(Pelicula.opciones)
p.add_option("opcion 3")

p1 = Pelicula("Toy Story", 175, 1972)