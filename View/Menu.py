try:
    from Base import limpiarConsola
except:
    from View.Base import limpiarConsola

#region metodos generales
def mostrarMenu( pMenuOpciones:dict):
    for clave in pMenuOpciones:
        tecla = clave
        opcion = pMenuOpciones[clave]
        print("   ["+str(tecla)+"]: "+opcion)
        del tecla
        del opcion
    
def capturarEleccion(pOpcionesMenu:dict):
    eleccion = input(">>")
    if not estaEleccionEsValida( eleccion, pOpcionesMenu):
        limpiarConsola()
        print("Opcion no valida - por favor intente de nuevo")
        mostrarMenu(pOpcionesMenu)
        eleccion = capturarEleccion( pOpcionesMenu)
    return eleccion

def estaEleccionEsValida( pEleccion, pOpcionesMenu:dict):
    laOpcionEsValida = False
    for cadaOpcion in pOpcionesMenu:
        unaOpcion = str(cadaOpcion)
        if pEleccion == unaOpcion:
            laOpcionEsValida = True
            break
    return laOpcionEsValida

def interactuarConMenu( pOpcionesMenu:dict):
    mostrarMenu( pOpcionesMenu)
    eleccion = capturarEleccion( pOpcionesMenu)
    del pOpcionesMenu
    limpiarConsola()
    return eleccion

#endregion

def interactuarConMenuPrincipal():
    opcionesMenu = {1:"crear mapa",'q':"salir"}
    return interactuarConMenu( opcionesMenu)

#region op1:crear mapa
def interactuarConMenuCrearMapa():
    opcionesMenu = {1:"añadir carreteras",2:"conectar carreteras",3:"listar esquinas",'q':" <- volver"}
    return interactuarConMenu( opcionesMenu)
