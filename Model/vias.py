try:
    from Base import * #para probar el codigo es este mismo archivo
except:
    from Model.Base import *#para probar el codigo en otro archivo

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
    
    def __init__(self, pNodoConectado, pDistancia:int, pConcurrencia:int, pEstaCerrado:bool=True, pSentido:int=0):
        Vertice.__init__( self, pNodoConectado, pDistancia, pSentido)
        self.concurrencia = pConcurrencia
        self.estaCerrado = pEstaCerrado
