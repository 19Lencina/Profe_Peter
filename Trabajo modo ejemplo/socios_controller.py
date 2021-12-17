import socios_model


###################################
### Definción de la clase Socio ###
###################################
class Socio:
    
    # Definimos las constantes de la clase
    CUOTA_SOCIO = 100.0
    DESCUENTO_MENORES = 0.5
    DESCUENTO_FAMILIA_NUMEROSA6 = 0.2
    DESCUENTO_FAMILIA_NUMEROSA10 = 0.3

    # constructor que toma como parámetro el id, nnombre, apellido, dni, 
    # cantidad del grupo familiar y cantidad de menores de 18 años que 
    # integran el grupo familiar.
    #RespuestaEjercicio: agregado de cuota en el constructor del socio, inicializado en 0.0
    #De esta manera, cada vez que creamos un objeto, la propiedad cuota tendr� como valor un tipo float.
    def __init__(self, id_socio, nombre_socio, apellido_socio, DNI_socio, 
                    cant_grupo_familiar, cant_menores18, nombre_y_apellido=""): 
        self.id_socio = int(id_socio)
        self.apellido_socio = apellido_socio
        self.nombre_socio = nombre_socio
        self.DNI_socio = DNI_socio
        self.cant_grupo_familiar = int(cant_grupo_familiar)
        self.cant_menores18 = int(cant_menores18)
        self.nombre_y_apellido = nombre_socio + " " + apellido_socio
  
    # método que busca desde el modelo, los datos de un socio, en base al id.
    # retorna un objeto de tipo Socio, con los datos encontrados en sus propiedades.
    def obtener_socio_x_Id(self):
        # guardamos en la Tupla "socio_encontrado" el resultado del llamado 
        # de la funcion "buscar_socio_x_Id".
        socio_encontrado = socios_model.buscar_socio_x_Id(self.id_socio)
        # si la búsqueda fue existosa creamos un OBJETO de tipo Socio y lo 
        # guardamos en "socio_devuelto". Le damos como parámetro al constructor,
        # cada posición de la tupla socio_encontrado[x], ya que son los valores
        # de las propiedades del socio (nombre, apellido, nro de documento, etc).
        if socio_encontrado:
            
            #RespuestaEjercicio: agregado de "socio_encontrado[6]", referencia a la cuota en la tupla
            socio_devuelto = Socio(socio_encontrado[0], socio_encontrado[1], 
                                    socio_encontrado[2], socio_encontrado[3], 
                                    socio_encontrado[4], socio_encontrado[5], socio_encontrado[6]) 
            # retornamos el objeto socio con sus propiedades seteadas.
            return socio_devuelto 
        else:
            # si no se encuentra el socio buscado el modelo habrá devuelto un
            # FALSE y eso es lo que devolvemos
            return socio_encontrado
    
    # método que pasa al modelo los datos del socio (como tupla) y devuelve el
    # OBJETO socio_guardado
    def guardar_socio(self):
        # pasamos al modelo los datos del socio como tupla y guardamos la tupla 
        # recibida del modelo en socio_nuevo
        
        #RespuestaEjercicio: seteamos la propiedad "cuota" objeto Socio con el valor de retorno del m�todo "calcular_cuta()" (l�nea 59).
        #RespuestaEjercicio: agregado del par�metro "self.cuota" en el constructor (l�nea 62).
        #RespuestaEjercicio: agregado del par�metro "socio_encontrado[6]" (posici�n donde tenemos el valor de la cuota) para la construcci�n del objeto Socio (l�nea 66).
        self.cuota = self.calcular_cuota() 
        socio_nuevo = socios_model.alta_socio((self.id_socio, self.nombre_socio, 
                                        self.apellido_socio, self.DNI_socio, 
                                        self.cant_grupo_familiar, self.cant_menores18, self.nombre_y_apellido)) 
        # con los elementos de la tupla recibida, creamos un OBJETO socio
        socio_guardado = Socio(socio_nuevo[0], socio_nuevo[1], socio_nuevo[2], 
                                socio_nuevo[3], socio_nuevo[4], socio_nuevo[5], socio_nuevo[6]) 
        return socio_guardado # devolvemos el objeto socio

    # método que pasa al modelo la id del socio a elminar
    def eliminar_socio(self):
        return socios_model.baja_socio(self.id_socio)

    # método que pasa que pasa al modelo la tupla con los datos del socio a modificar
    def modificar_socio(self):
        #RespuestaEjercicio: inicializamos la propiedad "self.cuota" con el resultado de la llamada al m�todo "calcular_cuota"
        self.cuota = self.calcular_cuota()
        #RespuestaEjercicio: agregado del parámetro "self.cuota". (l�nea 81).
        socio_modificado = (self.id_socio, self.nombre_socio, self.apellido_socio,
                    self.DNI_socio, self.cant_grupo_familiar, self.cant_menores18, self.nombre_y_apellido) 
        return socios_model.modificacion_socio(socio_modificado) # devolvemos el resultado

    # método que calcula la cuota en función de los datos del socio
    # y los valores definidos
    def calcular_cuota(self):
        cuota_grupo_familiar = (self.CUOTA_SOCIO * 
                            (self.cant_grupo_familiar-self.cant_menores18) +
            self.CUOTA_SOCIO * (1-self.DESCUENTO_MENORES) * self.cant_menores18)
        if self.cant_grupo_familiar>=10:
            return cuota_grupo_familiar * (1 - self.DESCUENTO_FAMILIA_NUMEROSA10)
        elif self.cant_grupo_familiar>=6:
            return cuota_grupo_familiar * (1 - self.DESCUENTO_FAMILIA_NUMEROSA6)
        else:
            return cuota_grupo_familiar
