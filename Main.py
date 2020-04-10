#from Modelo import Esquina
from Model.Vias import *
from View.Base import *
from View.Menu import *
import time

def controlMenuPrincipal( pEleccion):
    if pEleccion is '1':
        eleccion = interactuarConMenuCrearMapa()
        controlMenuCrearMapa( eleccion)

def controlMenuCrearMapa( pEleccion):
    if pEleccion is '1':
        ejecutarFuncionAñadirCarreteras()
    elif pEleccion is '2':
        ejecutarFuncionConectarCarreteras()
    elif pEleccion is '3':
        ejecutarFuncionListarEsquinas()

def runApplication():
    while True:
        eleccionDemo = interactuarConMenuPrincipal()
        if eleccionDemo is "q":
            print("Hasta la Proxima <negros del ataud llendose>")
            break
        else:
            controlMenuPrincipal(eleccionDemo)
            limpiarConsola()

_mapaDeCarreteras = []

def ejecutarFuncionAñadirCarreteras():
    limpiarConsola()
    print("<Funcion 'Añadir Carreteras'>")
    time.sleep(3)
    limpiarConsola()
    nuevaCarreraEsquina = input("ingrese Carrera de la nueva esquina :")
    nuevaCalleEsquina = input("ingrese Calle de la nueva esquina :")
    _mapaDeCarreteras.append( Esquina(nuevaCarreraEsquina, nuevaCalleEsquina))
    limpiarConsola()
    quiereRepetir = input("esquina añadida.\nDesea añadir otra? (s/n):")
    if quiereRepetir is 's' or quiereRepetir is 'S' or quiereRepetir is '':
        ejecutarFuncionAñadirCarreteras()

def ejecutarFuncionConectarCarreteras():
    print("<Funcion 'Conectar Carreteras'>")
    time.sleep(3)

def ejecutarFuncionListarEsquinas():
    print("<Funcion 'Listar Esquinas'>")
    time.sleep(3)

def ejecutarDemostracionModelo():
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

def main():
    ejecutarDemostracionModelo()

    runApplication()
    

if __name__ == '__main__': main()