try:
    from tkinter import Tk, Frame, Label, Entry, Button, Menu, Checkbutton, Toplevel
    from lib.PGcore import Core
except:
    from lib.depend import installDepend
    installDepend()
    from tkinter import Tk, Frame, Label, Entry, Button, Menu, Checkbutton, Toplevel
    from lib.PGcore import Core
PyInstaller_GUI = "PyInstaller_GUI v2.0"
# ------------------------------------------------------CORE_INTERFACE---------------------------------------------
root = Tk()
try:
    # Puede fallar si se ejecuta en linux
    root.iconbitmap('lib/icon.ico')
except:
    pass
barra_menu = Menu(root)
root.config(menu=barra_menu)
root.title(PyInstaller_GUI)
root.resizable(0, 0)
frame = Frame(root)
frame.grid(row=0, column=0)

root2 = None

# ------------------------------------------------------CORE_PROGRAM-----------------------------------------------

core = Core()


def opciones(op):
    def start():
        global root2
        root2 = Toplevel()
        try:
            # Puede fallar si se ejecuta en linux
            root2.iconbitmap('lib/icon.ico')
        except:
            pass
        root2.title(PyInstaller_GUI + " - Archivo de version")
        root2.resizable(0, 0)

        label1 = Label(root2, text="CompanyName:")
        entry1 = Entry(root2, width=66, textvariable=core.CompanyName)
        label2 = Label(root2, text="FileDescription:")
        entry2 = Entry(root2, width=66, textvariable=core.FileDescription)
        label3 = Label(root2, text="FileVersion:")
        entry3 = Entry(root2, width=66, textvariable=core.FileVersion)
        label4 = Label(root2, text="InternalName:")
        entry4 = Entry(root2, width=66, textvariable=core.InternalName)
        label5 = Label(root2, text="LegalCopyright:")
        entry5 = Entry(root2, width=66, textvariable=core.LegalCopyright)
        label6 = Label(root2, text="OriginalFilename:")
        entry6 = Entry(root2, width=66, textvariable=core.OriginalFilename)
        label7 = Label(root2, text="ProductName:")
        entry7 = Entry(root2, width=66, textvariable=core.ProductName)
        label8 = Label(root2, text="ProductVersion:")
        entry8 = Entry(root2, width=66, textvariable=core.ProductVersion)
        Button(root2, text="Guardar/Usar", command=lambda: opciones(3)).grid(row=8, column=0, columnspan=2)
        Button(root2, text="Cancelar", command=lambda: opciones(2)).grid(row=8, column=2, columnspan=2)

        label1.grid(row=0, column=0, pady=2.5)
        entry1.grid(row=0, column=1, pady=2.5, columnspan=5)
        label2.grid(row=1, column=0, pady=2.5)
        entry2.grid(row=1, column=1, pady=2.5, columnspan=5)
        label3.grid(row=2, column=0, pady=2.5)
        entry3.grid(row=2, column=1, pady=2.5, columnspan=5)
        label4.grid(row=3, column=0, pady=2.5)
        entry4.grid(row=3, column=1, pady=2.5, columnspan=5)
        label5.grid(row=4, column=0, pady=2.5)
        entry5.grid(row=4, column=1, pady=2.5, columnspan=5)
        label6.grid(row=5, column=0, pady=2.5)
        entry6.grid(row=5, column=1, pady=2.5, columnspan=5)
        label7.grid(row=6, column=0, pady=2.5)
        entry7.grid(row=6, column=1, pady=2.5, columnspan=5)
        label8.grid(row=7, column=0, pady=2.5)
        entry8.grid(row=7, column=1, pady=2.5, columnspan=5)

        root2.mainloop()

    if op == 1:
        # Abrir y cerrar ventana, 'Archivo de version'
        if core.var_file_version.get():
            core.var_status_file_version.set("?")
            start()
        else:
            if root2:
                root2.destroy()
    elif op == 2:
        # Cancelar
        root2.destroy()

    elif op == 3:
        # Guardar
        core.crear_file_version()

    elif op == 4:
        # Español
        a = core.cambiarIdioma(1)
        if a:
            root.destroy()

    elif op == 5:
        # Ingles
        a = core.cambiarIdioma(2)
        if a:
            root.destroy()


def Icon():
    if core.icon.get():
        icono_boton.grid(row=2, column=0)
        icono_entrada.grid(row=2, column=1, columnspan=8, ipadx=250)
    else:
        icono_boton.grid_remove()
        icono_entrada.grid_remove()


# --------------------------------------------------------INTERFACE------------------------------------------------
file_menu = Menu(barra_menu, tearoff=0)
barra_menu.add_cascade(label=core.words[0], menu=file_menu)
file_menu.add_command(label=core.words[1], command=core.Abrir_archivo_py)
file_menu.add_command(label="Ejecutar .spec", command=core.abrir_archivo_spec)
file_menu.add_command(label=core.words[2], command=lambda: root.destroy())

idioma_menu = Menu(barra_menu, tearoff=0)
barra_menu.add_cascade(label=core.words[9], menu=idioma_menu)
idioma_menu.add_command(label="Spanish", command=lambda: opciones(4))
idioma_menu.add_command(label="English", command=lambda: opciones(5))

# --------------------------------------------------------------------------------------------


Label(frame, text=core.words[3]).grid(row=0, column=0, pady=2.5, padx=2.5)

Entry(frame, textvariable=core.file_py).grid(row=0, column=1, columnspan=8, pady=2.5, padx=2.5, ipadx=250)

Checkbutton(frame, text=core.words[6], variable=core.icon, command=Icon).grid(row=1, column=0)

Checkbutton(frame, text=core.words[5], variable=core.onefile).grid(row=1, column=1)

Checkbutton(frame, text=core.words[4], variable=core.windowed).grid(row=1, column=3)

Label(frame, text="key:", anchor="e").grid(row=1, column=4, pady=2.5)

Entry(frame, textvariable=core.key).grid(row=1, column=5, pady=2.5)

Checkbutton(frame, text="Administrador", variable=core.admin).grid(row=1, column=6)

Checkbutton(frame, text="Limpiar cache", variable=core.clean).grid(row=1, column=7)

icono_boton = Button(frame, text=core.words[8], command=core.Abrir_icono)
icono_entrada = Entry(frame, textvariable=core.file_ico)

Label(frame, text="Directorios de origen ( Archivos o carpetas) para incluir en el exe.").grid(row=4, column=1,
                                                                                               columnspan=5, pady=5)

Entry(frame, width=66, textvariable=core.entry1_a).grid(row=5, column=1, columnspan=5)
Entry(frame, width=66, textvariable=core.entry2_a).grid(row=6, column=1, columnspan=5)
Entry(frame, width=66, textvariable=core.entry3_a).grid(row=7, column=1, columnspan=5)
Entry(frame, width=66, textvariable=core.entry4_a).grid(row=8, column=1, columnspan=5)
Entry(frame, width=66, textvariable=core.entry5_a).grid(row=9, column=1, columnspan=5)
Entry(frame, width=66, textvariable=core.entry6_a).grid(row=10, column=1, columnspan=5)

Label(frame, text="Directorios de destino:").grid(row=4, column=6)
Entry(frame, textvariable=core.entry1_b).grid(row=5, column=6, padx=5)
Entry(frame, textvariable=core.entry2_b).grid(row=6, column=6, padx=5)
Entry(frame, textvariable=core.entry3_b).grid(row=7, column=6, padx=5)
Entry(frame, textvariable=core.entry4_b).grid(row=8, column=6, padx=5)
Entry(frame, textvariable=core.entry5_b).grid(row=9, column=6, padx=5)
Entry(frame, textvariable=core.entry6_b).grid(row=10, column=6, padx=5)

Button(frame, text="Agregar archivos", command=core.agregar_archivos).grid(row=5, column=0, rowspan=3)
Label(frame, text="o").grid(row=6, column=0, rowspan=4)
Button(frame, text="Agregar carpeta", command=core.agregar_carpeta).grid(row=8, column=0, rowspan=3)

Checkbutton(frame, text="Archivo de version", variable=core.var_file_version, command=lambda: opciones(1)).grid(row=5,
                                                                                                                column=7)
Label(frame, textvariable=core.var_status_file_version).grid(row=6, column=7)

Button(frame, text=core.words[7], command=core.build, font=12, bd=5).grid(row=9, column=7, padx=10, rowspan=2)

Icon()
root.mainloop()
