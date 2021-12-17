import pymysql
from pymysql.err import Error

#   Sólo para tener de referencia la estructura de la tabla
#   TABLE `socios` 
#   (
#   `id_socio` int(11) NOT NULL,
#   `nombres_socio` text NOT NULL,
#   `apellidos_socio` text NOT NULL,
#   `dni_socio` bigint(20) NOT NULL,
#   `cant_grupo_familiar` int(11) NOT NULL DEFAULT 0,
#   `cant_menores18` int(11) NOT NULL DEFAULT 0
#   ) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;


###############################################################################
### Función que retorna la conexión a la base de datos.                     ###
### prestar atención a los parámetros para que la conexión sea exitosa.     ###
###############################################################################
def abrir_conexion():
    try: # utilizamos un try, ya que nuestro código puede generar excepciones
        # guardamos la conexión en un objeto de tipo Connection,  dando los 
        # parámetros necesarios para crear/ejecutar la conexión.
        conexion = pymysql.connect(host='localhost',
                                    user='root',
                                    password='',
                                    db='abm_socios')
        print("La conexión a la base de datos fue correcta")
        return conexion # retornamos el objeto "conexion" de tipo Connection.
    # si se genera una excepción lo guardamos en "error_capturado"
    except (Exception, Error) as error_capturado: 
        print("Ocurrió el siguiente error en la conexión a la base de datos: ",
                error_capturado) # mostramos el error por consola.
    
###############################################################################
### Función que CIERRA la conexión... no devuelve nada, ni modifica,        ###
### sólo cierra la conexión recibida como parámentro.                       ###
###############################################################################
def cerrar_conexion(conexion):
    try: 
        conexion.close() # el método .close() de las conections cierra la conexión
        print("La conexión a la base de datos cerrada de forma correcta")
    # si se genera una excepción lo guardamos en "error_capturado"
    except (Exception, Error) as error_capturado: 
        print("Ocurrió el siguiente error al cerrar la conexión a la base de datos: "
                , error_capturado) # mostramos el error por consola.

###############################################################################
### Función recibe un id_socio como parámetro, busca en la BD el socio      ###
### con ese id, y devuelve una tupla con los datos de socio encontrado.     ###
###############################################################################
def buscar_socio_x_Id(id_buscar):
    try: # utilizamos un try, ya que nuestro código puede generar una excepción.
        # guardamos en "conexion" el retorno de la función "abrir_conexion".
        conexion = abrir_conexion() 
        # guardamos en "cursor" un objeto de tipo Cursor relacionado a la
        # conexión, de esta manera podremos ejecutar diferentes consultas, y 
        # obtener los resultados obtenidos de la conexión con la base de datos.
        cursor =  conexion.cursor()
        # creamos un string con el contenido de la sentencia SQL que 
        # ejecutaremos en la base de datos. 
        #RespuestaEjercicio: agregado de cuota en el sql
        query = 'SELECT id_socio, nombres_socio, apellidos_socio, dni_socio, \
                cant_grupo_familiar, cant_menores18, nombre_y_apellido \
                FROM socios WHERE id_socio = %s;'
        # con el método .execute de los cursors ejecutamos la sentencia SQL
        # de la query, y que será completada con el valor de id_buscar recibido
        cursor.execute(query, id_buscar)
        # guardamos en la Tupla "socio", el primer dato encontrado en la consulta.
        socio = cursor.fetchone()
        # retornamos La tupla "socio" que obtuvimos en la consulta.
        return socio
    # Si se genera una excepción (algún error desde la base de datos,
    # en la conexión, etc) devolvemos un False
    except:
        return False
    # el bloque finally siempre se ejecuta por lo que siempre cerramos la conexión.
    finally: 
        cerrar_conexion(conexion)


# Función que modifica los datos de un socio, dado el parámetro dado.
def modificacion_socio(socio):
    # utilizamos un try, ya que nuestro código puede generar excepciones.
    try:
        conexion = abrir_conexion()
        cursor =  conexion.cursor()
        #RespuestaEjercicio: agregado de la cuota en el sql (l�nea 91)
        query = 'UPDATE socios SET nombres_socio = %s, apellidos_socio = %s, \
            dni_socio = %s, cant_grupo_familiar = %s,\
            cant_menores18 = %s, nombre_y_apellido=%s WHERE id_socio = %s;' 
            
        #cant_menores18 = %s WHERE id_socio = %s;'
        # guardamos en values, los valores que guardamos en cada una de las 
        # posiciones de la tupla socio recibida como parámetro
        values = (socio[1], socio[2], socio[3], socio[4], socio[5], socio[6], socio[0])
        # con el método .execute de los cursors ejecutamos la sentencia SQL
        # de la query, completada con la tupla values
        # donde están los datos modificados del socio.
        cursor.execute(query, values)
        # mediante el método .commit() de las conections se ejecuta la 
        # modificacion de forma definitiva en la tabla.
        conexion.commit()
        # devolvemos True, como bandera afirmativa que todo ha salido bien.
        return True
    # retornamos False, como bandera de que algo ha salido mal.
    except:
        return False
    # el bloque finally siempre se ejecuta por lo que siempre cerramos la conexión.
    finally: 
        cerrar_conexion(conexion)


def baja_socio(id_eliminar): 
    # utilizamos un try, ya que nuestro código puede generar excepciones.
    try:
        conexion = abrir_conexion()
        cursor =  conexion.cursor()
        query = 'DELETE FROM socios WHERE id_socio = %s;'
        cursor.execute(query, id_eliminar)
        conexion.commit()
        return True
    # retornamos False, como bandera de que algo ha salido mal.
    except:
        return False
    # el bloque finally siempre se ejecuta por lo que siempre cerramos la conexión.
    finally: 
        cerrar_conexion(conexion)


#Función para dar de alta en la base de datos un socio
def alta_socio(socio):
    try:
        # abrimos la conexión
        conexion = abrir_conexion()
        # creamos un cursor, en base a la conexión con la base de datos. De esta
        # manera podemos ejecutar consultas en la base de datos en la que estemos
        # conectados
        cursor =  conexion.cursor()
        #creamos un string con la consulta que ejecutaremos
        #RespuestaEjercicio: agregado de cuota en el sql (l�nea 143).
        query = 'INSERT INTO socios(nombres_socio, apellidos_socio, dni_socio,\
             cant_grupo_familiar, cant_menores18, nombre_y_apellido) VALUES (%s, %s, %s, %s, %s, %s);' 
        # ejecutamos en el cursor la query (string con la consulta como primer 
        # parámetro) y la tupla "socio[1:]" (como segundo parámetro), 
        # de esta manera, damos como parámetro todo el contenido de la tupla, 
        # sin incluir la primera posición, ya que el id_socio es autoincremental)        
        cursor.execute(query, socio[1:])
        # mediante el método .commit() de las conections se ejecuta la 
        # modificacion de forma definitiva en la tabla.
        conexion.commit()
        # creamos una query donde buscamos el socio con el id mayor (el último 
        # que creamos) para posicionarnos y mostrar dichos valores en 
        # la capa de presentacion (view).
        query = 'SELECT * FROM socios WHERE id_socio = \
                                (SELECT MAX(id_socio) FROM socios)'
        cursor.execute(query) # ejecutamos la sentencia SQL
        # el método .fetchone() de los cursors devuelve un único registro de la BD
        socio = cursor.fetchone()
        return socio # devolvemos la tupla socio con los datos del nuevo socio
    # retornamos False, como bandera de que algo ha salido mal    
    except:
        return False
    # el bloque finally siempre se ejecuta por lo que siempre cerramos la conexión
    finally: 
        cerrar_conexion(conexion)

# alta_socio([1, 'Steve', 'Rogers', '26505640', 0, 0])
# alta_socio([1, 'Clark', 'Kent', '26505641', 4, 2])
# alta_socio([1, 'Peter', 'Parker', '26505642', 2, 1])
# alta_socio([1, 'Bruce', 'Wayne', '26505643', 3, 0])

# print(buscar_socio_x_Id(1))

# modificacion_socio([3, 'Peter', 'Parker', '45505642', 2, 1])
# print(buscar_socio_x_Id(3))

# alta_socio([1, 'Bruce', 'Wayne', '26505643', 3, 0])
# print(buscar_socio_x_Id(5))

# baja_socio(5)