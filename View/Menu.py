try:
    from base import limpiarConsola
except:
    from view.base import limpiarConsola

#region metodos generales
def mostrarmenu( pmenuOpciones:dict):
    for clave in pmenuOpciones:
        tecla = clave
        opcion = pmenuOpciones[clave]
        print("   ["+str(tecla)+"]: "+opcion)
        del tecla
        del opcion
    
def capturarEleccion(pOpcionesmenu:dict):
    eleccion = input(">>")
    if not estaEleccionEsValida( eleccion, pOpcionesmenu):
        limpiarConsola()
        print("Opcion no valida - por favor intente de nuevo")
        mostrarmenu(pOpcionesmenu)
        eleccion = capturarEleccion( pOpcionesmenu)
    return eleccion

def estaEleccionEsValida( pEleccion, pOpcionesmenu:dict):
    laOpcionEsValida = False
    for cadaOpcion in pOpcionesmenu:
        unaOpcion = str(cadaOpcion)
        if pEleccion == unaOpcion:
            laOpcionEsValida = True
            break
    return laOpcionEsValida

def interactuarConmenu( pOpcionesmenu:dict):
    mostrarmenu( pOpcionesmenu)
    eleccion = capturarEleccion( pOpcionesmenu)
    del pOpcionesmenu
    limpiarConsola()
    return eleccion

#endregion

def interactuarConmenuPrincipal():
    opcionesmenu = {1:"crear mapa",'q':"salir"}
    return interactuarConmenu( opcionesmenu)

#region op1:crear mapa
def interactuarConmenuCrearMapa():
    opcionesmenu = {1:"añadir carreteras",2:"conectar carreteras",3:"listar esquinas",'q':" <- volver"}
    return interactuarConmenu( opcionesmenu)
