from tkinter import messagebox
import tkinter as tk
import sqlite3

def quitar(self):
    global ventana_quitar
    ventana_quitar = tk.Toplevel(self.root)
    ventana_quitar.title("Quitar Producto")
    # Obtener opciones disponibles en la base de datos
    opciones_disponibles = obtener_opciones_base_datos()

        # Crear entry widget y etiqueta
    tk.Label(ventana_quitar, text="Seleccione el producto a quitar:").pack()
    producto_a_quitar_var = tk.StringVar(ventana_quitar)
    producto_a_quitar_var.set(opciones_disponibles[0] if opciones_disponibles else "")  # Establecer el valor predeterminado

    dropdown = tk.OptionMenu(ventana_quitar, producto_a_quitar_var, *opciones_disponibles)
    dropdown.pack()
    # Botón para quitar el producto
    tk.Button(ventana_quitar, text="Quitar Producto", command=lambda: quitar_producto(producto_a_quitar_var.get())).pack()

from tkinter import messagebox
import sqlite3

def obtener_opciones_base_datos():
    try:
        # Conectar a la base de datos (o crearla si no existe)
        conn = sqlite3.connect('base_datos_biomagnetismo.db')
        cursor = conn.cursor()

        # Obtener los productos de la base de datos donde bool = 1
        cursor.execute('SELECT producto FROM Productos WHERE bool = 1')
        opciones = [row[0] for row in cursor.fetchall()]

        # Cerrar la conexión
        conn.close()

        return opciones
    except Exception as e:
        messagebox.showerror("Error", f"Error al obtener opciones desde la base de datos: {str(e)}")
        return []

# Ejemplo de uso:
opciones_disponibles = obtener_opciones_base_datos()


def quitar_producto(producto_a_quitar_var):
        # Verificar si el producto existe en la base de datos
    if producto_a_quitar_var in obtener_opciones_base_datos():
        try:
            # Aquí puedes agregar la lógica para cambiar el valor de la columna bool a 0
            conn = sqlite3.connect('base_datos_biomagnetismo.db')
            cursor = conn.cursor()

            # Ejecutar la sentencia SQL UPDATE
            cursor.execute('UPDATE Productos SET bool = 0 WHERE producto = ?', (producto_a_quitar_var,))

            # Commit y cerrar la conexión
            conn.commit()
            conn.close()
            messagebox.showinfo("Éxito", f"{producto_a_quitar_var} se ha eliminado con éxito.")
            ventana_quitar.destroy()
        except Exception as e:
            messagebox.showerror("Error", f"Error al actualizar el producto en la base de datos: {str(e)}")
    else:
        messagebox.showerror("Error", "El producto no existe en la base de datos.")
