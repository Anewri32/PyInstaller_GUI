# PyInstaller_GUI V2.0
Este repositorio contiene el script Pyinstaller de forma gráfica para facilitarnos un poco la creación de programas ejecutables.

Esta es una iniciativa para transportar esas herramientas vitales que usamos cuando programamos en python, así ahorramos tiempo ya que en lugar de escribir y memorizar codigo, lo único que tendremos que hacer será dar un par de clics.

Eres libre de agregar o modificar lo que quieras, perfeccionemos juntos esta herramienta gráfica.

PyInstaller_GUI puede hacer lo siguiente:

*la posibilidad de elegir el icono del "exe".

*elegir si se crea un archivo unico o distribuido en carpetas.

*elegir si se desea el programa ventaneado o no.

*da la posibilidad de cifrar el codigo del programa.

*la opcion para correr el programa con permisos de administrador.

*la opcion para vaciar la cache y compilar el programa sin ningun error o interferencia del codigo anterior.

*agregar de manera sencilla los archivos y carpetas al "exe", para esto vea el apartado a continuacion llamado "Funcion que resuelve rutas".

*la posibilidad de incluir informacion en el "exe" sobre la version, nombre, compañia, ect.


Funcion que resuelve rutas:

Pyinstaller y PyInstaller_GUI dan la posibilidad de añadir archivos al exe, pero ambos necesitan que los mismos programas sean quienes resuelvan las rutas de sus respectivos archivos, es por esto que depende de usted agregar esta caracteristica a su codigo.

A continuacion un ejemplo de lo que seria una funcion que resuelve rutas:

import os, sys

def resolver_ruta(ruta_relativa):
    if hasattr(sys, '_MEIPASS'):
        return os.path.join(sys._MEIPASS, ruta_relativa)
    return os.path.join(os.path.abspath('.'), ruta_relativa)


    