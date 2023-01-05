from cancion import Cancion
import json

class Gestor:
    def __init__(self):
        self.canciones=[]

    def agregar_cancion(self,nombre,artista,genero,anio):
        nuevo=Cancion(nombre,artista,genero,anio)
        self.canciones.append(nuevo)
        return True

    def obtener_canciones(self):
        json=[]
        for i in self.canciones:
            cancion={
                'nombre':i.nombre,
                'artista':i.artista,
                'anio':i.genero,
                'genero':i.anio
            }
            json.append(cancion)
        return json