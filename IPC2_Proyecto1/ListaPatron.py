from Patron import Patron
import os
class ListaPatron():
    def __init__(self):
        self.inicio1 = None
        self.fin1 = None
        self.size1 = 0

    def insertarSimpleEnlaPa(self, codigo, secuencia):
        new1 = Patron(codigo, secuencia)
        self.size1 += 1
        if self.inicio1 is None:
            self.inicio1 = new1
        else:
            aux1 = self.inicio1
            while aux1.siguiente1 is not None:
                aux1 = aux1.siguiente1
            aux1.siguiente1 = new1

    def getPatron(self, codigo):
        aux1 = self.inicio1
        while aux1 is not None:
            if aux1.codigo == codigo:
                return aux1
            aux1 = aux1.siguiente1
        return None

    def getPatronG(self, codigo):
        aux1 = self.inicio1
        while aux1 is not None:
            if aux1.codigo == codigo:
                return aux1.secuencia
            aux1 = aux1.siguiente1
        return None
        

    def imprimirSimpleEnlaPa(self):
        tmp = self.inicio1
        while(tmp!=None):
            print(tmp.getCodigo()+" --- "+tmp.getSecuencia())
            tmp = tmp.siguiente1

    

    def OrdenarPatron(self):
        if self.size1 > 1:
            while True:
                actua=self.inicio1
                o=None
                p=self.inicio1.getSiguiente1()
                sicambio=False
                while p!=None:
                    if actua.codigo[0]>p.codigo[0]:
                        sicambio=True
                        if o!=None:
                            temporal=p.getSiguiente1()
                            o.setSiguiente1(p)
                            p.setSiguiente1(actua)
                            actua.setSiguiente1(temporal)
                        else:
                            temporal1= p.getSiguiente1()
                            self.inicio1 = p
                            p.setSiguiente1(actua)
                            actua.setSiguiente1(temporal1)
                        o=p
                        p=actua.getSiguiente1()
                    else:
                        o=actua
                        actua=p
                        p=p.getSiguiente1()
                if sicambio==False:
                    break        

  