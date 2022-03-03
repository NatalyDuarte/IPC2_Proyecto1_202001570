from ListaCelda import ListaCelda
class Patron():
    def __init__(self, codigo, secuencia):
        self.codigo = codigo
        self.secuencia = secuencia
        self.lista_celda = ListaCelda()
        self.siguiente1 = None

    def getCodigo(self):
        return self.codigo
    
    def getCelda(self):
        return self.lista_celda

    def getSecuencia(self):
        return self.secuencia

    def getSiguiente1(self):
        return self.siguiente1

    def setCodigo(self, codigo):
        self.codigo = codigo

    def setSecuencia(self, secuencia):
        self.secuencia = secuencia

    def setSiguiente1(self,nodis1):
        self.siguiente1=nodis1