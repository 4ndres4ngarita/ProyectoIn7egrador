Refactorizacion base.py - buscadores y comparadores
=

   *se volvió a refactorizar base.py
   *nuevo comparadoresDeNodos.py!: compara atributos con parametros de nodos completos o con valores de atributos
   *nuevo buscadoresDeConexiones.py!: todas sus clases, por el momento, se basan en una sola interfaz. algunas implementaciones solo requieren de la lista ( listas de nodo en crudo) del los nodos y otro requieren listas del producto de las implementaciones anteriores (listas de nodos procesadas).