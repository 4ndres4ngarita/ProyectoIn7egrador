try:
    from base import *
    from comparadoresDeNodos import *  
except:
    from model.base import *
    from model.comparadoresDeNodos import *

class IbuscadorDeConexiones:

    def __init__(self, listaDeConexiones:list):
        self.__listaDeConexiones = listaDeConexiones
        self.__conexionesEncontradas = []

    def getConexiones( self, condicion):
        pass
    
    def __añadirConexionEncontrada(self, conexionEncontrada:Conexion):
        self.__conexionesEncontradas.append( conexionEncontrada)
#buscadores con la lista directa de un nodo.
class BuscadorDeConexionesPorNodo(IbuscadorDeConexiones):
    def __init__(self, listaDeConexiones):
        super().__init__(listaDeConexiones)
    
    def getConexiones( self, nodoBuscado:Nodo):
        for conexionIesima in self._IbuscadorDeConexiones__listaDeConexiones:
            nodoDeUnaConexion = conexionIesima.getNodoConectado()
            unaConexionTieneElNodoBuscado = (
                ComparadorDeNodos.sonNodosIdenticos( nodoDeUnaConexion, nodoBuscado)
            )
            if unaConexionTieneElNodoBuscado:
                self._IbuscadorDeConexiones__añadirConexionEncontrada( conexionIesima)
            del unaConexionTieneElNodoBuscado
        return self._IbuscadorDeConexiones__conexionesEncontradas

class BuscadorDeConexionesPorCodigoDelNodo(IbuscadorDeConexiones):
    def __init__(self, listaDeConexiones):
        super().__init__(listaDeConexiones)

    def getConexiones(self, codigoDelNodoBuscado:str):
        for conexionIesima in self._IbuscadorDeConexiones__listaDeConexiones:
            nodoDeUnaConexion = conexionIesima.getNodoConectado()
            unNodoTieneElCodigoBuscado =(
                ComparadorDeCodigoDeNodos.sonIguales
                ( nodoDeUnaConexion.getCodigo(), codigoDelNodoBuscado)
            )
            if unNodoTieneElCodigoBuscado: 
                self._IbuscadorDeConexiones__añadirConexionEncontrada( conexionIesima)
            del unNodoTieneElCodigoBuscado
        return self._IbuscadorDeConexiones__conexionesEncontradas

#buscadores con listas procesadas.
class BuscadorDeConexionesPorNumeroDeConexion(IbuscadorDeConexiones):
    
    def __init__(self, listaDeConexiones):
        super().__init__(listaDeConexiones)
    
    def getConexiones(self, numeroDeConexionBuscado:int):
        for conexionIesima in self._IbuscadorDeConexiones__listaDeConexiones:
            numeroDeUnaConexion = conexionIesima.getNumeroDeConexion()
            unaConexionTieneElNumeroBuscado = (
                ComparadorDeNumeroDeConexiones.sonIguales(
                    numeroDeUnaConexion, numeroDeConexionBuscado
                )
            )
            if unaConexionTieneElNumeroBuscado:
                self._IbuscadorDeConexiones__añadirConexionEncontrada( conexionIesima)
        return self._IbuscadorDeConexiones__conexionesEncontradas

