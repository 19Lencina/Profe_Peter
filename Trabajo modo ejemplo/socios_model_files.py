import pathlib # librería que brinda herramientas para trabajar con los paths de los archivos
from os import rename, remove

###############################################################################
### Función retorna el objeto f que es un objeto file (archivo)             ###
### recibe como parámentros un moco de apertura, y el nombre del achivo     ###
### (este parámetro si no es recibido por defecto toma el valor socios.txt) ### 
###############################################################################
def abrir_conexion(modo, file_name = 'socios.txt'):
    try: # utilizamos un try, ya que nuestro código puede generar excepciones
        # creamos un objeto PATH, con la libraria pathlib y el método .path() 
        # que toma como parámetro la ubicación y nombre del archivo
        # y nombramos al objeto socios_path
        file_path = pathlib.Path(file_name)
        if file_path.exists() and modo == 'leer': # preguntasmo con el
            # método .exists() de los objetos path si este existe
            # Si existe y además el modo recibido como parámentro es 
            # 'escribir' abrimos el archivo y generarmos un objeto file con la
            # función open() que toma como parámetros el path (que nosotros ya 
            # lo habíamos nombrado como socios_paht), y los siguientes parámetros: 
            # 'a' = append - Abre un archivo para añadirlo, 
            # crea el archivo si no existe
            # 'r' = read - Valor por defecto. Abre un archivo para su lectura, 
            # error si el archivo no existe 
            # 'w' = write - Abre un archivo para escribir, 
            # reemplazando el archivo que exista con ese mismo nombre 
            # 'x' = create - Crea el archivo especificado, 
            # devuelve un error si el archivo existe
            f = open(file_path, 'r')
            # si el archivo no existe y el modo es leer
        elif not(file_path.exists()) and modo == 'leer':
            f = open(file_path, 'a') # creamos el archivo
            f = open(file_path, 'r') # abrimos el archivo en modo lectura
        else:  # si el path no existe, creamos el objeto archivo con el parámetro
               # 'w' para que se cree el archivo 
            f = open(file_path, 'a')
        print("El archivo de datos fue abierto de forma correcta")
        return f # retornamos el objeto socios_file de tipo file 
    # si se genera una excepción lo guardamos en "error_capturado"
    except (Exception) as error_capturado: 
        print("Ocurrió el siguiente error al abrir el archivo de datos: ", 
                        error_capturado) # mostramos el error por consola.
    

###############################################################################
### Función cierra el archivo cuyo nombre recibe como parámetrojeto archivo ###
###############################################################################
def cerrar_conexion(file_name):
    try: 
        file_name.close() # el método .close() de los objetos file cierra el archivo
        print("El archivo de datos fue cerrado de forma correcta")
    except (Exception) as error_capturado:
        print("Ocurrió el siguiente error al cerrar el archivo de datos: ",
                        error_capturado)


###############################################################################
### Función retorna una tupla con los datos del socio que                   ###
### tenga el id_buscar pasado como parámetro                                ###
###############################################################################
def buscar_socio_x_Id(id_buscar):
    try: # utilizamos un try, ya que nuestro código puede generar una excepción.
        # guardamos en socios_file el retorno de la función abrir_conexion()
        socios_file = abrir_conexion('leer') 
        # el metodo .readlines() de los files genera una lista 
        # donde cada línea es un elemento
        for line in socios_file.readlines(): 
            if line.split(',')[0]=='#' or line.split(',')[0]!=str(id_buscar): 
                continue # si la línea no comienza con un '#' ni el id de socio 
                # de la línea coincide con el que se quiere modificar se escribe
                # la línea en el nuevo archivo.
                # el método .split() de las strings genera una lista tomando 
                # como separador la cadena pasada como parámetro
            # si el id de socio de la línea coincide con el que se quiere buscar
            elif line.split(',')[0]==str(id_buscar):
                socio_buscado = tuple(line.rstrip().split(',')) 
                # socio_buscado es el string de la línea del archivo convertida 
                # en tupla.
                # el método .rstrip() de las strings renueve los todos los 
                # marcadores, en nuestro caso necesitamo remover \n del salto 
                # de línea
        return socio_buscado # devuelve la tupla socio que obtuvimos 
                             #de la lectura y búsqueda en el archivo
    except:
        return False # si se genera una excepción devolvemos un False
    finally: # el bloque finally siempre se ejecuta por lo que siempre cerramos el archivo
        cerrar_conexion(socios_file)


###############################################################################
### Función que modifica el socio pasado como parámetro                     ###
###############################################################################
#Función que modifica los datos de un socio, dado el parámetro dado.
def modificacion_socio(socio_modificado, delete_mark=''):
    try: # utilizamos un try, ya que nuestro código puede generar una excepción.
        # abrimos el archivo socios.txt y guardamos el objeto en socios_file_old
        socios_file_old = abrir_conexion('leer', 'socios.txt')
        # lo mismo pero para el archivo socios_temp.txt pero en modo escribir 
        socios_file_new = abrir_conexion('escribir', 'socios_temp.txt') 
        # convetimos la tupla en string
        socio_string = delete_mark + ','.join(map(str, socio_modificado)) + '\n' 
        # La función map() devuelve un objeto map con los resultados de aplicar 
        # la función dada, en nuestro caso str() a cada elemento de un objeto 
        # iterable dado (lista, tupla, etc.)
        # El método .join() de las strings une en una sola string todos los 
        # elementos del ojeto iterable que se le pase como parámetro, 
        # en nuestor caso el objeto map, separados por la string sobre la que 
        # se ejecuta el métido en nuestro caso la string ','
        for line in socios_file_old: # para cada linea en socios_file_old
            # si la línea no comienza con un '#' ni el id de socio de la línea
            # coincide con el que se quiere modificar se escribe la línea en el 
            # nuevo archivo
            if line.split(',')[0]=='#' or line.split(',')[0]!=str(socio_modificado[0]): 
                socios_file_new.write(line) 
            # si el id de socio de la línea coincide con el que se quiere 
            # modificar se escribe el socio modificado (pasado a string)
            elif line.split(',')[0]==str(socio_modificado[0]):
                socios_file_new.write(socio_string) 
        return True  # retornamos un True si se pudo escribir correctamente 
                     # el socio modificado en el archivo
    except:
        return False # si se genera una excepción devolvemos un False
    finally: # el bloque finally siempre se ejecuta por lo que siempre cerramos los archivos
        cerrar_conexion(socios_file_old) # cerramos el archivo socios.txt
        cerrar_conexion(socios_file_new) # cerramos el archivo socios_temp.txt
        # como vamos a borrar socios.txt verificamos que socios_temp.txt existe
        if pathlib.Path('socios_temp.txt').exists(): 
            remove('socios.txt') # eliminamos el archivo socios.txt
            #renombramos el archivo socios_temp.txt como socios.txt
            rename('socios_temp.txt', 'socios.txt')
            # remove() y rename() son dos funciones de la librería os 
            # (operating sistem) de Python 


###############################################################################
### Función que elimina el socio con el id pasado como parámetro            ###
###############################################################################
def baja_socio(id_eliminar):
    try: # utilizamos un try, ya que nuestro código puede generar una excepción.
        # buscamos el socio a elminar
        socio_a_borrar = buscar_socio_x_Id(id_eliminar)
        # modificacion_socios() devuelve True o False
        socio_borrado = modificacion_socio(socio_a_borrar, '#,') 
        # retornamos un True si se puedo escribir correctamente el socio 
        # modificado en el archivo
        return socio_borrado 
    except:
        return False # si se genera una excepción devolvemos un False


###############################################################################
### Función que agrega el socio pasado como parámetro                       ###
###############################################################################
def alta_socio(socio):
    try: # utilizamos un try, ya que nuestro código puede generar una excepción.
        # guardamos en socios_file el retorno de la función abrir_conexion()
        # en modo leer el archivo socios.txt
        socios_file = abrir_conexion('leer', 'socios.txt') 
        # el método file.readlines(), divide el archivo en una lista,
        # donde cada elemento es una línea del archivo
        # el método len() cuenta las líneas y 
        # le sumamos 1 para obtener el id_socio siguiente
        id_socio_nuevo = len(socios_file.readlines()) + 1 , 
        # guardamos en socios_file el retorno de la función abrir_conexion()
        # en modo escribir el archivo socios.txt
        socios_file = abrir_conexion('escribir', 'socios.txt')
        # generamos la tupla socio_nuevo con los datos del nuevo socio
        socio_nuevo = (id_socio_nuevo, socio[1], socio[2], socio[3], socio[4], 
                        socio[5])
        # convetimos la tupla en string
        socio_string = ','.join(map(str, socio_nuevo)) + '\n' 
        # La función map() devuelve un objeto map con los resultados de aplicar 
        # la función dada, en nuestro caso str() a cada elemento de un objeto 
        # iterable dado (lista, tupla, etc.)
        # El método .join() de las strings une en una sola string todos los 
        # elementos del ojeto iterable que se le pase como
        # parámetro, en nuestor caso el objeto map, separados por la string 
        # sobre la que se ejecuta el métido en nuestro caso la string ','
        socios_file.write(socio_string)  # El método file.write() 
        # escribe el parámetro (pero solo toma strings)
        # que recibe, al final del archivo (pero como agregamos a la string \n 
        # entonces cada socio será una línea nueva)
        return socio_nuevo # retorna la tupla con los datos del socio nuevo
    except:
        return False # si se genera una excepción devolvemos un False
    finally: # el bloque finally siempre se ejecuta por lo que siempre cerramos el archivo
        cerrar_conexion(socios_file)

# alta_socio([1,'Steve','Rogers','26505640',0,0])
# alta_socio([1,'Clark','Kent','26505641',4,2])
# alta_socio([1,'Peter','Parker','26505642',2,1])
# print(alta_socio([1,'Bruce','Wayne','26505643',3,0]))

# print(buscar_socio_x_Id(1))

# modificacion_socio([3,'Peter','Parker','45505642',4,1])
# print(buscar_socio_x_Id(3))

# alta_socio([1,'Bruce','Wayne','26505643',3,0])
# print(buscar_socio_x_Id(3))

# baja_socio(5)