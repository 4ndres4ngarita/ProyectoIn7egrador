try:
    from Vias import *
    from Base import * #para probar el codigo es este mismo archivo
except:
    from Model.Vias import *
    from Model.Base import *#para probar el codigo en otro archivo

class Ruta:

    nodoInicio:Nodo
    nodoFin:Nodo
    distanciasEntreNodos:dict

    def __init__(self, pNodoInicio, pNodoFin):
        self.nodoInicio = pNodoInicio
        self.nodoFin = pNodoFin
        self.distanciasEntreNodos = {}