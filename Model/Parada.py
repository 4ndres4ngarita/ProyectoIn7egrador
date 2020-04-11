try:
    from Vias import *
    from Base import * #para probar el codigo es este mismo archivo
except:
    from Model.Vias import *
    from Model.Base import *#para probar el codigo en otro archivo

class Parada(Nodo):

    def __init__(self, pId:str=""):
        Nodo.__init__(self, pId, "Parada")

    
