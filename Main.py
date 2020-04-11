#from Modelo import Esquina
from Model.Vias import *
from View.Base import *
from View.Menu import *
from Model.Mapa import *
from Model.Parada import *
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

def ejecutarDemostracionModelo():
    esquina1 = Esquina( "33", "48")
    esquina2 = Esquina( "33", "36")
    mapaDemo = Mapa("Ciudad1")
    mapaDemo.añadirEsquina(esquina1)
    mapaDemo.añadirEsquina(esquina2)
    mapaDemo.conectarEsquinas( esquina1, esquina2, 10, 20, False, 1)
    mapaDemo.conectarEsquinasPorId( esquina1.id, esquina2.id, 10, 20, False, -1)
    punto1 = Parada("p1")
    
    

    

def main():
    ejecutarDemostracionModelo()
    

if __name__ == '__main__': main()