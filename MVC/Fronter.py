from MVC.Modelo import *
import os

def saludar():
    print("Bienvenido")

def enter():
    print("\n")
    
def limpiarConsola():
    os.system('cls' if os.name == 'nt' else 'clear')

def estanConectadasLasEsquinas( pEsquina1:Esquina, pEsquina2:Esquina):
    enter()
    print("verificando conexion mutua entre esquinas ...")
    if pEsquina1.estaConectadoCon(pEsquina2) and pEsquina2.estaConectadoCon(pEsquina1):
        print(presentarNodo(pEsquina1) + " esta conectado con " + presentarNodo( pEsquina2))
    else:
        print(presentarNodo(pEsquina1) + " no esta conectado con " + presentarNodo( pEsquina2))
    enter()

def imprimirNuevaConexion(pEsquina1:Esquina, pEsquina2:Esquina):
    print(presentarNodo(pEsquina1)+" y "+presentarNodo( pEsquina2)+" se han conectado.")

#region funciones para clase Nodo y Vertice
def presentarNodo(pNodo:Nodo):
    switch = {
        "Esquina": "carrera "+pNodo.carrera+" con calle "+pNodo.calle
    }

    return switch.get(pNodo.tipo, "nodo #"+str(pNodo.id))

def estanConectados( pNodo1:Nodo, pNodo2:Nodo):
    enter()
    print("verificando conexion mutua entre nodos ...")
    if pNodo1.estaConectadoCon(pNodo2) and pNodo2.estaConectadoCon(pNodo1):
        print(presentarNodo(pNodo1) + " esta conectado con " + presentarNodo( pNodo2))
    else:
        print(presentarNodo(pNodo1) + " no esta conectado con " + presentarNodo( pNodo2))
    enter()

def imprimirNuevaConexion(pNodo1:Esquina, pNodo2:Esquina):
    print(presentarNodo(pNodo1)+" y "+presentarNodo( pNodo2)+" estan vinculados.")
#endregion

