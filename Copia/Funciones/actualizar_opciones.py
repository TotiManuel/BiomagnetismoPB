import tkinter as tk
from tkinter import messagebox
import sqlite3

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

def actualizar_opciones(widget, variable, default_value="Sin opciones"):
    respuesta = messagebox.askyesno("Deseas Recargar?", "Deseas Recargar?")
    if respuesta:
        try:
            nuevas_opciones = obtener_opciones_base_datos()
            variable.set(nuevas_opciones[0] if nuevas_opciones else default_value)

            # Limpiar el widget actual
            menu = widget['menu']
            menu.delete(0, 'end')

            # Agregar las nuevas opciones al widget
            for opcion in nuevas_opciones:
                menu.add_command(label=opcion, command=lambda value=opcion: variable.set(value))

            messagebox.showinfo("Éxito", "Opciones actualizadas con éxito.")
        except Exception as e:
            messagebox.showerror("Error", f"Error al actualizar opciones: {str(e)}")
    else:
        pass