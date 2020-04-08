#from Modelo import Esquina
from MVC.Modelo import *
from MVC.Fronter import *
def main():
    esquina1 = Esquina( "33", "48")
    esquina2 = Esquina( "33", "36")
    estanConectadasLasEsquinas( esquina1, esquina2)

    esquina1.agregarCarretera( esquina2, 12, 10)
    imprimirNuevaConexion( esquina1, esquina2)

    estanConectadasLasEsquinas( esquina1, esquina2)
    estanConectados(esquina1,esquina2)
    esquina3 = Esquina("35","34")
    esquina1.agregarCarretera( esquina3, 23, 45, False, 1)
    esquina3.agregarCarretera(esquina2, 23, 45, False, 1)

    esquina4 = Esquina("25","23")
    esquina2.agregarCarretera( esquina4, 23, 45, False)
    esquina1.agregarCarretera( esquina1, 20, 12, False, 1)
    

if __name__ == '__main__': main()