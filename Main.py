#from Modelo import Esquina
from MVC.Modelo import Esquina
from MVC.Fronter import *
def main():
    """esquina1 = Esquina( "33", "48")
    esquina2 = Esquina( "33", "36")
    estanConectadasLasEsquinas( esquina1, esquina2)

    esquina1.conectarEsquina( esquina2, 12, 10)
    imprimirNuevaConexion( esquina1, esquina2)

    estanConectadasLasEsquinas( esquina1, esquina2)

    esquina3 = Esquina("35","34")
    esquina1.conectarEsquina( esquina3, 23, 45, False, 1)
    esquina3.conectarEsquina(esquina2, 23, 45, False, 1)

    esquina4 = Esquina("25","23")
    esquina2.conectarEsquina( esquina4, 23, 45, False)
    esquina1.conectarEsquina( esquina1, 20, 12, False, 1)
    """

    nodo1 = Nodo(1)
    nodo2 = Nodo(2)
    estanConectadosLosNodos(nodo1,nodo2)
    nodo1.conectarNodo(nodo2,12)
    imprimirNuevoVertice(nodo1,nodo2)
    estanConectadosLosNodos(nodo1,nodo2)
    nodo3 = Nodo(3)
    nodo1.conectarNodo(nodo3,23,1)
    nodo3.conectarNodo(nodo2,23,1)
    nodo4 = Nodo(4)
    nodo2.conectarNodo(nodo4,23)
    nodo1.conectarNodo(nodo1,20,1)
    imprimirNuevoVertice(nodo1, nodo1)
    del nodo1.vertices[2]

    

if __name__ == '__main__': main()