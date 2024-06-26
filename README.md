# PyInstaller_GUI
![image](lib/icon.ico)

Este repositorio contiene el script Pyinstaller de forma gráfica para facilitarnos un poco la creación de programas ejecutables. Requiere `Python 3`.

Esta es una iniciativa para transportar esas herramientas vitales que usamos cuando programamos en python, así ahorramos tiempo ya que en lugar de escribir y memorizar codigo, lo único que tendremos que hacer será dar un par de clics.

Eres libre de agregar o modificar lo que quieras, perfeccionemos juntos esta herramienta gráfica.

## PyInstaller_GUI puede hacer lo siguiente:

* La posibilidad de elegir el icono del "exe".

* Elegir si se crea un archivo unico o distribuido en carpetas.

* Elegir si se desea el programa ventaneado o no.

* Brinda la posibilidad de cifrar el codigo del programa.

* La opcion para correr el programa con permisos de administrador.

* La opcion para vaciar la cache y compilar el programa sin ningun error o interferencia del codigo anterior.

* Agregar de manera sencilla los archivos y carpetas al "exe", para esto vea el apartado a continuacion llamado [`Funcion que resuelve rutas`](https://github.com/anewri32/PyInstaller_GUI#funcion-que-resuelve-rutas).

* La posibilidad de incluir informacion en el "exe" sobre la version, nombre, compañia, ect.


## Uso

El uso de esta aplicacion es tan simple como clonar o descargar en zip el repositorio, seguido de ejecutar el archivo `PyInstaller_GUI`, y eso es todo. La interfaz fue hecha para que sea intiutiva, no le costara usarla.


## Funcion que resuelve rutas:

Pyinstaller y PyInstaller_GUI dan la posibilidad de añadir archivos al exe, pero ambos necesitan que los mismos programas sean quienes resuelvan las rutas de sus respectivos archivos, es por esto que depende de usted agregar esta caracteristica a su codigo.

A continuacion un ejemplo de lo que seria una funcion que resuelve rutas:


[`Resolver_ruta.py`](Resolver_ruta.py)
```py
import os, sys

def resolver_ruta(ruta_relativa):
    if hasattr(sys, '_MEIPASS'):
        return os.path.join(sys._MEIPASS, ruta_relativa)
    return os.path.join(os.path.abspath('.'), ruta_relativa)
```
### Ejemplo de la llamada a la funcion:
```py
# Normalmente la ruta se especifica de esta manera:
root.iconbitmap('img/icon.ico')

# Entonces, para incluir la funcion que resuelve rutas, se coloca de esta manera:
root.iconbitmap(resolver_ruta('img/icon.ico'))    
```
