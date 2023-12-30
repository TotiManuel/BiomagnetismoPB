import tkinter as tk
from tkinter import messagebox
#import sqlite3
from Funciones.DataBase import agregar_base_de_datos
#from Funciones import quitar_producto
#from Funciones.DataBase import agregar_venta
#from Funciones.DataBase import reembolso
#from Funciones.DataBase import mostrar_grafico
#from Funciones.DataBase import agregar_producto
#from Funciones.DataBase import opciones_base_de_datos
#from Funciones import actualizar_opciones
#from Funciones.DataBase import ver_stock
class RegistroVentas:
    def __init__(self, root):
        self.root = root
        self.root.title("Registro de Ventas")
        self.root.geometry("500x500")

        self.ventas = []
        self.reembolsos = []
        
        # Barra de menú
        menu_bar = tk.Menu(root)
        root.config(menu=menu_bar)

        # Menú "Archivo"
        archivo_menu = tk.Menu(menu_bar, tearoff=0)
        menu_bar.add_cascade(label="Archivo", menu=archivo_menu)
        archivo_menu.add_command(label="Actualizar", command=self.prueba)
        archivo_menu.add_command(label="Salir", command=root.destroy)

        # Menú "Productos"
        productos_menu = tk.Menu(menu_bar, tearoff=0)
        menu_bar.add_cascade(label="Productos", menu=productos_menu)
        productos_menu.add_command(label="Agregar Producto", command=self.prueba)
        productos_menu.add_command(label="Quitar Producto", command=self.prueba)

        # Menú "Ajustes"
        Ajustes_menu = tk.Menu(menu_bar, tearoff=0)
        menu_bar.add_cascade(label="Ajustes", menu=Ajustes_menu)
        Ajustes_menu.add_command(label="Crear Base de Datos", command=self.database)

        # Etiqueta y entrada para el monto de la venta
        self.label_producto = tk.Label(root, text="Bienvenida!! ")
        self.label_producto.grid(row=0, column=0, padx=10, pady=10)

        # Botones para agregar venta y reembolso
        self.boton_agregar_venta = tk.Button(root, text="Agregar Venta", command=self.prueba)
        self.boton_agregar_venta.place(x=10, y=10)

        self.boton_reembolso = tk.Button(root, text="Reembolso", command=self.prueba)
        self.boton_reembolso.place(x=10, y=50)

        # Botón para mostrar el gráfico
        self.boton_mostrar_grafico = tk.Button(root, text="Mostrar Gráfico", command=self.prueba)
        self.boton_mostrar_grafico.place(x=10, y=90)

        # Botón para mostrar el stock
        self.boton_mostrar_grafico = tk.Button(root, text="Ver Stock", command=self.prueba)
        self.boton_mostrar_grafico.place(x=10, y=130)

#    def actualizar(self):
#        actualizar_opciones.actualizar_opciones(self)
    def database(self):
        agregar_base_de_datos.agregar_datebase(self)
    def prueba(self):
        print("Prueba")
if __name__ == "__main__":
    root = tk.Tk()
    app = RegistroVentas(root)
    root.mainloop()
