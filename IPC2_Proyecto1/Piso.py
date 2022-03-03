from ListaPatron import ListaPatron
from ListaCelda import ListaCelda
class Piso():
    def __init__(self,nombre, Ro, Co, Fi, Si):
        self.nombre = nombre
        self.Ro = Ro
        self.Co = Co
        self.Fi = Fi
        self.Si = Si
        self.lista_patron = ListaPatron()
        self.lista_celda = ListaCelda()
        self.siguiente=None

    def getPatron(self):
        return self.lista_patron
    
    def getCelda(self):
        return self.lista_celda
    
    def getNombre(self):
        return self.nombre
    
    def getRo(self):
        return self.Ro

    def getCo(self):
        return self.Co
    
    def getFi(self):
        return self.Fi

    def getSi(self):
        return self.Si

    def getSiguiente(self):
        return self.siguiente

    def setNombre(self, nombre):
        self.nombre = nombre
    
    def setRo(self, Ro):
        self.Ro = Ro

    def setCo(self, Co):
        self.Co = Co

    def setFi(self, Fi):
        self.Fi = Fi

    def setSi(self, Si):
        self.Si = Si

    def setSiguiente(self,nodis):
        self.siguiente=nodis
    