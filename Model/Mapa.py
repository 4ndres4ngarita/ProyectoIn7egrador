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
        return self.esquinas[pId]

    def estaRegistradaLaEsquina(self, pEsquinaId:str):
        estaRegistrado = False
        for siguienteEsquina in self.esquinas:
            if pEsquinaId == siguienteEsquina:
                estaRegistrado = True
                break
        return estaRegistrado

    def conectarEsquinas(self, pNodo1:Esquina, pNodo2:Esquina, pDistancia:int, pConcurrencia:int, pEstaCerrado:bool, pSentidoCardinal:int, pDireccionVectorial:int):
        pNodo1.agregarCarretera(pNodo2, pDistancia, pConcurrencia, pEstaCerrado, pSentidoCardinal, pDireccionVectorial)
        pNodo2.agregarCarretera(pNodo1, pDistancia, pConcurrencia, pEstaCerrado, (pSentidoCardinal*-1), (pDireccionVectorial*-1))

    def conectarEsquinasPorId(self, pEsquina1:str, pEsquina2:str, pDistancia:int, pConcurrencia:int, pEstaCerrado:bool, pSentidoCardinal:int, pDireccionVectorial:int):
        esquina1 = self.pedirEsquinaPorId( pEsquina1)
        esquina2 = self.pedirEsquinaPorId( pEsquina2)
        carreteraDe1a2 = Carretera( esquina2, pDistancia, pConcurrencia, pEstaCerrado, pSentidoCardinal, pDireccionVectorial)
        carreteraDe2a1 = Carretera( esquina1, pDistancia, pConcurrencia, pEstaCerrado, (pSentidoCardinal*-1), (pDireccionVectorial*-1))
        esquina1.agregarCarretera(carreteraDe1a2)
        esquina2.agregarCarretera(carreteraDe2a1)