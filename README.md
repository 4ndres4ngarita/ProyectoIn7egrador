Definir trabajo de cada capa en el modelo MVC
=
    *Modelo de trabajar con objetos directamente y no recibir usualmente parametros de tipo de dato comun (int o str) a excepcion de los metodos constructores.

    *de lo anterior, la clase Vertice tiene los atributos:
        **sentidoCardinal("refiriendose al sentido segun los puntos cardinales").
        **direccionvestorial("que vendria siendo el reemplazo al atributo eliminado 'sentido'").

    *Hay problemas con la nomenclatura para nombrar los nodos ( o esquinas):
        **la clase Model.Esquina tiene atributo 'anexo' para poder describir con precicion el id, en casos especiales.
        **De los casos o cuestiones estan las glorietas(roundpoint) e intersecciones que no pueden cruzarse por un lado.
