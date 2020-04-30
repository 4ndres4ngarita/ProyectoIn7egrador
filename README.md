Refactorizacion Solo de base.py - setters y getters
=

   *Se creó el archivo sentidosGeoespaciales.py donde estan las clases o posibilidades de los atributos direccionCardinal y direccionVectorial de la clase Conexion.Aquí se implementó el reemplazo de constantes numericas por "variables constantes".
   *los atributos de las clases en el archivo base.py pasaron a ser privadas, junto con setters y getters.
   *Se trató de refactorizar usando y evidenciando el concepto de Responsabilidad Unica
   *conexion.numero fue cambiado por conexion.numeroDeConexion
   *Se eliminó cierto codigo en este commit en el archivo base.py, sin embargo, esta en realidad esta reservado para hacerle una refactorizacion, debido a cuestiones de abstraccion, segun Andres :)