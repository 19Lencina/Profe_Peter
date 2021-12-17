import sys

try:
    import Tkinter as tk
except ImportError:
    import tkinter as tk

try:
    import ttk
    py3 = False
except ImportError:
    import tkinter.ttk as ttk
    py3 = True

def set_Tk_var():
    global var_ent_Id_Socio
    var_ent_Id_Socio = tk.StringVar()
    global var_ent_Apellido
    var_ent_Apellido = tk.StringVar()
    global var_ent_Nombre
    var_ent_Nombre = tk.StringVar()
    global var_ent_DNI
    var_ent_DNI = tk.StringVar()
    global var_chk_grupo_familiar
    var_chk_grupo_familiar = tk.IntVar()
    global var_sbox_grupo_familiar
    var_sbox_grupo_familiar = tk.StringVar()
    global var_chk_menores18
    var_chk_menores18 = tk.IntVar()
    global var_sbox_menores18
    var_sbox_menores18 = tk.StringVar()



def init(top, gui, *args, **kwargs):
    global w, top_level, root
    w = gui
    top_level = top
    root = top

def destroy_window():
    # Function which closes the window.
    global top_level
    top_level.destroy()
    top_level = None

if __name__ == '__main__':
    import socios_view
    socios_view.vp_start_gui()




