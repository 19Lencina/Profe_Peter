import socios_controller
import os

###############################################################################
### FUNCION LIMPIAR PANTALLA CONSOLA                                        ### 
###############################################################################
def screen_clear():
    # para macOS y  linux (os.name es 'posix')
    if os.name == 'posix':
        _ = os.system('clear')
    # para windows platfrom
    else:
        _ = os.system('cls')


###############################################################################
### FUNCION MENU PRINCIPAL                                                  ### 
###############################################################################
def menu_principal():
    item = 0
    while item!=99:
        screen_clear()
        print('')
        print('##################')
        print('### APP SOCIOS ###')
        print('##################')
        print('')
        print('Menú de opciones:')
        print('-----------------')
        print('')
        print(' 1 - Buscar socio x nro de Id')
        print(' 2 - Alta nuevo socio')
        print('99 - Finalizar')
        print('')
        item = int(input('Ingrese la opción deseada y presione ENTER para continuar:\n'))
    
        if item == 1:
            id_socio_a_buscar = ingresar_id_socio()
            socio_buscado = buscar_socio_x_id(id_socio_a_buscar)
            if socio_buscado:
                mostrar_socio(socio_buscado)
                menu_baja_modificacion(socio_buscado)
            else: 
                print('### Búsqueda sin resultados. El Id de Socio:', 
                                        id_socio_a_buscar, 'no existe ###')
                input('Presione ENTER para continuar.\n') 
            continue
        elif item == 2:
            socio_nuevo = ingresar_datos_socio('', 'alta')
            guardar_socio(socio_nuevo)
            continue
        elif item!=99: 
            input('La opción ingresada no es válida, presione ENTER para continuar.\n')


###############################################################################
### FUNCION MENU BAJA / MODIFICACION / CALCULO CUOTA                        ### 
###############################################################################
def menu_baja_modificacion(socio_buscado):
    item = 0
    while item!=99:
        print('Menú de opciones:')
        print('-----------------')
        print('')
        print(' 1 - Elminar socio')
        print(' 2 - Modificar socio')
        print(' 3 - Calcular cuota')
        print('99 - Volver al menu anterior')
        print('')
        item = int(input('Ingrese la opción deseada y presione ENTER para continuar:\n'))
        if item == 1:
            eliminar_socio(socio_buscado)
            input('Presione ENTER para continuar.\n')
            break
        elif item == 2:
            socio_modificado = ingresar_datos_socio(socio_buscado, 'modif')
            modificar_socio(socio_modificado)
            input('Presione ENTER para continuar.\n')
            break
        elif item == 3:
            calcular_cuota(socio_buscado)
            input('Presione ENTER para continuar.\n')
            break
        elif item!=99: 
            print('')
            input('La opción ingresada no es válida, presione ENTER para continuar.\n')

###############################################################################
### FUNCION QUE MUESTRA EL SOCIO RECIBIDO COMO PARAMETRO                    ### 
###############################################################################
def mostrar_socio(socio):
    screen_clear()
    print('')
    print('########################################################')
    print('### DATOS SOCIO ID: {}'.format(socio.id_socio))
    print('########################################################')
    print('--------------------------------------------------------')
    print('Apellido: {}'.format(socio.apellido_socio))
    print('--------------------------------------------------------')
    print('Nombre: {}'.format(socio.nombre_socio))
    print('--------------------------------------------------------')
    print('DNI: {}'.format(socio.DNI_socio))
    print('--------------------------------------------------------')
    print('Cantidad grupo familiar: {}'.format(socio.cant_grupo_familiar))
    print('--------------------------------------------------------')
    print('Cantidad menores de 18 años: {}'.format(socio.cant_menores18))
    print('--------------------------------------------------------')
    print('')
    input('Presione ENTER para continuar.\n')

###############################################################################
### FUNCION PARA INGRESAR ID DE SOCIO A BUSCAR                              ### 
###############################################################################
def ingresar_id_socio(): 
    screen_clear()
    print('')
    print('########################################################')
    print('### Ingrese Id del socio a buscar')
    print('########################################################')
    print('--------------------------------------------------------')
    val_Id_Socio = input('Id Socio: ')
    print('--------------------------------------------------------')
    print('')
    input('Presione ENTER para continuar.\n')
    return val_Id_Socio

###############################################################################
### FUNCION OPCION BUSCAR SOCIO POR LA ID RECIBIDA COMO PARAMETRO           ### 
###############################################################################
def buscar_socio_x_id(id_socio):
    socio_a_buscar = socios_controller.Socio(id_socio, '', '', '', 1, 0)
    socio_buscado = socio_a_buscar.obtener_socio_x_Id()
    return socio_buscado

###############################################################################
### FUNCION PARA INGRESO DE DATOS SOCIO                                     ### 
###############################################################################
def ingresar_datos_socio(socio, tipo_ingreso):
    if tipo_ingreso == 'alta':
        titulo = 'Ingrese los datos del nuevo socio'
    elif tipo_ingreso == 'modif':
        titulo = 'Ingrese los datos a modificar del socio {} \
            (datos sin cambios presione ENTER)'.format(socio.id_socio)
    print('')
    print('########################################################')
    print('### ', titulo)
    print('########################################################')
    print('--------------------------------------------------------')
    val_Apellido = input('Apellido: ')
    print('--------------------------------------------------------')
    val_Nombre = input('Nombre: ')
    print('--------------------------------------------------------')
    val_DNI = input('DNI: ')
    print('--------------------------------------------------------')
    val_grupo_familiar = input('Cantidad grupo familiar: ')
    print('--------------------------------------------------------')
    val_menores18 = input('Cantidad menores de 18 años: ')
    print('--------------------------------------------------------')
    print('')
    input('Presione ENTER para continuar.\n')
    if tipo_ingreso == 'alta':
        socio_ingresado = socios_controller.Socio(1, val_Nombre, val_Apellido, 
                                    val_DNI, val_grupo_familiar, val_menores18)
    elif tipo_ingreso == 'modif':
        if val_Apellido == '':
            val_Apellido = socio.apellido_socio
        if val_Nombre == '':
            val_Nombre = socio.nombre_socio
        if val_DNI == '':
            val_DNI = socio.DNI_socio
        if val_grupo_familiar == '':
            val_grupo_familiar = socio.cant_grupo_familiar
        if val_menores18 == '':
            val_menores18 = socio.cant_menores18
        socio_ingresado = socios_controller.Socio(socio.id_socio, val_Nombre, 
                    val_Apellido, val_DNI, val_grupo_familiar, val_menores18)
    return socio_ingresado

###############################################################################
### FUNCION OPCION MODIFICAR SOCIO                                          ### 
###############################################################################
def modificar_socio(socio_modificado):
    if socio_modificado.modificar_socio():
        print('### El socio ' + socio_modificado.apellido_socio + ', ' + 
            socio_modificado.nombre_socio +' (Id de Socio: '+ 
            str(socio_modificado.id_socio) + ') fue modificado exitosamente ###')
    else: 
        print('### Error. El socio no pudo ser modificado, por favor, intente nuevamente ###')

###############################################################################
### FUNCION OPCION ELMINAR SOCIO                                            ### 
###############################################################################
def eliminar_socio(socio_baja):
    if socio_baja.eliminar_socio():
        print('#### El socio ' + socio_baja.apellido_socio + ', ' + 
                socio_baja.nombre_socio + ' (Id de Socio: '+ 
                str(socio_baja.id_socio) + ') fue eliminado exitosamente ###')
    else: 
        print('### Error. El socio no pudo ser eliminado, por favor, intente nuevamente ###')

###############################################################################
### FUNCION OPCION ALTA SOCIO                                               ### 
###############################################################################
def guardar_socio(socio_nuevo):
    socio_guardado = socio_nuevo.guardar_socio()
    if socio_guardado:
        print('### El socio ' + socio_guardado.apellido_socio + ', ' + 
                socio_guardado.nombre_socio + ' (Id de Socio: '+ 
                str(socio_guardado.id_socio) + ') fue guardado exitosamente ###')
    else: 
        print('### Error. El socio no pudo ser guardado, por favor, intente nuevamente ###')

###############################################################################
### FUNCION OPCION CALCULAR CUOTA SOCIO                                     ### 
###############################################################################
def calcular_cuota(socio_cuota):
    print('### El socio ' + socio_cuota.apellido_socio + ', ' + 
            socio_cuota.nombre_socio + ' (Id de Socio: '+ 
            str(socio_cuota.id_socio) + ') deberá abonar una cuota de $' + 
            str(socio_cuota.calcular_cuota()), ' ###')


# Ejecutamos la función menu_principal
menu_principal()

# socio_prueba = socios_controller.Socio(1, 'Steve', 'Rogers', '26505640', 3, 2)
# mostrar_socio(socio_prueba)
