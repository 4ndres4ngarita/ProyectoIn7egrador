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
    __estaCerrado:bool
    __sentidoCardinal: int
    __direccionVectorial:int
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

class ApiladorDeConexionesDeNodos:

    def __init__(self, nodoBase:Nodo = None):
        self.__nodoBase = nodoBase

    def apilarConexionAlNodoBase(self, conexionNueva:Conexion):
        ApiladorDeConexionesDeNodos.añadirConexion( self.__nodoBase, conexionNueva)

    @staticmethod
    def apilarConexion( nodoConConexiones:Nodo, conexionNueva:Conexion):
        ApiladorDeConexionesDeNodos.__apilarConexion( nodoConConexiones, conexionNueva)      

    @staticmethod
    def __apilarConexion(nodoConConexiones:Nodo, conexionNueva:Conexion):
        nodoConConexiones.getListaDeConexiones().append( conexionNueva)

class ContadorDeConexionesDeNodos:

    @staticmethod
    def contarTodasLasConexiones( nodoConConexiones:Nodo):
        return nodoConConexiones.getListaDeConexiones().count()

    @staticmethod
    def contarConexionesCon( nodoConConexiones:Nodo, nodoBuscado:Nodo):
        numeroDeConexiones = 0
        
        for cadaConexion in nodoConConexiones.getlistaDeConexiones():
            nodoDeCadaConexion = cadaConexion.getNodoConectado()
            elNodoDeUnaConexion = ComparadorDeNodos( nodoDeCadaConexion)
            if elNodoDeUnaConexion.esIgualAl( nodoBuscado):
                numeroDeConexiones += 1

        return numeroDeConexiones

class ComparadorDeNodos:

    def __init__(self, nodoBase:Nodo = None):
        self.__nodoBase = nodoBase

    def esIgualAl(self, nodoComparado:Nodo):
        return ComparadorDeNodos.sonIgualesLosNodos( self.__nodoBase, nodoComparado)
    
    @staticmethod
    def sonIgualesLosNodos( unNodo:Nodo, otroNodo:Nodo):
        return ComparadorDeNodos.__sonIguales( unNodo, otroNodo)
    
    @staticmethod
    def __sonIguales( unNodo:Nodo, otroNodo:Nodo):
        return (( unNodo.getCodigo() == otroNodo.getCodigo()) and
            (unNodo.getNombre() == otroNodo.getNombre()) and
            (unNodo.getTipoDelNodo() == otroNodo.getTipoDelNodo()) and
            (unNodo.getListaDeConexiones() == otroNodo.getListaDeConexiones()))

class BuscadorDeConexiones:

    __listaDeConexionesEncontradas = []

    def __init__(self, nodoBase:Nodo):
        self.__nodoBase = nodoBase

    def buscarConexionesCon(self, nodoBuscado:Nodo):
        BuscadorDeConexiones.buscarConexionesEntre( self.__nodoBase, nodoBuscado)

    @staticmethod
    def buscarConexionesEntre( nodoConConexiones:Nodo, nodoBuscado:Nodo):
        for unaConexion in nodoConConexiones.getListaDeConexiones():
            unNodoDeUnaConexion = unaConexion.getNodoConectado()
            comparandoUnNodo = ComparadorDeNodos( unNodoDeUnaConexion)
            if comparandoUnNodo.esIgual( nodoBuscado):
                BuscadorDeConexiones.__añadirConexionEncontrada( unaConexion)

    @staticmethod
    def getListaDeConexionesEncontradas( self):
        return BuscadorDeConexiones.__listaDeConexionesEncontradas
    
    def __añadirConexionEncontrada(self, conexionEncontrada:Conexion):
        BuscadorDeConexiones.__listaDeConexionesEncontradas.append( conexionEncontrada)

#Region pruebas

