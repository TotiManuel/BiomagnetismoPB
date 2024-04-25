import tkinter as tk
from tkinter import messagebox
import sqlite3
from Funciones.DataBase import opciones_base_de_datos

def realizar_venta(cantidad, producto_seleccionado):
    try:
        cantidad = int(cantidad)
        # Obtener el stock actual del producto seleccionado
        stock_actual = obtener_stock_desde_bd(producto_seleccionado)

        if cantidad <= stock_actual:
            # Realizar la venta aquí (actualizar la base de datos, etc.)
            actualizar_stock_en_bd(producto_seleccionado, stock_actual - cantidad, cantidad)
            messagebox.showinfo("Éxito", "Venta realizada con éxito.")
            toplevel.destroy()
        else:
            messagebox.showerror("Error", "No hay suficiente stock para realizar la venta.")
    except ValueError:
        messagebox.showerror("Error", "Ingrese una cantidad válida.")

def obtener_stock_desde_bd(producto):
    try:
        conn = sqlite3.connect('base_datos_biomagnetismo.db')
        cursor = conn.cursor()
        cursor.execute('SELECT stock FROM Productos WHERE producto = ?', (producto,))
        resultado = cursor.fetchone()
        conn.close()
        return resultado[0] if resultado else 0
    except Exception as e:
        messagebox.showerror("Error", f"Error al obtener el stock desde la base de datos: {str(e)}")
        return 0

def actualizar_stock_en_bd(producto, stock, cantidad):
    try:
        conn = sqlite3.connect('base_datos_biomagnetismo.db')
        cursor = conn.cursor()

        # Obtener las ventas actuales del producto
        cursor.execute('SELECT ventas FROM Productos WHERE producto = ?', (producto,))
        resultado_ventas = cursor.fetchone()

        if resultado_ventas:
            ventas_actuales = resultado_ventas[0]
            nuevas_ventas = ventas_actuales + cantidad  # Sumar 1 a las ventas actuales

            # Actualizar las ventas en la base de datos
            cursor.execute('UPDATE Productos SET ventas = ? WHERE producto = ?', (nuevas_ventas, producto))
            conn.commit()
            messagebox.showinfo("Éxito", "Ventas actualizadas con éxito.")
        else:
            messagebox.showerror("Error", "Producto no encontrado en la base de datos.")

        # Obtener el stock actual del producto
        cursor.execute('SELECT stock FROM Productos WHERE producto = ?', (producto,))
        resultado = cursor.fetchone()

        if resultado:
            # Actualizar el stock en la base de datos
            cursor.execute('UPDATE Productos SET stock = ? WHERE producto = ?', (stock, producto))
            conn.commit()
        else:
            messagebox.showerror("Error", "Producto no encontrado en la base de datos.")
        conn.close()
    except Exception as e:
        messagebox.showerror("Error", f"Error al actualizar el stock en la base de datos: {str(e)}")


'''
def agregar_venta(self):
    global toplevel
    toplevel = tk.Toplevel(self.root)
    toplevel.title("Agregar Venta")
    toplevel.geometry("400x150+0+0")

    # Etiqueta y entrada para el monto de la venta
    label_producto = tk.Label(toplevel, text="Selecciona el producto:")
    label_producto.place(relx=0.01, rely=0.01, relwidth = 0.4, relheight = 0.23)
    
    try:
        productos = opciones_base_de_datos.obtener_opciones()
    except:
        messagebox.showerror("Ajustes", "Por Favor Crea una Base de Datos.")
        return

    try:
        producto_seleccionado = tk.StringVar()
        producto_seleccionado.set(productos[0] if productos else "Sin opciones")
        dropdown_producto = tk.OptionMenu(toplevel, producto_seleccionado, *productos)
        dropdown_producto.place(relx=0.5,rely=0.01, relwidth=0.5, relheight = 0.23)
    except:
        messagebox.showerror("Ajustes", "Por Favor Crea una Base de Datos.")
        return

    label_cantidad = tk.Label(toplevel, text="Cantidad:")
    label_cantidad.place(relx=0.01,rely=0.25, relwidth=0.4, relheight = 0.23)

    entry_cantidad = tk.Entry(toplevel)
    entry_cantidad.place(relx=0.5,rely=0.25, relwidth=0.4, relheight = 0.23)

    # Botones para agregar venta y reembolso
    boton_venta = tk.Button(toplevel, text="Realizar Venta", command=lambda: realizar_venta(entry_cantidad.get(),producto_seleccionado.get()))
    boton_venta.place(relx=0.01,rely=0.5, relwidth=0.98, relheight = 0.2)
'''