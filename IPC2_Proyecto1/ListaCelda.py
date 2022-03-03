from Celda import Celda
import os
import webbrowser
class ListaCelda():
    def __init__(self):
        self.inicio2 = None
        self.size2 = 0

    def insertarCelda(self, Ro, Co, color):
        nuevo = Celda(Ro, Co,color)
        self.size2 += 1
        if self.inicio2 is None:
            self.inicio2 = nuevo
        else:
            tmp = self.inicio2
            while tmp.siguiente2 is not None:
                tmp = tmp.siguiente2
            tmp.siguiente2 = nuevo
            nuevo.anterior2 = tmp

    '''
    def getCelda(self):
        suma = 0
        tmp = self.inicio2
        while tmp is not None:
            suma  = suma+int(tmp.color)
            tmp = tmp.siguiente2
        return suma
    '''
    def imprimirDobleEnlaPa(self):
        tmp = self.inicio2
        while(tmp!=None):
            print(tmp.getRo()+" --- "+tmp.getCo()+" --- "+tmp.getColor())
            tmp = tmp.siguiente2

    