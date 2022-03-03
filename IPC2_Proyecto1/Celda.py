class Celda():
    def __init__(self, Ro, Co,color):
        self.Ro = Ro
        self.Co= Co
        self.color= color
        self.siguiente2=None
        self.anterior2=None

    def getRo(self):
        return self.Ro

    def getCo(self):
        return self.Co

    def getColor(self):
        return self.color

    def setRo(self, Ro):
        self.Ro = Ro

    def setCo(self, Co):
        self.Co = Co

    def setColor(self, color):
        self.color = color
