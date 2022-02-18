class Celda():
    def __init__(self, Ro, Co, color):
        self.Row = Ro
        self.Colum = Co
        self.Color= color
        self.siguiente=None
        self.anterior=None