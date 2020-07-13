#from modelo import Esquina
from model.tiposDeNodos import *
from view.base import *
from view.menu import *
import time

def controlmenuPrincipal( pEleccion):
    if pEleccion == '1':
        eleccion = interactuarConmenuCrearMapa()
        controlmenuCrearMapa( eleccion)

def controlmenuCrearMapa( pEleccion):
    if pEleccion == '1':
        ejecutarFuncionAñadirCarreteras()
    elif pEleccion == '2':
        ejecutarFuncionConectarCarreteras()
    elif pEleccion == '3':
        ejecutarFuncionListarEsquinas()

def runApplication():
    while True:
        eleccionDemo = interactuarConmenuPrincipal()
        if eleccionDemo == "q":
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
    if quiereRepetir == 's' or quiereRepetir == 'S' or quiereRepetir == '':
        ejecutarFuncionAñadirCarreteras()

def ejecutarFuncionConectarCarreteras():
    print("<Funcion 'Conectar Carreteras'>")
    time.sleep(3)

def ejecutarFuncionListarEsquinas():
    print("<Funcion 'Listar Esquinas'>")
    time.sleep(3)

def ejecutarDemostracionmodelo():
    e1 = Esquina("1","n1")
    e2 = Esquina("2","n2")
    m1 = Mapa( "ciudad1")
    m1.añadirEsquina(e1)
    m1.añadirEsquina(e2)
    m1.conectarEsquinasPorCodigo( "1","2",10,12,False,1,1)
    m1.conectarEsquinasPorCodigo( "1","2",20,13,False,2,0)
    m1.conectarEsquinasPorCodigo( "1","2",30,14,False,3,-1)
    p1 = Parada("1","LaTiendaDeMarta")
    m1.añadirParada(p1)
    m1.conectarParada( p1.codigo, e1.codigo, e2.codigo, 2)
    m1


def main():
    ejecutarDemostracionmodelo()
    

if __name__ == '__main__': main()