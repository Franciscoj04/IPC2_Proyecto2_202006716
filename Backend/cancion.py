class Cancion:
    def __init__(self,nombre,artista,genero,anio):
        self.nombre=nombre
        self.artista=artista
        self.genero=genero
        self.anio=anio

    def getCancion(self):
        return self