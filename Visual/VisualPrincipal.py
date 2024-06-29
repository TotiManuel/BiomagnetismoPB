import tkinter as tk
from tkinter import ttk, messagebox

class VisualPrincipal:
    #region Constructor
    def __init__(self, root, controlador):
        self.root = root
        self.controlador = controlador

        self.root.title("JMM")
        
        #region Menu
        barraMenu = tk.Menu(self.root)
        menuArchivo = tk.Menu(barraMenu, tearoff=0)
        menuTurnero = tk.Menu(barraMenu, tearoff=0)

        menuArchivo.add_command(label="Configurar", command=lambda: self.isSucess(False), background="red")
        menuArchivo.add_separator()
        menuArchivo.add_command(label="Salir", command=lambda: quit())
        barraMenu.add_cascade(label="Archivo", menu = menuArchivo)

        menuTurnero.add_command(label="Buscar Paciente", command=lambda: self.isSucess(False), background="red")
        menuTurnero.add_command(label="Turnero", command=lambda: self.isSucess(False), background="red")
        barraMenu.add_cascade(label="Turnero", menu = menuTurnero)
    
        root.config(menu=barraMenu)
        #endregion

        #region notebook
        notebook = ttk.Notebook(self.root)

        tab1 = ttk.Frame(notebook)
        tab2 = ttk.Frame(notebook)
        tab3 = ttk.Frame(notebook)
        tab4 = ttk.Frame(notebook)
        tab5 = ttk.Frame(notebook)

        notebook.add(tab1, text="Bienvenido")
        notebook.add(tab2, text="Listar")
        notebook.add(tab3, text="Agregar")
        notebook.add(tab4, text="Modificar")
        notebook.add(tab5, text="Eliminar")

        #region Tab1
        self.boton = tk.Button(tab1, text="Salir", command=lambda:self.isSucess(False))
        self.boton.pack()
        #endregion

        #region Tab2
        etiqueta = tk.Label(tab2, text='Selecciona un elemento:').pack()
        opciones = ['Opción 1', 'Opción 2', 'Opción 3', 'Opción 4']
        opcion_seleccionada = tk.StringVar()
        combo = ttk.Combobox(tab2, values=opciones, textvariable=opcion_seleccionada)
        combo.pack()
        combo.bind('<<ComboboxSelected>>', self.listarProducto)

        self.boton = tk.Button(tab2, text="Salir", command=lambda:self.isSucess(False)).pack()
        #endregion

        #region Tab3
        self.boton = tk.Button(tab3, text="Salir", command=lambda:self.isSucess(False))
        self.boton.pack()
        #endregion

        #region Tab4
        self.boton = tk.Button(tab4, text="Salir", command=lambda:self.isSucess(False))
        self.boton.pack()
        #endregion

        #region Tab5
        self.boton = tk.Button(tab5, text="Salir", command=lambda:self.isSucess(False))
        self.boton.pack()
        #endregion

        notebook.pack(expand=True, fill='both')
        #endregion

        #self.label = tk.Label(self.root, text="Valor: 0")
        #self.label.pack()

    #endregion

    #region Mensajes Extras
    def isSucess(self, state):
        messagebox.showinfo("Estado", f"Sucess: {state}")
    #endregion

    #region Producto
    def mostrarMenuProducto(self):
        print("1) Listar Productos")
        print("2) Agregar Productos")
        print("0) Volver")
        return input("Ingresa la opcion >> ")
    
    def listarProducto(self, event):
        seleccion = event.widget.get()
        if seleccion == "Opción 1":
            print(f'Se seleccionó: {seleccion}')
        else:
            quit()
        
    def agregarProductos(self):
        nombre = input("Dime el nombre del producto >> ")
        talla = input("Dime la talla del producto >> ")
        precio = input("Dime el precio del producto >> ")
        return nombre, talla, precio
    #endregion

    #region MenuPrincipal
    def mostrarMenuPrincipal(self):
        print("1) Productos")
        print("0) Salir")
        return input("Elige una opcion >> ")
    #endregion
