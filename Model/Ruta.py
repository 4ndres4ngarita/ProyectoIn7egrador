try:
    from vias import *
    from base import * #para probar el codigo es este mismo archivo
except:
    from model.vias import *
    from model.base import *#para probar el codigo en otro archivo

class Ruta:

    nodoInicio:Nodo
    nodoFin:Nodo
    distanciasEntreNodos:dict

    def __init__(self, pNodoInicio, pNodoFin):
        self.nodoInicio = pNodoInicio
        self.nodoFin = pNodoFin
        self.distanciasEntreNodos = {}