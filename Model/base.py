class Nodo:
    id: str
    tipoNodo:str
    vertices: list

    def __init__(self, pId:str, pTipo:str=None):
        self.id = pId
        self.tipo = pTipo
        self.vertices = []

    def conectarNodo(self, pNodo, pDistancia: int, pSentido: int = 0):
        nuevoVertice = Vertice(pNodo, pDistancia, pSentido)
        self.vertices.append(nuevoVertice)
        if self.estaConectadoCon(pNodo) and not pNodo.estaConectadoCon(self):
            pNodo.conectarNodo(self, pDistancia, (pSentido * -1))

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

    def eliminarVertice(self, pPosicionVertice:int=None):
        if pPosicionVertice is None :
            pPosicionVertice = len(self.vertices)-1
        del self.vertices[pPosicionVertice]

class Vertice:
        nodoConectado: Nodo
        distancia: int
        sentido: int  # -1 Invertido, 0 Completo, 1 Simple

        def __init__(self, pNodoConectado: Nodo, pDistancia: int, pSentido: int):
            self.nodoConectado = pNodoConectado
            self.distancia = pDistancia
            self.sentido = pSentido