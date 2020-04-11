try:
    from base import * #para probar el codigo es este mismo archivo
except:
    from model.base import *#para probar el codigo en otro archivo

class Esquina(Nodo):
    carrera:str
    calle:str
    anexo:str

    def __init__(self, pCarrera:str, pCalle:str, pAnexo:str=None):
        if pAnexo is None:
            Nodo.__init__( self, ("cra"+pCarrera+"cll"+pCalle), "Esquina")
        else:
            Nodo.__init__( self, ("cra"+pCarrera+"cll"+pCalle+pAnexo), "Esquina")
        self.carrera = pCarrera
        self.calle = pCalle

    def agregarCarretera(self, pCarretera):
        self.vertices.append( pCarretera)

    def estaConectadoCon(self, pNodoId):
        noEstaConectado = True
        carretera_i = 1
        while noEstaConectado and carretera_i <= len(self.vertices):
            carreteraSiguiente = self.vertices[carretera_i-1]
            if carreteraSiguiente.nodoConectado.id == pNodoId:
                noEstaConectado = False
            else:
                carretera_i += 1
        
        estaConectado = not noEstaConectado
        
        return estaConectado

class Carretera(Vertice):

    concurrencia:int
    estaCerrado:bool
    
    def __init__(self, pNodoConectado, pDistancia:int, pConcurrencia:int, pEstaCerrado:bool, pSentidoCardinal:int, pDireccionVectorial:int):
        Vertice.__init__( self, pNodoConectado, pDistancia, pSentidoCardinal, pDireccionVectorial)
        self.concurrencia = pConcurrencia
        self.estaCerrado = pEstaCerrado
