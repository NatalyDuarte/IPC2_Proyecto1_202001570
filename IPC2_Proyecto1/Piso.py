from Listaenlazada import Listaenlazada
class Piso():
    def __init__(self,nombre, Ro, Co, Fi, Si):
        self.nombre = nombre
        self.Ro = Ro
        self.Co = Co
        self.Fi = Fi
        self.Si = Si
        self.siguiente=None
        self.Celda=Listaenlazada()