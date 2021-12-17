import sys
import socios_controller
from tkinter import messagebox

try:
    import Tkinter as tk
except ImportError:
    import tkinter as tk
    from tkinter.messagebox import *

try:
    import ttk
    py3 = False
except ImportError:
    import tkinter.ttk as ttk
    py3 = True

import socios_support_view

def vp_start_gui():
    '''Starting point when module is the main routine.'''
    global val, w, root
    root = tk.Tk()
    socios_support_view.set_Tk_var()
    top = win_Socios (root)
    socios_support_view.init(root, top)
    root.mainloop()

w = None
def create_win_Socios(rt, *args, **kwargs):
    '''Starting point when module is imported by another module.
       Correct form of call: 'create_win_Socios(root, *args, **kwargs)' .'''
    global w, w_win, root
    #rt = root
    root = rt
    w = tk.Toplevel (root)
    socios_support_view.set_Tk_var()
    top = win_Socios (w)
    socios_support_view.init(w, top, *args, **kwargs)
    return (w, top)

def destroy_win_Socios():
    global w
    w.destroy()
    w = None

class win_Socios:
    def __init__(self, top=None):
        '''This class configures and populates the toplevel window.
           top is the toplevel containing window.'''
        _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#d9d9d9' # X11 color: 'gray85'
        _ana1color = '#d9d9d9' # X11 color: 'gray85'
        _ana2color = '#ececec' # Closest X11 color: 'gray92'
        self.style = ttk.Style()
        if sys.platform == "win32":
            self.style.theme_use('winnative')
        self.style.configure('.',background=_bgcolor)
        self.style.configure('.',foreground=_fgcolor)
        self.style.configure('.',font="TkDefaultFont")
        self.style.map('.',background=
            [('selected', _compcolor), ('active',_ana2color)])

        top.geometry("377x327+468+103")
        top.minsize(120, 1)
        top.maxsize(1540, 741)
        top.resizable(1,  1)
        top.title("Socios App")
        top.configure(background="#d9d9d9")
        top.configure(highlightbackground="#d9d9d9")
        top.configure(highlightcolor="black")
        
        self.menubar = tk.Menu(top,font="TkMenuFont",bg=_bgcolor,fg=_fgcolor)
        top.configure(menu = self.menubar)

        ### BUTTON NUEVO SOCIO
        self.btn_Nuevo_Socio = ttk.Button(top)
        self.btn_Nuevo_Socio.place(relx=0.69, rely=0.122, height=25, width=86)
        self.btn_Nuevo_Socio.configure(takefocus="")
        self.btn_Nuevo_Socio.configure(text='''Nuevo Socio''')
        self.btn_Nuevo_Socio.configure(command=self.boton_nuevo_socio)

        ### BUTTON BUSCAR SOCIO
        self.btn_Buscar = ttk.Button(top)
        self.btn_Buscar.place(relx=0.69, rely=0.031, height=25, width=86)
        self.btn_Buscar.configure(takefocus="")
        self.btn_Buscar.configure(text='''Buscar''')
        self.btn_Buscar.configure(command=self.boton_buscar_socio)

        ### LABEL ID SOCIO 
        self.lbl_Id_Socio = tk.Label(top)
        self.lbl_Id_Socio.place(relx=0.053, rely=0.092, height=21, width=54)
        self.lbl_Id_Socio.configure(activebackground="#f9f9f9")
        self.lbl_Id_Socio.configure(activeforeground="black")
        self.lbl_Id_Socio.configure(background="#d9d9d9")
        self.lbl_Id_Socio.configure(disabledforeground="#a3a3a3")
        self.lbl_Id_Socio.configure(foreground="#000000")
        self.lbl_Id_Socio.configure(highlightbackground="#d9d9d9")
        self.lbl_Id_Socio.configure(highlightcolor="black")
        self.lbl_Id_Socio.configure(text='''Socio #:''')

        ### ENTRY ID SOCIO
        self.ent_Id_Socio = ttk.Entry(top)
        self.ent_Id_Socio.place(relx=0.239, rely=0.092, relheight=0.064
                , relwidth=0.414)
        self.ent_Id_Socio.configure(takefocus="")
        self.ent_Id_Socio.configure(cursor="ibeam")
        self.ent_Id_Socio.configure(textvariable=socios_support_view.var_ent_Id_Socio)

        ### LABEL APELLIDO
        self.lbl_Apellido = tk.Label(top)
        self.lbl_Apellido.place(relx=0.053, rely=0.245, height=21, width=64)
        self.lbl_Apellido.configure(activebackground="#f9f9f9")
        self.lbl_Apellido.configure(activeforeground="black")
        self.lbl_Apellido.configure(anchor='w')
        self.lbl_Apellido.configure(background="#d9d9d9")
        self.lbl_Apellido.configure(disabledforeground="#a3a3a3")
        self.lbl_Apellido.configure(foreground="#000000")
        self.lbl_Apellido.configure(highlightbackground="#d9d9d9")
        self.lbl_Apellido.configure(highlightcolor="black")
        self.lbl_Apellido.configure(state='disabled')
        self.lbl_Apellido.configure(text='''Apellido/s:''')
        
        # ENTRY APELLIDO
        self.ent_Apellido = tk.Entry(top)
        self.ent_Apellido.place(relx=0.239, rely=0.245, height=20
                , relwidth=0.674)
        self.ent_Apellido.configure(background="white")
        self.ent_Apellido.configure(disabledforeground="#a3a3a3")
        self.ent_Apellido.configure(font="TkFixedFont")
        self.ent_Apellido.configure(foreground="#000000")
        self.ent_Apellido.configure(highlightbackground="#d9d9d9")
        self.ent_Apellido.configure(highlightcolor="black")
        self.ent_Apellido.configure(insertbackground="black")
        self.ent_Apellido.configure(selectbackground="blue")
        self.ent_Apellido.configure(selectforeground="white")
        self.ent_Apellido.configure(state='disabled')
        self.ent_Apellido.configure(textvariable=socios_support_view.var_ent_Apellido)

        ### LABEL NOMBRE
        self.lbl_Nombre = tk.Label(top)
        self.lbl_Nombre.place(relx=0.053, rely=0.336, height=21, width=64)
        self.lbl_Nombre.configure(activebackground="#f9f9f9")
        self.lbl_Nombre.configure(activeforeground="black")
        self.lbl_Nombre.configure(anchor='w')
        self.lbl_Nombre.configure(background="#d9d9d9")
        self.lbl_Nombre.configure(disabledforeground="#a3a3a3")
        self.lbl_Nombre.configure(foreground="#000000")
        self.lbl_Nombre.configure(highlightbackground="#d9d9d9")
        self.lbl_Nombre.configure(highlightcolor="black")
        self.lbl_Nombre.configure(state='disabled')
        self.lbl_Nombre.configure(text='''Nombre/s:''')

        ### ENTRY NOMBRE
        self.ent_Nombre = tk.Entry(top)
        self.ent_Nombre.place(relx=0.239, rely=0.336, height=20, relwidth=0.674)
        self.ent_Nombre.configure(background="white")
        self.ent_Nombre.configure(disabledforeground="#a3a3a3")
        self.ent_Nombre.configure(font="TkFixedFont")
        self.ent_Nombre.configure(foreground="#000000")
        self.ent_Nombre.configure(highlightbackground="#d9d9d9")
        self.ent_Nombre.configure(highlightcolor="black")
        self.ent_Nombre.configure(insertbackground="black")
        self.ent_Nombre.configure(selectbackground="blue")
        self.ent_Nombre.configure(selectforeground="white")
        self.ent_Nombre.configure(state='disabled')
        self.ent_Nombre.configure(textvariable=socios_support_view.var_ent_Nombre)

        ### LABEL DNI
        self.lbl_DNI = tk.Label(top)
        self.lbl_DNI.place(relx=0.053, rely=0.428, height=21, width=54)
        self.lbl_DNI.configure(activebackground="#f9f9f9")
        self.lbl_DNI.configure(activeforeground="black")
        self.lbl_DNI.configure(anchor='w')
        self.lbl_DNI.configure(background="#d9d9d9")
        self.lbl_DNI.configure(disabledforeground="#a3a3a3")
        self.lbl_DNI.configure(foreground="#000000")
        self.lbl_DNI.configure(highlightbackground="#d9d9d9")
        self.lbl_DNI.configure(highlightcolor="black")
        self.lbl_DNI.configure(state='disabled')
        self.lbl_DNI.configure(text='''DNI #:''')

        ### ENTRY DNI
        self.ent_DNI = tk.Entry(top)
        self.ent_DNI.place(relx=0.239, rely=0.428, height=20, relwidth=0.674)
        self.ent_DNI.configure(background="white")
        self.ent_DNI.configure(disabledforeground="#a3a3a3")
        self.ent_DNI.configure(font="TkFixedFont")
        self.ent_DNI.configure(foreground="#000000")
        self.ent_DNI.configure(highlightbackground="#d9d9d9")
        self.ent_DNI.configure(highlightcolor="black")
        self.ent_DNI.configure(insertbackground="black")
        self.ent_DNI.configure(selectbackground="blue")
        self.ent_DNI.configure(selectforeground="white")
        self.ent_DNI.configure(state='disabled')
        self.ent_DNI.configure(textvariable=socios_support_view.var_ent_DNI)
        
        ### SEPARADOR
        self.TSeparator1 = ttk.Separator(top)
        self.TSeparator1.place(relx=0.027, rely=0.52,  relwidth=0.928)
 
        ### CHECK BUTTON GRUPO FAMILIAR
        self.chk_Grupo_Familiar = ttk.Checkbutton(top)
        self.chk_Grupo_Familiar.place(relx=0.053, rely=0.55, relwidth=0.345
                , relheight=0.0, height=21)
        self.chk_Grupo_Familiar.configure(variable=socios_support_view.var_chk_grupo_familiar)
        self.chk_Grupo_Familiar.configure(takefocus="")
        self.chk_Grupo_Familiar.configure(text='''Grupo Familiar''')
        self.chk_Grupo_Familiar.configure(state='disabled')
        self.chk_Grupo_Familiar.configure(command=self.check_grupo_familiar)

        ### LABEL GRUPO FAMILIAR
        self.lbl_cant_grupo_familiar = tk.Label(top)
        self.lbl_cant_grupo_familiar.place(relx=0.106, rely=0.612, height=21
                , width=157)
        self.lbl_cant_grupo_familiar.configure(background="#d9d9d9")
        self.lbl_cant_grupo_familiar.configure(disabledforeground="#a3a3a3")
        self.lbl_cant_grupo_familiar.configure(foreground="#000000")
        self.lbl_cant_grupo_familiar.configure(state='disabled')
        self.lbl_cant_grupo_familiar.configure(text='''Cant. miembros gr. familiar:''')

        ### SPINBOX CANTIDAD GRUPO FAMILIAR
        self.sbox_cant_grupo_familar = tk.Spinbox(top, from_=1.0, to=99.0)
        self.sbox_cant_grupo_familar.place(relx=0.531, rely=0.612
                , relheight=0.058, relwidth=0.093)
        self.sbox_cant_grupo_familar.configure(activebackground="#f9f9f9")
        self.sbox_cant_grupo_familar.configure(background="white")
        self.sbox_cant_grupo_familar.configure(buttonbackground="#d9d9d9")
        self.sbox_cant_grupo_familar.configure(disabledforeground="#a3a3a3")
        self.sbox_cant_grupo_familar.configure(font="TkDefaultFont")
        self.sbox_cant_grupo_familar.configure(foreground="black")
        self.sbox_cant_grupo_familar.configure(highlightbackground="black")
        self.sbox_cant_grupo_familar.configure(highlightcolor="black")
        self.sbox_cant_grupo_familar.configure(insertbackground="black")
        self.sbox_cant_grupo_familar.configure(justify='right')
        self.sbox_cant_grupo_familar.configure(selectbackground="blue")
        self.sbox_cant_grupo_familar.configure(selectforeground="white")
        self.sbox_cant_grupo_familar.configure(state='disabled')
        self.sbox_cant_grupo_familar.configure(textvariable=socios_support_view.var_sbox_grupo_familiar)

        ### CHECK BUTTON MENORES 18
        self.chk_menores = ttk.Checkbutton(top)
        self.chk_menores.place(relx=0.053, rely=0.703, relwidth=0.424
                , relheight=0.0, height=21)
        self.chk_menores.configure(variable=socios_support_view.var_chk_menores18)
        self.chk_menores.configure(takefocus="")
        self.chk_menores.configure(text='''Menores 18 años''')
        self.chk_menores.configure(state='disabled')
        self.chk_menores.configure(command=self.check_menores18)

        ### LABEL CANTIDAD MENORES
        self.lbl_cant_menores18 = tk.Label(top)
        self.lbl_cant_menores18.place(relx=0.106, rely=0.765, height=21
                , width=132)
        self.lbl_cant_menores18.configure(background="#d9d9d9")
        self.lbl_cant_menores18.configure(disabledforeground="#a3a3a3")
        self.lbl_cant_menores18.configure(foreground="#000000")
        self.lbl_cant_menores18.configure(state='disabled')
        self.lbl_cant_menores18.configure(text='''Cant. menores 18 años:''')

        ### SPINBOX CANTIDAD MENORES 18
        self.sbox_cant_menores18 = tk.Spinbox(top, from_=1.0, to=99.0)
        self.sbox_cant_menores18.place(relx=0.531, rely=0.765, relheight=0.058
                , relwidth=0.093)
        self.sbox_cant_menores18.configure(activebackground="#f9f9f9")
        self.sbox_cant_menores18.configure(background="white")
        self.sbox_cant_menores18.configure(buttonbackground="#d9d9d9")
        self.sbox_cant_menores18.configure(disabledforeground="#a3a3a3")
        self.sbox_cant_menores18.configure(font="TkDefaultFont")
        self.sbox_cant_menores18.configure(foreground="black")
        self.sbox_cant_menores18.configure(highlightbackground="black")
        self.sbox_cant_menores18.configure(highlightcolor="black")
        self.sbox_cant_menores18.configure(insertbackground="black")
        self.sbox_cant_menores18.configure(justify='right')
        self.sbox_cant_menores18.configure(selectbackground="blue")
        self.sbox_cant_menores18.configure(selectforeground="white")
        self.sbox_cant_menores18.configure(state='disabled')
        self.sbox_cant_menores18.configure(textvariable=socios_support_view.var_sbox_menores18)
        
        ### SEPARADOR
        self.TSeparator2 = ttk.Separator(top)
        self.TSeparator2.place(relx=0.027, rely=0.856,  relwidth=0.928)

        ### BUTTON ALTA SOCIO
        self.btn_Alta = ttk.Button(top)
        self.btn_Alta.place(relx=0.027, rely=0.887, height=25, width=86)
        self.btn_Alta.configure(takefocus="")
        self.btn_Alta.configure(text='''Guardar Socio''')
        self.btn_Alta.configure(state='disabled')
        self.btn_Alta.configure(command=self.boton_guardar_socio)

        ### BUTTON BAJA SOCIO
        self.btn_Baja = ttk.Button(top)
        self.btn_Baja.place(relx=0.265, rely=0.887, height=25, width=66)
        self.btn_Baja.configure(takefocus="")
        self.btn_Baja.configure(text='''Baja Socio''')
        self.btn_Baja.configure(state='disabled')
        self.btn_Baja.configure(command=self.boton_baja_socio)

        ### BUTTON MODIFICAR SOCIO
        self.btn_Modificar = ttk.Button(top)
        self.btn_Modificar.place(relx=0.451, rely=0.887, height=25, width=106)
        self.btn_Modificar.configure(takefocus="")
        self.btn_Modificar.configure(text='''Modificar Socio''')
        self.btn_Modificar.configure(state='disabled')
        self.btn_Modificar.configure(command=self.boton_modificar_socio)

        ### BUTTON CALCULAR CUOTA
        self.btn_Calcular_Cuota = ttk.Button(top)
        self.btn_Calcular_Cuota.place(relx=0.743, rely=0.887, height=25
                , width=88)
        self.btn_Calcular_Cuota.configure(takefocus="")
        self.btn_Calcular_Cuota.configure(text='''Calcular Cuota''')
        self.btn_Calcular_Cuota.configure(state='disabled')
        self.btn_Calcular_Cuota.configure(command=self.boton_calcular_cuota)

    ###################################################
    ##### FUNCIONES ASOCIADAS A CADA CHECK BUTTON #####
    ###################################################

    def check_grupo_familiar(self):
        check_state_grupo_familiar = socios_support_view.var_chk_grupo_familiar.get()
        if check_state_grupo_familiar==1:
            self.lbl_cant_grupo_familiar.configure(state='normal')
            self.sbox_cant_grupo_familar.configure(state='normal')
            socios_support_view.var_sbox_grupo_familiar.set('2')
            self.chk_menores.configure(state='normal')
            socios_support_view.var_chk_menores18.set(0)
        elif check_state_grupo_familiar==0:
            self.lbl_cant_grupo_familiar.configure(state='disabled')
            self.sbox_cant_grupo_familar.configure(state='disabled')
            socios_support_view.var_sbox_grupo_familiar.set('1')
            self.chk_menores.configure(state='disabled')
            socios_support_view.var_chk_menores18.set(0)
            self.lbl_cant_menores18.configure(state='disabled')
            self.sbox_cant_menores18.configure(state='disabled')
            socios_support_view.var_sbox_menores18.set('0')

    def check_menores18(self):
        check_state_menores18 = socios_support_view.var_chk_menores18.get()
        if check_state_menores18 == 1:
            self.lbl_cant_menores18.configure(state='normal')
            self.sbox_cant_menores18.configure(state='normal')
            socios_support_view.var_sbox_menores18.set('1')
        elif check_state_menores18 == 0:
            self.lbl_cant_menores18.configure(state='disabled')
            self.sbox_cant_menores18.configure(state='disabled')
            socios_support_view.var_sbox_menores18.set('0')            

    #############################################
    ##### FUNCIONES ASOCIADAS A CADA BUTTON #####
    #############################################

    def boton_buscar_socio(self):
        socio_a_buscar = self.leer_datos()
        socio_buscado = socio_a_buscar.obtener_socio_x_Id()
        if socio_buscado: # si socio_buscado no está vacio será TRUE
            socios_support_view.var_ent_Id_Socio.set(socio_buscado.id_socio)
            socios_support_view.var_ent_Apellido.set(socio_buscado.apellido_socio)
            socios_support_view.var_ent_Nombre.set(socio_buscado.nombre_socio)
            socios_support_view.var_ent_DNI.set(socio_buscado.DNI_socio)
            if socio_buscado.cant_grupo_familiar!=0:
                socios_support_view.var_chk_grupo_familiar.set(1)
                socios_support_view.var_sbox_grupo_familiar.set(socio_buscado.cant_grupo_familiar)
                self.sbox_cant_grupo_familar.configure(state='normal')
                self.lbl_cant_grupo_familiar.configure(state='normal')
                self.chk_menores.configure(state='normal')
            else:
                socios_support_view.var_chk_grupo_familiar.set(0)
                socios_support_view.var_sbox_grupo_familiar.set(socio_buscado.cant_grupo_familiar)                
                self.sbox_cant_grupo_familar.configure(state='disabled')
                self.lbl_cant_grupo_familiar.configure(state='disabled')
                self.chk_menores.configure(state='disabled')
            if socio_buscado.cant_menores18!=0:
                    socios_support_view.var_chk_menores18.set(1)
                    socios_support_view.var_sbox_menores18.set(socio_buscado.cant_menores18)
                    self.sbox_cant_menores18.configure(state='normal')
                    self.lbl_cant_menores18.configure(state='normal')
            else:
                socios_support_view.var_chk_menores18.set(0)
                socios_support_view.var_sbox_menores18.set(socio_buscado.cant_menores18)
                self.sbox_cant_menores18.configure(state='disabled')
                self.lbl_cant_menores18.configure(state='disabled')                            

            ### código para setear formulario ###
            self.btn_Nuevo_Socio.configure(state='normal')
            self.btn_Buscar.configure(state='normal')
            self.lbl_Id_Socio.configure(state='normal')
            self.ent_Id_Socio.configure(state='normal')
            self.lbl_Apellido.configure(state='normal')
            self.ent_Apellido.configure(state='normal')
            self.lbl_Nombre.configure(state='normal')
            self.ent_Nombre.configure(state='normal')
            self.lbl_DNI.configure(state='normal')
            self.ent_DNI.configure(state='normal')
            self.chk_Grupo_Familiar.configure(state='normal')
            self.btn_Alta.configure(state='disabled')
            self.btn_Baja.configure(state='normal')
            self.btn_Modificar.configure(state='normal')
            self.btn_Calcular_Cuota.configure(state='normal')
        else: # si socio_buscado está vacio NO SERA TRUE (sera FALSE)
            self.win_warning('Búsqueda sin resultados', 'Id de Socio: '+ str(socio_a_buscar.id_socio) + ' no existe')
            self.inicializar_forumulario()

    def boton_nuevo_socio(self):
        self.inicializar_forumulario()
        ### código para setear formulario ###
        self.btn_Nuevo_Socio.configure(state='normal')
        self.btn_Buscar.configure(state='normal')
        self.lbl_Id_Socio.configure(state='normal')
        self.ent_Id_Socio.configure(state='normal')
        self.lbl_Apellido.configure(state='normal')
        self.ent_Apellido.configure(state='normal')
        self.lbl_Nombre.configure(state='normal')
        self.ent_Nombre.configure(state='normal')
        self.lbl_DNI.configure(state='normal')
        self.ent_DNI.configure(state='normal')
        self.chk_Grupo_Familiar.configure(state='normal')
        self.btn_Alta.configure(state='normal')
        self.btn_Baja.configure(state='disabled')
        self.btn_Modificar.configure(state='disabled')
        self.btn_Calcular_Cuota.configure(state='normal')

    def boton_guardar_socio(self):
        socio_nuevo = self.leer_datos()
        socio_guardado = socio_nuevo.guardar_socio()
        if socio_guardado:
            self.win_warning('Socio guardado', 'El socio ' + socio_guardado.apellido_socio + ', ' + socio_guardado.nombre_socio +
                             ' (Id de Socio: '+ str(socio_guardado.id_socio) + ') fue guardado exitosamente.')
        else: 
            self.win_warning('Error', 'El socio no pudo ser guardado, por favor, intente nuevamente')
        self.inicializar_forumulario()

    def boton_baja_socio(self):
        socio_baja = self.leer_datos()
        if socio_baja.eliminar_socio():
            self.win_warning('Socio eliminado', 'El socio ' + socio_baja.apellido_socio + ', ' + socio_baja.nombre_socio +
                             ' (Id de Socio: '+ str(socio_baja.id_socio) + ') fue eliminado exitosamente.')
        else: 
            self.win_warning('Error', 'El socio no pudo ser eliminado, por favor, intente nuevamente')          
        self.inicializar_forumulario()

    def boton_modificar_socio(self):
        socio_modificado = self.leer_datos()     
        if socio_modificado.modificar_socio():
            self.win_warning('Socio modificado', 'El socio ' + socio_modificado.apellido_socio + ', ' + socio_modificado.nombre_socio +
                             ' (Id de Socio: '+ str(socio_modificado.id_socio) + ') fue modificado exitosamente.')
        else: 
            self.win_warning('Error', 'El socio no pudo ser modificado, por favor, intente nuevamente')  
        self.inicializar_forumulario()

    def boton_calcular_cuota(self):
        socio_cuota = self.leer_datos()
        self.win_warning('Valor Cuota', 'El socio ' + socio_cuota.apellido_socio + ', ' + socio_cuota.nombre_socio +
                    ' (Id de Socio: '+ str(socio_cuota.id_socio) + ') deberá abonar una cuota de $' + 
                    str(socio_cuota.calcular_cuota()))
        self.inicializar_forumulario()

    ################################
    ##### FUNCIONES FORMULARIO #####
    ################################
    
    def inicializar_forumulario(self):
        self.btn_Nuevo_Socio.configure(state='normal')
        self.btn_Buscar.configure(state='normal')
        self.lbl_Id_Socio.configure(state='normal')
        self.ent_Id_Socio.configure(state='normal')
        self.lbl_Apellido.configure(state='disabled')
        self.ent_Apellido.configure(state='disabled')
        self.lbl_Nombre.configure(state='disabled')
        self.ent_Nombre.configure(state='disabled')
        self.lbl_DNI.configure(state='disabled')
        self.ent_DNI.configure(state='disabled')
        self.chk_Grupo_Familiar.configure(state='disabled')
        self.lbl_cant_grupo_familiar.configure(state='disabled')
        self.sbox_cant_grupo_familar.configure(state='disabled')
        self.chk_menores.configure(state='disabled')
        self.lbl_cant_menores18.configure(state='disabled')
        self.sbox_cant_menores18.configure(state='disabled')
        self.btn_Alta.configure(state='disabled')
        self.btn_Baja.configure(state='disabled')
        self.btn_Modificar.configure(state='disabled')
        self.btn_Calcular_Cuota.configure(state='disabled')
        socios_support_view.var_ent_Id_Socio.set('')
        socios_support_view.var_ent_Apellido.set('')
        socios_support_view.var_ent_Nombre.set('')
        socios_support_view.var_ent_DNI.set('')
        socios_support_view.var_sbox_grupo_familiar.set('')
        socios_support_view.var_sbox_menores18.set('')
        socios_support_view.var_chk_grupo_familiar.set(0)
        socios_support_view.var_chk_menores18.set(0)
    

    def leer_datos(self):
        if socios_support_view.var_ent_Id_Socio.get()=='':
            val_Id_Socio = 1
        else: 
            val_Id_Socio = socios_support_view.var_ent_Id_Socio.get()
        val_Apellido = socios_support_view.var_ent_Apellido.get()
        val_Nombre = socios_support_view.var_ent_Nombre.get()
        val_DNI = socios_support_view.var_ent_DNI.get()       
        # val_Cuota =  0 # ALE
        if socios_support_view.var_sbox_grupo_familiar.get()=='':
            val_grupo_familiar = 1
        else: 
            val_grupo_familiar = socios_support_view.var_sbox_grupo_familiar.get()
        if socios_support_view.var_sbox_menores18.get()=='':
            val_menores18 = 0
        else:
            val_menores18 = socios_support_view.var_sbox_menores18.get()
        socio = socios_controller.Socio(val_Id_Socio, val_Nombre, val_Apellido, 
                    val_DNI, val_grupo_familiar, val_menores18) #, val_Cuota)#Peter: agregado val_Cuota
        return socio

    ####################################
    ##### CODIGO VENTANAS MENSAJES #####
    ####################################
    
    def win_warning(self, text_title, text_message):
        messagebox.showinfo(text_title, text_message)
    

if __name__ == '__main__':
    vp_start_gui()





