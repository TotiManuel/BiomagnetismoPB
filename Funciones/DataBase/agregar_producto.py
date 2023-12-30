import tkinter as tk
from tkinter import messagebox
import sqlite3

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
            else:
                messagebox.showerror("Error", "El producto ya existe en la base de datos, Debes Actualizar.")
        except ValueError:
            messagebox.showerror("Error", "Ingrese un precio y stock válidos.")
    else:
        messagebox.showerror("Error", "Complete todos los campos.")

def agregar_producto(self):
    global ventana_agregar_producto
    ventana_agregar_producto = tk.Toplevel(self.root)
    ventana_agregar_producto.title("Porcentaje de Ganancias y Pérdidas")
    ventana_agregar_producto.geometry("200x200")
    
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
