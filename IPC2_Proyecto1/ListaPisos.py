from Piso import Piso
class ListaPisos():#matriz
    def __init__(self):
        self.inicio = None
        self.fin = None
        self.size = 0

    def insertarSimpleEnla(self, nombre, R, C, F, S):
        new = Piso(nombre,R, C, F, S)
        self.size += 1
        if self.inicio is None:
            self.inicio = new
        else:
            aux = self.inicio
            while aux.siguiente is not None:
                aux = aux.siguiente
            aux.siguiente = new

    def getPiso(self, nombre):
        aux = self.inicio
        while aux is not None:
            if aux.nombre == nombre:
                return aux
            aux = aux.siguiente
        return None

    def imprimirSimpleEnla(self):
        tmp = self.inicio
        while(tmp!=None):
            print(str(tmp.getNombre())+" --- "+tmp.getRo()+" --- "+tmp.getCo()+" --- "+tmp.getFi()+" --- "+tmp.getSi())
            tmp = tmp.siguiente

    def ordenar(self):
        if self.size>1:
            while True:
                act=self.inicio
                i=None
                j=self.inicio.getSiguiente()
                cambio=False
                while j!=None:
                    if act.nombre[0]>j.nombre[0]:
                        cambio=True
                        if i!=None:
                            temp=j.getSiguiente()
                            i.setSiguiente(j)
                            j.setSiguiente(act)
                            act.setSiguiente(temp)
                        else:
                            te1= j.getSiguiente()
                            self.inicio=j
                            j.setSiguiente(act)
                            act.setSiguiente(te1)
                        i=j
                        j=act.getSiguiente()

                    else:
                        i=act
                        act=j
                        j=j.getSiguiente()
                if cambio==False:
                    break        