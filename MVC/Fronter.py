from MVC.Modelo import *
def saludar():
    print("Bienvenido")

def enter():
    print("\n")

def presentarEsquina( pEsquina:Esquina):
    return "carrera "+pEsquina.carrera+" con calle "+pEsquina.calle

def estanConectadasLasEsquinas( pEsquina1:Esquina, pEsquina2:Esquina):
    enter()
    print("verificando conexion mutua entre esquinas ...")
    if pEsquina1.estaConectadoCon(pEsquina2) and pEsquina2.estaConectadoCon(pEsquina1):
        print(presentarEsquina(pEsquina1) + " esta conectado con " + presentarEsquina( pEsquina2))
    else:
        print(presentarEsquina(pEsquina1) + " no esta conectado con " + presentarEsquina( pEsquina2))
    enter()

def imprimirNuevaConexion(pEsquina1:Esquina, pEsquina2:Esquina):
    print(presentarEsquina(pEsquina1)+" y "+presentarEsquina( pEsquina2)+" se han conectado.")


