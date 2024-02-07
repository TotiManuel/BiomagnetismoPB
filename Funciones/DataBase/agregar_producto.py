import tkinter as tk
from tkinter import messagebox
import sqlite3
from Funciones.DataBase import opciones_base_de_datos

def producto_existe(nombre_producto):
    conn = sqlite3.connect('base_datos_biomagnetismo.db')
    cursor = conn.cursor()
    cursor.execute('SELECT COUNT(*) FROM Productos WHERE producto = ?', (nombre_producto,))
    count = cursor.fetchone()[0]
    conn.close()
    return count > 0

def agregar_producto_funcion():
    nombre_producto = entry_nombre.get()
    precio_producto = entry_precio.get()
    stock_producto = entry_stock.get()
    talle = entry_talle.get()

    if nombre_producto and precio_producto and stock_producto:
        try:
            precio_producto = float(precio_producto)
            stock_producto = int(stock_producto)

            if not producto_existe(nombre_producto):
                conn = sqlite3.connect('base_datos_biomagnetismo.db')
                cursor = conn.cursor()
                cursor.execute('INSERT INTO Productos (bool, producto, valor, stock, ventas, reembolsos, talle) VALUES (?,?, ?, ?, ?, ?, ?)',
                               (1, nombre_producto, precio_producto, stock_producto,0,0, talle))
                conn.commit()
                conn.close()
                messagebox.showinfo("Éxito", f"Producto {nombre_producto} agregado con éxito.")
                ventana_agregar_producto.destroy()  # Cerrar la ventana Toplevel después de agregar el producto
            elif nombre_producto:
                if not talle:
                    conn = sqlite3.connect('base_datos_biomagnetismo.db')
                    cursor = conn.cursor()
                    cursor.execute('INSERT INTO Productos (bool, producto, valor, stock, ventas, reembolsos, talle) VALUES (?,?, ?, ?, ?, ?, ?)',
                               (1, nombre_producto, precio_producto, stock_producto,0,0, talle))
                    conn.commit()
                    conn.close()
                    messagebox.showinfo("Éxito", f"Producto {nombre_producto} agregado con éxito.")
                    ventana_agregar_producto.destroy()  # Cerrar la ventana Toplevel después de agregar el producto
                else:
                    messagebox.showerror("Error", "El producto ya existe en la base de datos, Debes Actualizar.")
            else:
                messagebox.showerror("Error", "El producto ya existe en la base de datos, Debes Actualizar.")
        except ValueError:
            messagebox.showerror("Error", "Ingrese un precio y stock válidos.")
    else:
        messagebox.showerror("Error", "Complete todos los campos.")

def agregar_producto_funcion_Existente(cantidad, nombre_producto):
    if nombre_producto and cantidad:
        try:
            cantidad = int(cantidad)

            conn = sqlite3.connect('base_datos_biomagnetismo.db')
            cursor = conn.cursor()

            # Buscar el producto existente en la base de datos
            cursor.execute('SELECT stock FROM Productos WHERE producto = ?', (nombre_producto,))
            stock_actual = cursor.fetchone()[0]

            # Actualizar la cantidad del producto existente
            cursor.execute('UPDATE Productos SET stock = ? WHERE producto = ?', (stock_actual + cantidad, nombre_producto))
            conn.commit()
            conn.close()

            messagebox.showinfo("Éxito", f"Se agregaron {cantidad} unidades al producto {nombre_producto}.")
            ventana_agregar_producto.destroy()
            toplevel.destroy()

        except ValueError:
            messagebox.showerror("Error", "Ingrese una cantidad válida.")
    else:
        messagebox.showerror("Error", "Complete todos los campos.")
        
def agregar_producto_funcion_Existe():
    global toplevel
    toplevel = tk.Toplevel(ventana_agregar_producto)
    toplevel.title("Agregar Venta")

     # Etiqueta y entrada para el monto de la venta
    label_producto = tk.Label(toplevel, text="Selecciona el producto:")
    label_producto.grid(row=0, column=0, padx=10, pady=10)
    
    try:
        productos = opciones_base_de_datos.obtener_opciones()
    except:
        messagebox.showerror("Ajustes", "Por Favor Crea una Base de Datos.")
        return

    try:
        producto_seleccionado = tk.StringVar()
        producto_seleccionado.set(productos[0] if productos else "Sin opciones")
        dropdown_producto = tk.OptionMenu(toplevel, producto_seleccionado, *productos)
        dropdown_producto.grid(row=0, column=1, padx=10, pady=10)
    except:
        messagebox.showerror("Ajustes", "Por Favor Crea una Base de Datos.")
        return

    label_cantidad = tk.Label(toplevel, text="Cantidad:")
    label_cantidad.grid(row=1, column=0, padx=10, pady=10)

    entry_cantidad = tk.Entry(toplevel)
    entry_cantidad.grid(row=1, column=1, padx=10, pady=10)

    # Botones para agregar producto
    boton_venta = tk.Button(toplevel, text="Agregar Producto", command=lambda: agregar_producto_funcion_Existente(entry_cantidad.get(), producto_seleccionado.get()))
    boton_venta.grid(row=2, column=0, columnspan=2, pady=10)

def agregar_producto(self):
    global ventana_agregar_producto
    ventana_agregar_producto = tk.Toplevel(self.root)
    ventana_agregar_producto.title("Agregar Producto")
    ventana_agregar_producto.geometry("200x225+0+0")
    
    # Crear entry widgets y etiquetas
    tk.Label(ventana_agregar_producto, text="Nombre del Producto:").pack()
    global entry_nombre
    entry_nombre = tk.Entry(ventana_agregar_producto)
    entry_nombre.pack()

    tk.Label(ventana_agregar_producto, text="Precio del Producto:").pack()
    global entry_precio
    entry_precio = tk.Entry(ventana_agregar_producto)
    entry_precio.pack()

    tk.Label(ventana_agregar_producto, text="Stock del Producto:").pack()
    global entry_stock
    entry_stock = tk.Entry(ventana_agregar_producto)
    entry_stock.pack()
    
    tk.Label(ventana_agregar_producto, text="Talle del Producto:").pack()
    global entry_talle
    entry_talle = tk.Entry(ventana_agregar_producto)
    entry_talle.pack()

    # Botón para agregar el producto
    tk.Button(ventana_agregar_producto, text="Agregar Producto", command=agregar_producto_funcion).pack()
    tk.Button(ventana_agregar_producto, text="Agregar Producto Existente", command=agregar_producto_funcion_Existe).pack()
