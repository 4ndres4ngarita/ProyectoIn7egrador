#from modelo import Esquina
from model.vias import *
from view.base import *
from view.menu import *
from model.Mapa import *
from model.Parada import *
import time

def controlmenuPrincipal( pEleccion):
    if pEleccion is '1':
        eleccion = interactuarConmenuCrearMapa()
        controlmenuCrearMapa( eleccion)

def controlmenuCrearMapa( pEleccion):
    if pEleccion is '1':
        ejecutarFuncionAñadirCarreteras()
    elif pEleccion is '2':
        ejecutarFuncionConectarCarreteras()
    elif pEleccion is '3':
        ejecutarFuncionListarEsquinas()

def runApplication():
    while True:
        eleccionDemo = interactuarConmenuPrincipal()
        if eleccionDemo is "q":
            print("Hasta la Proxima <negros del ataud llendose>")
            break
        else:
            controlmenuPrincipal(eleccionDemo)
            limpiarConsola()

_mapaDeCarreteras = []

def ejecutarFuncionAñadirCarreteras():
    limpiarConsola()
    print("[Añadir Carreteras]")
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

def ejecutarDemostracionmodelo():
    esquina1 = Esquina( "33", "48")
    esquina2 = Esquina( "33", "36")
    mapaDemo = Mapa("Ciudad1")
    mapaDemo.añadirEsquina(esquina1)
    mapaDemo.añadirEsquina(esquina2)
    mapaDemo.conectarEsquinas( esquina1, esquina2, 10, 20, False, 1)
    mapaDemo.conectarEsquinasPorId( esquina1.id, esquina2.id, 10, 20, False, -1)
    punto1 = Parada("p1")
    
    

    

def main():
    ejecutarDemostracionmodelo()
    

if __name__ == '__main__': main()