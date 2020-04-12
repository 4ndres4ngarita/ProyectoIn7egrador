try:
    from base import * #para probar el codigo es este mismo archivo
except:
    from model.base import *#para probar el codigo en otro archivo

class Esquina(Nodo):
    def __init__(self, pCodigo, pNombre):
        Nodo.__init__(self,pCodigo, pNombre, "Esquina")

class Parada(Nodo):
    distanciaOriginalEntreNodos:int
    def __init__(self, pCodigo, pNombre):
        Nodo.__init__(self, pCodigo, pNombre, "Parada")
        self.distanciaOriginalEntreNodos = 0

    
