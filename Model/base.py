class Nodo:
    codigo:str
    nombre: str
    tipoNodo:str
    conexiones: list

    def __init__(self, pCodigo:str, pNombre:str, pTipo:str=None):
        self.codigo = pCodigo
        self.nombre = pNombre
        self.tipo = pTipo
        self.conexiones = []

    def añadirConexion(self, pConexion):
        numeroNuevaConexion = self.pedirNumeroDeConexionesCon(pConexion.nodoConectado.codigo) +1
        pConexion.numero = numeroNuevaConexion
        self.conexiones.append(pConexion)

    def estaConectadoCon(self, pCodigoNodo):
        estaConectado = False
        for unaConexion in self.conexiones:
            if unaConexion.nodoConectado.codigo == pCodigoNodo:
                estaConectado = True
                break
        return estaConectado

    def pedirNumeroDeConexionesCon(self, pCodigoNodo:str):
        numeroDeConexiones = 0
        for unaConexion in self.conexiones:
            if unaConexion.nodoConectado.codigo == pCodigoNodo:
                numeroDeConexiones += 1
        return numeroDeConexiones

    def pedirLaConexionCon(self, pCodigoNodo:str, pNumeroDeConexion:int):
        for unaConexion in self.conexiones:
            if (unaConexion.nodoConectado.codigo == pCodigoNodo and
                unaConexion.numero == pNumeroDeConexion):
                conexion = unaConexion
        return conexion
    
    def reenumerarConexionesCon(self, pCodigoNodo:str):
        nuevoNumeroDeConexion = 1
        for unaConexion in self.conexiones:
            if unaConexion.nodoConectado.codigo == pCodigoNodo:
                unaConexion.numero = nuevoNumeroDeConexion
                nuevoNumeroDeConexion += 1

    def cambiarNodoConectadoPor(self, pCodigoNodo:str, pNodoNuevo, pNumeroDeConexion:int):
        conexion = self.pedirLaConexionCon( pCodigoNodo, pNumeroDeConexion)
        conexion.nodoConectado = pNodoNuevo
        self.reenumerarConexionesCon( pCodigoNodo)
        self.reenumerarConexionesCon( pNodoNuevo.codigo)
        return conexion.numero

#region editar atributos de una conexion
    
    def cambiarDistanciaDeConexionCon( self, pNodoConectado:str, pNumeroDeConexion:int, pDistanciaNueva):
        conexion = self.pedirLaConexionCon( pNodoConectado, pNumeroDeConexion)
        conexion.distancia = pDistanciaNueva

    def cambiarConcurrenciaDeConexionCon( self, pNodoConectado, pNumeroDeConexion, pConcurrenciaNueva):
        conexion = self.pedirLaConexionCon( pNodoConectado, pNumeroDeConexion)
        conexion.concurrencia = pConcurrenciaNueva

    def cambiarDisponibilidadCardinalDeConexionCon( self, pNodoConectado, pNumeroDeConexion):
        conexion = self.pedirLaConexionCon( pNodoConectado, pNumeroDeConexion)
        conexion.estaCerrado = not conexion.estaCerrado

    def cambiarSentidoCardinalDeConexionCon( self, pNodoConectado, pNumeroDeConexion, pSentidoCardinalNuevo):
        conexion = self.pedirLaConexionCon( pNodoConectado, pNumeroDeConexion)
        conexion.sentidoCardinal = pSentidoCardinalNuevo

    def cambiarDireccionVectorialDeConexionCon( self, pNodoConectado, pNumeroDeConexion, pDireccionVectorialNuevo):
        conexion = self.pedirLaConexionCon( pNodoConectado, pNumeroDeConexion)
        conexion.direccionVectorial = pDireccionVectorialNuevo
#endregion

class Conexion:
        nodoConectado: Nodo
        distancia: int
        concurrencia:int
        estaCerrado:bool
        sentidoCardinal: int
        direccionVectorial:int # -1 Invertido, 0 Completo, 1 Simple
        numero:int

        def __init__(self, pNodoConectado, pDistancia: int, pConcurrencia:int, pEstaCerrado:bool, pSentidoCardinal: int, pDireccionVectorial:int,  pNumero=0):
            self.nodoConectado = pNodoConectado
            self.distancia = pDistancia
            self.sentidoCardinal = pSentidoCardinal
            self.direccionVectorial = pDireccionVectorial
            self.concurrencia = pConcurrencia
            self.estaCerrado = pEstaCerrado
            self.numero = pNumero