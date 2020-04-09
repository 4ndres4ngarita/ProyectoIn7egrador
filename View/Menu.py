try:
    from base import limpiarConsola
except:
    from view.base import limpiarConsola

#region metodos generales
def mostrarMenu( pMenuOpciones:dict):
    for clave in pMenuOpciones:
        tecla = clave
        opcion = pMenuOpciones[clave]
        print("   ["+str(tecla)+"]: "+opcion)
        del tecla
        del opcion
    
def capturarOpcion(pOpcionesMenu):
    eleccion = input(">>")
    if not estaOpcionEsValida( eleccion, pOpcionesMenu):
        limpiarConsola()
        print("Opcion no valida - por favor intente de nuevo")
        mostrarMenu(pOpcionesMenu)
        eleccion = capturarOpcion( pOpcionesMenu)
    return eleccion

def estaOpcionEsValida( pEleccion, pOpcionesMenu):
    laOpcionEsValida = False
    for siguienteOpcion in pOpcionesMenu:
        if str(siguienteOpcion) == pEleccion:
            laOpcionEsValida = True
    return laOpcionEsValida
#endregion

def lanzarMenuPrincipal():
    opcionesMenuprincipal = {1:"revisar mapa",'q':"salir"}
    mostrarMenu( opcionesMenuprincipal)
    eleccion = capturarOpcion( opcionesMenuprincipal)
    del opcionesMenuprincipal
    limpiarConsola()
    return eleccion