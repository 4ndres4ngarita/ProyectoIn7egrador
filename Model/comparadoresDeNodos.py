try:
    from base import *
except:
    from model.base import *

class ComparadorDeNodos:

    @staticmethod
    def sonNodosIdenticos( unNodo:Nodo, otroNodo:Nodo):
        tienenElMismoCodigo = ComparadorDeNodosPorCodigo.sonIguales(unNodo, otroNodo)
        tienenElMismoNombre = ComparadorDeNodosPorNombre.sonIguales(unNodo,otroNodo)
        sonElMismoTipo = ComparadorDeNodosPorTipo.sonIguales(unNodo, otroNodo)
        tienenLaMismaLista = ComparadorDeNodosPorListaDeConexiones.sonIguales( unNodo, otroNodo)
        sonIguales = tienenElMismoCodigo and tienenElMismoNombre and sonElMismoTipo and tienenLaMismaLista
        return sonIguales

#Comparadores de nodos por atributo
class ComparadorDeNodosPorCodigo:
    @staticmethod
    def sonIguales( unNodo:Nodo, otroNodo:Nodo):
        return (
            ComparadorDeCodigoDeNodos.sonIguales( 
                unNodo.getCodigo(), otroNodo.getCodigo()
            )
        )

class ComparadorDeNodosPorNombre:
    @staticmethod
    def sonIguales( unNodo:Nodo, otroNodo:Nodo):
        return (
            ComparadorDeNombreDeNodos.sonIguales(
                unNodo.getNombre(), otroNodo.getNombre()
            )
        )
    
class ComparadorDeNodosPorTipo:
    @staticmethod
    def sonIguales( unNodo:Nodo, otroNodo:Nodo):
        return(
            ComparadorDeTipoDeNodos.sonIguales(
                unNodo.getTipoDelNodo(), otroNodo.getTipoDelNodo()
            )
        )

class ComparadorDeNodosPorListaDeConexiones:
    @staticmethod
    def sonIguales( unNodo:Nodo, otroNodo:Nodo):
        return(
            ComparadorDeConexionesDeNodos.sonIguales(
                unNodo.getListaDeConexiones(),
                otroNodo.getListaDeConexiones()
            )
        )

#Comparadores de atributos
class ComparadorDeCodigoDeNodos:
    @staticmethod
    def sonIguales( unCodigo:type(Nodo().getCodigo()), otroCodigo:type(Nodo().getCodigo())):
        return unCodigo == otroCodigo

class ComparadorDeNombreDeNodos:
    @staticmethod
    def sonIguales( unNombre:type(Nodo().getNombre()), otroNombre:type(Nodo().getNombre())):
        return unNombre == otroNombre

class ComparadorDeTipoDeNodos:
    @staticmethod
    def sonIguales( unTipo:type(Nodo().getTipoDelNodo()), otroTipo:type(Nodo().getTipoDelNodo())):
        return unTipo == otroTipo

class ComparadorDeConexionesDeNodos:

    @staticmethod
    def sonIguales( unaListaDeConexiones:list, otraListaDeConexiones:list):
        return unaListaDeConexiones == otraListaDeConexiones

class ComparadorDeNumeroDeConexiones:

    @staticmethod
    def sonIguales( unNumero:int, otroNumero:int):
        return unNumero == otroNumero