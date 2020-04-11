try:
    from vias import *
    from base import * #para probar el codigo es este mismo archivo
except:
    from model.vias import *
    from model.base import *#para probar el codigo en otro archivo

class Parada(Nodo):

    def __init__(self, pId:str=""):
        Nodo.__init__(self, pId, "Parada")

    
