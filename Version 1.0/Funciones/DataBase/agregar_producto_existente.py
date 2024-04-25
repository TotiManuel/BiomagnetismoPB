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
            toplevel.destroy()

        except ValueError:
            messagebox.showerror("Error", "Ingrese una cantidad válida.")
    else:
        messagebox.showerror("Error", "Complete todos los campos.")

def agregar_producto_funcion_Existe():
    global toplevel
    toplevel = tk.Tk()
    toplevel.title("Agregar Venta")
    toplevel.geometry("400x150+0+0")

     # Etiqueta y entrada para el monto de la venta
    label_producto = tk.Label(toplevel, text="Selecciona el producto:")
    label_producto.pack()
    
    try:
        productos = opciones_base_de_datos.obtener_opciones()
    except:
        messagebox.showerror("Ajustes", "Por Favor Crea una Base de Datos.")
        return

    try:
        producto_seleccionado = tk.StringVar()
        producto_seleccionado.set(productos[0] if productos else "Sin opciones")
        dropdown_producto = tk.OptionMenu(toplevel, producto_seleccionado, *productos)
        dropdown_producto.pack()
    except:
        messagebox.showerror("Ajustes", "Por Favor Crea una Base de Datos.")
        return

    label_cantidad = tk.Label(toplevel, text="Cantidad:")
    label_cantidad.pack()

    entry_cantidad = tk.Entry(toplevel)
    entry_cantidad.pack()

    # Botones para agregar producto
    boton_venta = tk.Button(toplevel, text="Agregar Producto", command=lambda: agregar_producto_funcion_Existente(entry_cantidad.get(), producto_seleccionado.get()))
    boton_venta.pack()
