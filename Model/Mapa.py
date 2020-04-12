try:
    from tiposDeNodos import *
    from base import * #para probar el codigo es este mismo archivo
except:
    from model.tiposDeNodos import *
    from model.base import *#para probar el codigo en otro archivo

class Mapa(Nodo):
    esquinas:dict
    paradas:dict
    
    def __init__(self, pId:str = ""):
        Nodo.__init__( self, pId, "Mapa")
        self.esquinas = {}
        self.paradas = {}

#region metodosEsquinas
    def añadirEsquina(self, pEsquina):
        self.esquinas[pEsquina.codigo] = pEsquina

    def pedirEsquinaPorCodigo(self, pCodigo:str):
        return self.esquinas[pCodigo]
    
    def estaRegistradaLaEsquina(self, pEsquinaCodigo:str):
        estaRegistrado = False
        for siguienteEsquina in self.esquinas:
            if pEsquinaCodigo == siguienteEsquina:
                estaRegistrado = True
                break
        return estaRegistrado

    def conectarEsquinas(self, pEsquina1:Esquina, pEsquina2:Esquina, pDistancia:int, pConcurrencia:int, pEstaCerrado:bool, pSentidoCardinal:int, pDireccionVectorial:int):
        conexionDe1a2 = Conexion( pEsquina2, pDistancia, pConcurrencia, pEstaCerrado, pSentidoCardinal, pDireccionVectorial)
        conexionDe2a1 = Conexion( pEsquina1, pDistancia, pConcurrencia, pEstaCerrado, (pSentidoCardinal*-1), (pDireccionVectorial*-1))
        pEsquina1.añadirConexion(conexionDe1a2)
        pEsquina2.añadirConexion(conexionDe2a1)

    def conectarEsquinasPorCodigo(self, pEsquina1:str, pEsquina2:str, pDistancia:int, pConcurrencia:int, pEstaCerrado:bool, pSentidoCardinal:int, pDireccionVectorial:int):
        esquina1 = self.pedirEsquinaPorCodigo( pEsquina1)
        esquina2 = self.pedirEsquinaPorCodigo( pEsquina2)
        self.conectarEsquinas( esquina1, esquina2, pDistancia, pConcurrencia, pEstaCerrado, pSentidoCardinal, pDireccionVectorial)
#enregion
    
    def añadirParada(self, pParada:Parada):
        self.paradas[ pParada.codigo] = pParada

    def conectarParada(self, pCodigoParada:str, pCodigoEsquina1:str,pCodigoEsquina2:str, pNumeroDeConexion:int):
        esquina1 = self.pedirEsquinaPorCodigo(pCodigoEsquina1)
        esquina2 = self.pedirEsquinaPorCodigo(pCodigoEsquina2)
        parada = self.paradas[ pCodigoParada]
        distanciaEntreEsquinas = esquina1.pedirLaConexionCon( pCodigoEsquina2, pNumeroDeConexion).distancia / 2
        numeroDeConexionEsquina1 = esquina1.cambiarNodoConectadoPor(pCodigoEsquina2, parada, pNumeroDeConexion)
        esquina1.cambiarDistanciaDeConexionCon( pCodigoParada, numeroDeConexionEsquina1, distanciaEntreEsquinas)
        numeroDeConexionEsquina2 = esquina2.cambiarNodoConectadoPor(pCodigoEsquina1, parada, pNumeroDeConexion)
        esquina2.cambiarDistanciaDeConexionCon( pCodigoParada, numeroDeConexionEsquina2,distanciaEntreEsquinas)