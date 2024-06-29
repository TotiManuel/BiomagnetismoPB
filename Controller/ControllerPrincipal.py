#region Importaciones
import os
from Visual.VisualPrincipal import VisualPrincipal
from Modelos.Producto import Producto

import tkinter as tk
#endregion

class ControllerPrincipal:
    #region Constructor
    def __init__(self):
        self.app = tk.Tk()
        self.vista = VisualPrincipal(self.app, self)
        self.app.mainloop()
        self.listas_productos = []
    #endregion

    #region Funciones Extras
    def limpiar_Consola(self):
        try:
            os.system("clear")
        except:
            os.system("cls")

    def ultimo_Codigo(self, lista):
        try:
            for i in lista:
                ultimo_codigo = i.codigo
            return int(ultimo_codigo) + 1
        except:
            return 0
    #endregion

    #region Carga
    def cargar_Datos(self):
        with open('Archivos/Productos.txt') as file:
            renglones = file.readlines()
        for renglon in renglones:
            codigo, nombre, talla, precio = renglon.strip().split(',')
            producto = Producto(codigo, nombre, talla, precio)
            self.listas_productos.append(producto)
    #endregion

    #region Producto
    def agregar_Producto(self):
        nombre, talla, precio = self.vista.agregarProductos()
        codigo = self.ultimo_Codigo(self.listas_productos)
        producto = Producto(codigo, nombre, talla, precio)
        self.listas_productos.append(producto)
        with open("Archivos/Productos.txt", "w") as file:
            for producto in self.listas_productos:
                file.write(f"{producto}\n")
    def modificar_Producto(self):
        pass
    def eliminar_Producto(self):
        pass
    #endregion
    
    #region Menu Principal
    def inicializar(self):
        self.cargar_Datos()
        self.limpiar_Consola()
        opcion_Menu = 1
        while opcion_Menu != 0:
            opcion_Menu = self.vista.mostrarMenuPrincipal()
            self.limpiar_Consola()
            try:
                opcion_Menu = int(opcion_Menu)
                if opcion_Menu == 1:
                    self.limpiar_Consola()
                    opcion_Menu_Producto = 1
                    while opcion_Menu_Producto != 0:
                        opcion_Menu_Producto = self.vista.mostrarMenuProducto()
                        try:
                            opcion_Menu_Producto = int(opcion_Menu_Producto)
                            if opcion_Menu_Producto == 1:
                                self.limpiar_Consola()
                                self.vista.listarProducto(self.listas_productos)
                            elif opcion_Menu_Producto == 2:
                                self.limpiar_Consola()
                                self.agregar_Producto()
                            else:
                                self.limpiar_Consola()
                                self.vista.isSucess(False)
                        except:
                            self.vista.isSucess(False)
                elif opcion_Menu == 0:
                    pass
                else:
                    self.limpiar_Consola()
                    self.vista.isSucess(False)
            except:
                self.vista.isSucess(False)
    #endregion