try:
    from Vias import *
    from Base import * #para probar el codigo es este mismo archivo
except:
    from Model.Vias import *
    from Model.Base import *#para probar el codigo en otro archivo

class Mapa(Nodo):
    esquinas:dict
    rutas:dict
    
    def __init__(self, pId:str = "", pNodos:dict={}):
        Nodo.__init__( self, pId, "Mapa")
        self.nodos = pNodos
    
    def añadirNodo(self, pNodo):
        if not self.estaRegistradoElNodo():
            self.nodos[pNodo.id] = pNodo

    def pedirNodo(self, pId:str):
        if self.estaRegistradoElNodo(pId):
            return self.Nodo[pId]
        else:
            return None

    def estaRegistradoElNodo(self, pNodoId=str):
        estaRegistrado = False
        for siguienteNodo in self.nodos:
            if pNodoId == siguienteNodo:
                estaRegistrado = True
                break
        return estaRegistrado
    
    def conectarNodos(self, pIdNodo1, pIdNodo2, pVertice):
        pass

esquina1 = Esquina( "33", "48")
esquina2 = Esquina( "33", "36")
mapaDemo = Mapa()
mapaDemo.añadirNodo(esquina1)
mapaDemo.añadirNodo(esquina1)
#carretera1 = Carretera( "cra33cll36", 12, 10)
