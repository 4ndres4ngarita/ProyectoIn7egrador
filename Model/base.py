class Nodo:
    id: str
    tipoNodo:str
    vertices: list

    def __init__(self, pId:str, pTipo:str=None):
        self.id = pId
        self.tipo = pTipo
        self.vertices = []

    def añadirVertice(self, pVertice):
        self.vertices.append(pVertice)

    def estaConectadoCon(self, pNodo):
        noEstaConectado = True
        vertice_i = 1
        while noEstaConectado and vertice_i <= len(self.vertices):
            verticeSiguiente = self.vertices[vertice_i - 1]
            if (verticeSiguiente.nodoConectado.id == pNodo.id):
                noEstaConectado = False
            else:
                vertice_i += 1

        estaConectado = not noEstaConectado

        return estaConectado

    def eliminarVertice(self, pPosicionVertice:int):
        del self.vertices[pPosicionVertice]

class Vertice:
        nodoConectado: Nodo
        distancia: int
        sentidoCardinal: int
        direccionVectorial:int # -1 Invertido, 0 Completo, 1 Simple

        def __init__(self, pNodoConectado, pDistancia: int, pSentidoCardinal: int, pDireccionVectorial:int):
            self.nodoConectado = pNodoConectado
            self.distancia = pDistancia
            self.sentidoCardinal = pSentidoCardinal
            self.direccionVectorial = pDireccionVectorial
            
