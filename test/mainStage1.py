import json,sys
sys.path.append("D:\Proyectos\ProyectoIn7egrador")
from model.base import *
from model.comparadoresDeNodos import *
from model.buscadoresDeConexiones import *
def __main__():
    nodos = cargarNodosEnMemoria()
    realizarPruebas_ComparadoresDeNodos_(nodos)
    realizarPruebas_BuscadoresDeConexiones_(nodos)
    

#funciones para abstraer datos Json a Objetos
def cargarNodosEnMemoria():
    #with open("D:/Proyectos/ProyectoIn7egrador/test/graphStage1.json") as json_file:
    documento = importarArchivo( "D:/Proyectos/ProyectoIn7egrador/test/graphStage1.json")
    datosJson = importarJsonDesdeArchivo( documento)
    nodos = importarNodosDesdeJson(datosJson)
    importarConexionesDesdeJson( datosJson, nodos)
    del documento
    del datosJson
    print("Importacion Json cargado :)")
    return nodos
def importarArchivo( rutaDelArchivo:str):
    documento = open( rutaDelArchivo)
    return documento
def importarJsonDesdeArchivo( archivo):
    jsonCrudo = json.load( archivo)
    return jsonCrudo
def importarNodosDesdeJson( baseDeDatosJson):
    listaDeNodos= []
    for jsonIesimo in baseDeDatosJson["nodos"]:
        nuevoNodo = Nodo(
            jsonIesimo["codigo"],
            jsonIesimo["nombre"],
            jsonIesimo["tipo"]
        )
        listaDeNodos.append( nuevoNodo)
        del nuevoNodo
    return listaDeNodos

def importarPaqueteDeConexionesJson( baseDeDatosJson, codigoDelNodo:str):
    paqueteDeConexionesJson = []
    BaseDeDatosDeConexiones = baseDeDatosJson["conexiones"]
    for paqueteIesimo in BaseDeDatosDeConexiones:
        if paqueteIesimo["nodo"] == codigoDelNodo:
            paqueteDeConexionesJson = paqueteIesimo["lista"]
            break
    del BaseDeDatosDeConexiones
    return paqueteDeConexionesJson
def abstraerConexionesJson( paqueteDeConexiones, listaDeNodos:list):
    listaDeConexiones = []
    for conexionJsonIesimo in paqueteDeConexiones:
        nuevaConexion = Conexion()
        nuevaConexion.setDistancia( conexionJsonIesimo["distancia"])
        nuevaConexion.setConcurrencia( conexionJsonIesimo["concurrencia"])
        nuevaConexion.setSentidoCardinal( conexionJsonIesimo["sentidoCardinal"])
        nuevaConexion.setDireccionVectorial( conexionJsonIesimo["direccionVectorial"])
        nuevaConexion.setEstaCerrado( conexionJsonIesimo["estaCerrado"])
        nuevaConexion.setNumeroDeConexion(conexionJsonIesimo["numeroDeConexion"])
        for nodoIesimo in listaDeNodos:
            if nodoIesimo.getCodigo() == conexionJsonIesimo["nodoConectado"]:
                nuevaConexion.setNodoConectado( nodoIesimo)
                break
        listaDeConexiones.append( nuevaConexion)
    return listaDeConexiones
def importarConexionesDeUnNodo( baseDeDatosJson, codigoDelNodo:str, listaDeNodos:list):
    paqueteDeConexionesEnCrudo = importarPaqueteDeConexionesJson( baseDeDatosJson, codigoDelNodo)
    listaDeConexiones = abstraerConexionesJson( paqueteDeConexionesEnCrudo, listaDeNodos)
    return listaDeConexiones
def importarConexionesDesdeJson( baseDeDatosJson, listaDeNodos:list):
    for nodoIesimo in listaDeNodos:
        listaDeConexiones = importarConexionesDeUnNodo(
            baseDeDatosJson,
            nodoIesimo.getCodigo(), 
            listaDeNodos)
        nodoIesimo.setListaDeConexiones( listaDeConexiones)

def presentarNodo( nodo:Nodo):
    print(
        "{ codigo : "+ nodo.getCodigo() +
        ", nombre : "+ nodo.getNombre() +
        ", tipo : "+ nodo.getTipoDelNodo()+
        ", numero de conexiones : "+ str(len(nodo.getListaDeConexiones()))+
        " }"
    )
def presentarNodos( listaDeNodos:list):
    for nodoIesimo in listaDeNodos:
        presentarNodo( nodoIesimo)


#funciones de pruebas
def realizarPruebas_ComparadoresDeNodos_( nodos):
    n1 = nodos[0]
    n2 = nodos[1]
    n3 = nodos[2]
    n4 = nodos[3]
    n1copia = nodos[0]
    if(
        not ComparadorDeNodosPorCodigo.sonIguales( n1,n2) and
        not ComparadorDeNodosPorNombre.sonIguales( n1,n3) and
        ComparadorDeNodosPorTipo.sonIguales(n1,n4) and
        not ComparadorDeNodosPorListaDeConexiones.sonIguales(n2,n3) and
        not ComparadorDeNodos.sonNodosIdenticos( n1, n2) and
        ComparadorDeNodos.sonNodosIdenticos(n1, n1copia)
    ):
        print("test comparadoresDeNodos : okey!")
    else:
        print("test comparadoresDeNodos: not okey :/")
def realizarPruebas_BuscadoresDeConexiones_( nodos):
    n1 = nodos[0]
    n2 = nodos[1]
    n3 = nodos[2]
    n4 = nodos[3]
    buscadorPorNodosEn_n1 = BuscadorDeConexionesPorNodo( n1.getListaDeConexiones())
    buscadorPorCodigoDeNodoEn_n1 = BuscadorDeConexionesPorCodigoDelNodo( n1.getListaDeConexiones())
    subTest1 = (
        buscadorPorNodosEn_n1.getConexiones( n2) ==
        buscadorPorCodigoDeNodoEn_n1.getConexiones( n2.getCodigo())
    )
    buscadorPorCodigoDeNodoEn_n3 = BuscadorDeConexionesPorCodigoDelNodo( n3.getListaDeConexiones())
    conexionesDeN3conN2 = buscadorPorCodigoDeNodoEn_n3.getConexiones( "2")
    buscadorPorNumeroDeConexionEn_n3 = BuscadorDeConexionesPorNumeroDeConexion( conexionesDeN3conN2)
    subTest2 = len(buscadorPorNumeroDeConexionEn_n3.getConexiones( 1)) == 1
    if( subTest1 and subTest2):
        print("test buscadoresDeConexiones : okey!")
    else:
        print("test buscadoresDeConexiones : not okey :/")
__main__()