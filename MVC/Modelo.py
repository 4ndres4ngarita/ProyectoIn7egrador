class Esquina:
    carrera:str
    calle:str
    esquinasCarretera:list

    def __init__(self, pCarrera:str, pCalle:str):
        self.carrera = pCarrera
        self.calle = pCalle
        self.carreteras = []

    def conectarEsquina(self, pEsquina, pDistancia:int, pConcurrencia:int, pEstaCerrado:bool=True, pSentido:int = 0):
        nuevaCarretera = Carretera( pEsquina, pDistancia, pConcurrencia, pEstaCerrado, pSentido)
        self.carreteras.append( nuevaCarretera)
        if self.estaConectadoCon(pEsquina) and not pEsquina.estaConectadoCon(self):
            pEsquina.conectarEsquina(self, pDistancia, pConcurrencia, pEstaCerrado, (pSentido*-1))
               
    
    def estaConectadoCon(self, pEsquina):
        noEstaConectado = True
        carretera_i = 1
        while noEstaConectado and carretera_i <= len(self.carreteras):
            carreteraSiguiente = self.carreteras[carretera_i-1]
            if (carreteraSiguiente.esquinaConectada.calle == pEsquina.calle and 
            carreteraSiguiente.esquinaConectada.carrera == pEsquina.carrera ):
                noEstaConectado = False
            else:
                carretera_i += 1
        
        estaConectado = not noEstaConectado
        
        return estaConectado

class Carretera:
    esquinaConectada:Esquina
    distancia:int
    concurrencia:int
    estaCerrado:bool
    sentido:int # -1 Invertido, 0 Completo, 1 Simple
    
    def __init__(self, pEsquinaConectada:Esquina, pDistancia:int, pConcurrencia:int, pEstaCerrado:bool, pSentido:int):
        self.esquinaConectada = pEsquinaConectada
        self.distancia = pDistancia
        self.concurrencia = pConcurrencia
        self.estaCerrado = pEstaCerrado
        self.sentido = pSentido


class Nodo:
    id: int
    vertices: list

    def __init__(self, pId:int):
        self.id = pId
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

    def eliminarVertice(self, pPosicionVertice:int=len(vertices)-1):
        del self.vertices[pPosicionVertice]

class Vertice:
        nodoConectado: Nodo
        distancia: int
        sentido: int  # -1 Invertido, 0 Completo, 1 Simple

        def __init__(self, pNodoConectado: Nodo, pDistancia: int, pSentido: int):
            self.nodoConectado = pNodoConectado
            self.distancia = pDistancia
            self.sentido = pSentido