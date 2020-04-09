try:
    from base import * #para probar el codigo es este mismo archivo
except:
    from model.base import *#para probar el codigo en otro archivo

class Esquina(Nodo):
    carrera:str
    calle:str

    def __init__(self, pCarrera:str, pCalle:str):
        Nodo.__init__( self, ("cra"+pCarrera+"cll"+pCalle), "Esquina")
        self.carrera = pCarrera
        self.calle = pCalle

    def agregarCarretera(self, pNodo, pDistancia:int, pConcurrencia:int, pEstaCerrado:bool=True, pSentido:int = 0):
        nuevaCarretera = Carretera( pNodo, pDistancia, pConcurrencia, pEstaCerrado, pSentido)
        self.vertices.append( nuevaCarretera)
        if self.estaConectadoCon(pNodo) and not pNodo.estaConectadoCon(self):
            pNodo.agregarCarretera(self, pDistancia, pConcurrencia, pEstaCerrado, (pSentido*-1))
               
    
    def estaConectadoCon(self, pNodo):
        noEstaConectado = True
        carretera_i = 1
        while noEstaConectado and carretera_i <= len(self.vertices):
            carreteraSiguiente = self.vertices[carretera_i-1]
            if carreteraSiguiente.nodoConectado.id == pNodo.id:
                noEstaConectado = False
            else:
                carretera_i += 1
        
        estaConectado = not noEstaConectado
        
        return estaConectado

class Carretera(Vertice):

    concurrencia:int
    estaCerrado:bool
    
    def __init__(self, pNodoConectado:Nodo, pDistancia:int, pConcurrencia:int, pEstaCerrado:bool, pSentido:int):
        Vertice.__init__( self, pNodoConectado, pDistancia, pSentido)
        self.concurrencia = pConcurrencia
        self.estaCerrado = pEstaCerrado
