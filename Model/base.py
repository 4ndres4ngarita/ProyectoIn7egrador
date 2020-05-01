try:
    from sentidosGeoespaciales import *
except:
    from model.sentidosGeoespaciales import *

class Nodo:
    __codigo:str
    __nombre: str
    __tipoDelNodo:str
    __listaDeConexiones: list

    def __init__(self, codigoInicial = "", nombreInicial = "",
     tipoDelNodoInicial = ""):
        self.__codigo = codigoInicial
        self.__nombre = nombreInicial
        self.__tipoDelNodo = tipoDelNodoInicial
        self.__listaDeConexiones = [] 

    """
        definimos getCodigo ( de un nodo) para:
         retornar el codigo de un nodo.
    """

    def getCodigo( self):
        return self.__codigo

    def getNombre( self):
        return self.__nombre

    def getTipoDelNodo( self):
        return self.__tipoDelNodo

    def getListaDeConexiones( self):
        return self.__listaDeConexiones
    """
        definimos setCodigo ( de un nodo, un nuevo codigo) para:
         asignale un nuevo codigo al codigo de un nodo.
    """

    def setCodigo(  self, nuevoCodigo:str):
        self.__codigo = nuevoCodigo

    def setNombre( self, nuevoNombre:str):
        self.__nombre = nuevoNombre

    def setTipoDelNodo( self, nuevoTipoDelNodo:str):
        self.__tipoDelNodo = nuevoTipoDelNodo
    
    def setListaDeConexiones( self, nuevaListaDeConexiones:list):
        self.__listaDeConexiones = nuevaListaDeConexiones

class Conexion:
    __nodoConectado: Nodo
    __distancia: int
    __concurrencia:int
    __sentidoCardinal: int
    __direccionVectorial:int
    __estaCerrado:bool
    __numeroDeConexion:int

    def __init__(self):
        self.__nodoConectado = Nodo()
        self.__distancia = 0
        self.__sentidoCardinal = direccionCardinal.INDEFINIDA
        self.__direccionVectorial = direccionVectorial.INDEFINIDO
        self.__concurrencia = 0
        self.__estaCerrado = False
        self.__numeroDeConexion = 0

    def getNodoConectado( self):
        return self.__nodoConectado

    def getDistancia( self):
        return self.__distancia
    
    def getSentidoCardinal( self):
        return self.__sentidoCardinal
    
    def getDireccionVectorial( self):
        return self.__sentidoCardinal
    
    def getConcurrencia( self):
        return self.__concurrencia
    
    def getEstaCerrado( self):
        return self.__estaCerrado
    
    def getNumeroDeConexion( self):
        return self.__numeroDeConexion
    
    def setNodoConectado( self, nuevoNodoConectado:Nodo):
        self.__nodoConectado = nuevoNodoConectado
    
    def setDistancia( self, nuevaDistancia:int):
        self.__distancia = nuevaDistancia
    
    def setSentidoCardinal( self, nuevoSentidoCardinal:int):
        self.__sentidoCardinal = nuevoSentidoCardinal
    
    def setDireccionVectorial( self, nuevaDireccionVectorial:int):
        self.__sentidoCardinal = nuevaDireccionVectorial
    
    def setConcurrencia( self, nuevaConcurrencia:int):
        self.__concurrencia = nuevaConcurrencia
    
    def setEstaCerrado( self, nuevoEstado:bool):
        self.__estaCerrado = nuevoEstado
    
    def setNumeroDeConexion( self, nuevoNumeroDeConexion:int):
        self.__numeroDeConexion = nuevoNumeroDeConexion

