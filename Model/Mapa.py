try:
    from Vias import *
    from Base import * #para probar el codigo es este mismo archivo
except:
    from Model.Vias import *
    from Model.Base import *#para probar el codigo en otro archivo

class Mapa(Nodo):
    esquinas:dict
    paradas:dict
    
    def __init__(self, pId:str = ""):
        Nodo.__init__( self, pId, "Mapa")
        self.esquinas = {}
        self.paradas = {}

    def añadirEsquina(self, pEsquina):
        if not self.estaRegistradaLaEsquina( pEsquina.id):
            self.esquinas[pEsquina.id] = pEsquina
    
    def añadirParada(self, pParada):
        self.paradas[ pParada.id] = pParada

    def pedirEsquinaPorId(self, pId:str):
        if self.estaRegistradaLaEsquina(pId):
            return self.esquinas[pId]
        else:
            return None

    def estaRegistradaLaEsquina(self, pEsquinaId:str):
        estaRegistrado = False
        i=1
        for siguienteEsquina in self.esquinas:
            i+=1
            if pEsquinaId == siguienteEsquina:
                estaRegistrado = True
                break
        return estaRegistrado

    def conectarEsquinas(self, pNodo1:Esquina, pNodo2:Esquina, pDistancia:int, pConcurrencia:int, pEstaCerrado:bool = True, pSentido:int = 0):
        pNodo1.agregarCarretera(pNodo2, pDistancia, pConcurrencia, pEstaCerrado, pSentido)
        pNodo2.agregarCarretera(pNodo1, pDistancia, pConcurrencia, pEstaCerrado, pSentido)

    def conectarEsquinasPorId(self, pEsquina1:str, pEsquina2:str, pDistancia:int, pConcurrencia:int, pEstaCerrado:bool = True, pSentido:int = 0):
        self.pedirEsquinaPorId( pEsquina1).agregarCarretera( self.pedirEsquinaPorId( pEsquina2), pDistancia, pConcurrencia, pSentido)
        self.pedirEsquinaPorId( pEsquina2).agregarCarretera( self.pedirEsquinaPorId( pEsquina1), pDistancia, pConcurrencia, (pSentido*-1))