Este es un intento de un directorio de organizaciones mexicanas relacionadas con FOSS o alguna de sus variaciones. 

Si quieres agregar la tuya, edita la wiki.

Pre-requisitos
--------------

Tienes que tener instalado *make* y *rst2pdf* para poder construir el PDF.


Instrucciones
-------------

Para generar el directorio en PDF, solo corre:

.. code-block:: Bash

    make all


¿Cómo agrego mis datos?
-----------------------

#. Clona el repo.

#. Crea tu hoja en *src/*; utilizando el formato reStructured.

#. Agrégalo con un include; en orden alfabético, a *src/main.rst*. 

#. Prueba generar el PDF.

#. Haz un *pull request*.
