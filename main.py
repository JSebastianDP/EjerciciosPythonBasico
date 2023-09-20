import os
import pathlib
from pathlib import Path, PurePath

ruta = "Esta es la ruta que estoy usando para el script de python con la libreria os "
ruta2 = "Esta es la ruta que estoy usando para el script de python con la libreria pathlib "
#Sirve para mostrar en consola la ruta en donde se esta ejecutando el script, las variables solo son complementarias para guiarme
#print(ruta + os.getcwd())
#print(ruta2, Path.cwd())

#os.listdir sirve para listar los archivos en el directorio en que me encuentro
Archivos = "Los archivos en el directorio en el que me encuentro son: "
#print(Archivos, os.listdir())

#así se listarian los de una carpeta especifica con os
#print(Archivos, os.listdir('carpeta'))



Archivos2 = "Asi se listan los archivos con path"

#print(list(Path().iterdir()))
#así se listarian los de una carpeta especifica con path

#print(list(Path('carpeta').iterdir()))

#Juntar rutas con os
#print(os.path.join(os.getcwd(), 'CarpetaOS'))

#Juntar rutas con path
#print(PurePath.joinpath(Path.cwd(), 'CarpetaPath'))


#Crear carpetas usando python
#os.mkdir('CarpetaCreadaConOs')
#Crear carpeta con path, ventaja de path es que se puede comprobar si la carpeta existe o no

#Path('CarpetaCreadaConPath').mkdir(exist_ok=True)

#Crear carpetas dentro de otras carpetas
#os.makedirs(os.path.join('CarpetaCreadaConOs', 'SubCarpetaOs'))

#PurePath.joinpath(Path.cwd(), 'CarpetaCreadaConPath', 'SubCarpetaPath').mkdir(parents=True)

#Renombrar carpetas con os
#os.rename('CarpetaCreadaConOS', 'CarpetaOS')

#Renombrar carpetas con path, se necesitan 2 variables 1 con el nombre de la carpeta antigua y otra con el nombre deseado
path_acual = Path('CarpetaCreadaConPath')
path_nuevonombre= Path('CarpetaNuevaPath')
#Metodo para renombrar una vez creadas las 2 varialbes
#Path.rename(path_acual, path_nuevonombre)

#verificar si un archivo existe
print(os.path.exists('CarpetaOs'))
#verificar si un archivo existe con path
nombrearchivo= Path('CarpetaNuevaPath')
print(nombrearchivo.exists())

#Metadata ayuda a obtener la ruta absoluta de una carpeta indicata
print(os.path.abspath('CarpetaOs'))

script = Path('main.py')

#Prueba con path
#print(script.resolve())
#Saber la extension de un archivo
#print(script.stem)
#print(script.suffix)
#saber el tamaño de un archivo
print(script.stat().st_size)
