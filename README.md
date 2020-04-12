Primera version de conectar 'paradas' dentro de un mapa. lowercase
=

    *Demostracion de la insercion de un objeto Parada entre dos esquinas dentro de un objeto mapa.

    *Se eliminó el modulo Vias
    *La clase 'vertice', se llama ahora 'conexion' y viene con los atributos:
    **concurrencia y estaConectado, que son atributos que proviene de la clase carretera que ha sido eliminada.
    **numero es un atributo que identifica a una conexion de varias conexiones que pueden existir entre solo dos nodos.

    *clase Nodo tiene metodos para modificar cada atributo de una conexion escogida.

    *Entre los metodos de la clase Nodo estan:
    **añadirConexion(:Conexion)
    **estaConectado(:str)
    **pedirNumeroDeConexionesCon( :str):
    **pedirLaConexionCon(:str,:int)

    *el metodo 'cambiarNodoConectadoPor()' debe retornar, por el momento, el numero de conexion que tiene el Nodo1 con el nuevo nodo vinculado. con el metodo 'reenumerarConexionesCon()' se requiere para reenumerar o reidentificar todas las conexiones que aun sigue teniendo un nodo 2 con el nodo 1. Lo mismo es necesario para reenumerar las conexiones que tiene el nodo 3 (el nuevo) con el nodo 1 teniendo en cuenta la nueva conexion que se agregó.

    *el modulo tiposDeNodos, son clases que heredan de la clase Nodo para ser representacion o abstracciones dentro del programa.

 model/mapa.py
    *Se crea una 'region' para los metodos que interactuan solo con los objetos Esquinas entre ellos mismos.

    *conectarParada() es el metodo que principalmente se quiere destacar en es commit. Sin embargo, es necesario releerlo y optimizarlo, lo mismo que recomiendo para los metodos 'cambiarNodoConectadoPor()' y 'reenumerarConexionesCon()'