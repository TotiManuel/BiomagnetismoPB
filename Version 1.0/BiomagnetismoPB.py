import tkinter as tk
from Funciones.DataBase import agregar_base_de_datos
from Funciones.DataBase import agregar_producto
from Funciones import quitar_producto
from Funciones.DataBase import agregar_venta
from Funciones.DataBase import reembolso
from Funciones.DataBase import mostrar_grafico
from Funciones.DataBase import agregar_producto_existente
from Funciones import actualizar_opciones
from Funciones.DataBase import ver_stock


class RegistroVentas:
    def __init__(self, root):
        self.root = root
        self.root.title("Registro de Ventas")
        self.root.geometry("500x500+0+0")

        self.ventas = []
        self.reembolsos = []
#region menu
        # Barra de menú
        menu_bar = tk.Menu(root)
        root.config(menu=menu_bar)

        # Menú "Archivo"
        archivo_menu = tk.Menu(menu_bar, tearoff=0)
        menu_bar.add_cascade(label="Archivo", menu=archivo_menu)
        archivo_menu.add_command(label="Actualizar", command=self.actualizar)
        archivo_menu.add_command(label="Salir", command=root.destroy)

        # Menú "Ajustes"
        Ajustes_menu = tk.Menu(menu_bar, tearoff=0)
        menu_bar.add_cascade(label="Ajustes", menu=Ajustes_menu)
        Ajustes_menu.add_command(label="Crear Base de Datos", command=self.database)

        # Etiqueta y entrada para el monto de la venta
        self.label_producto = tk.Label(root, text="BIENVENIDA!! ")
        self.label_producto.place(relx=0.01, rely=0.01, relwidth = 0.3)

        # Botones para agregar venta y reembolso
        self.boton_agregar_venta = tk.Button(root, text="Agregar Venta", command=self.Agregar_Venta)
        self.boton_agregar_venta.place(relx=0.01, rely=0.07, relwidth = 0.3)

        self.boton_reembolso = tk.Button(root, text="Reembolso", command=self.Reembolso)
        self.boton_reembolso.place(relx=0.01, rely=0.15, relwidth = 0.3)

        # Botón para mostrar el gráfico
        self.boton_mostrar_grafico = tk.Button(root, text="Mostrar Gráfico", command=self.grafico)
        self.boton_mostrar_grafico.place(relx=0.01, rely=0.23, relwidth = 0.3)

        # Botón para mostrar el stock
        self.boton_mostrar_grafico = tk.Button(root, text="Ver Stock", command=self.VerStock)
        self.boton_mostrar_grafico.place(relx=0.01, rely=0.31, relwidth = 0.3)
        
        # Botón para Agregar Producto
        self.boton_agregar_producto = tk.Button(root, text="Agregar Producto", command=self.agregar_producto)
        self.boton_agregar_producto.place(relx=0.01, rely=0.39, relwidth = 0.3)
        
        # Botón para Agregar Producto Existente
        self.boton_quitar_producto = tk.Button(root, text="Agregar Stock", command=self.agregar_producto_existe)
        self.boton_quitar_producto.place(relx=0.01, rely=0.47, relwidth = 0.3)
        
        # Botón para Quitar Producto
        self.boton_quitar_producto = tk.Button(root, text="Quitar Producto", command=self.quitar_producto)
        self.boton_quitar_producto.place(relx=0.01, rely=0.55, relwidth = 0.3)
        
        # Botón para Turnero
        self.boton_turnero = tk.Button(root, text="Turnero", command=self.prueba)
        self.boton_turnero.place(relx=0.40, rely=0.07, relwidth = 0.3)
        
        # Botón para Listado de turnos
        self.boton_listado_turnos = tk.Button(root, text="Listado de Turnos", command=self.prueba)
        self.boton_listado_turnos.place(relx=0.40, rely=0.15, relwidth = 0.3)
        
        # Botón para Listado de Pacientes
        self.boton_listado_pacientes = tk.Button(root, text="Listado de Pacientes", command=self.prueba)
        self.boton_listado_pacientes.place(relx=0.40, rely=0.23, relwidth = 0.3)
        
#endregion
#region BaseDeDatos
    def grafico(self):
        mostrar_grafico.graficar(self)
    def actualizar(self):
        actualizar_opciones.obtener_opciones_base_datos()
    def Reembolso(self):
        reembolso.reembolso(self)
    def VerStock(self):
        ver_stock.lista(self)
    def Agregar_Venta(self):
        agregar_venta.agregar_venta(self)
    def quitar_producto(self):
        quitar_producto.quitar(self)
    def agregar_producto(self):
        agregar_producto.agregar_producto(self)
    def agregar_producto_existe(self):
    	agregar_producto_existente.agregar_producto_funcion_Existe()
    def database(self):
        agregar_base_de_datos.agregar_database()
    def prueba(self):
        print("Prueba")
#endregion
#region Principal
if __name__ == "__main__":
    root = tk.Tk()
    app = RegistroVentas(root)
    root.mainloop()
#endregion
