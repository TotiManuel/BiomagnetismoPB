import sqlite3
import tkinter as tk

# Crear una función para mostrar la ventana secundaria
def lista(self):
    # Crear una ventana secundaria
    ventana = tk.Toplevel(self.root)

    # Crear un widget de texto
    texto = tk.Text(ventana)
    texto.pack()

    # Conectarse a la base de datos
    conn = sqlite3.connect('base_datos_biomagnetismo.db')

    # Crear un cursor
    cursor = conn.cursor()

    # Ejecutar una consulta SQL
    cursor.execute("SELECT producto, stock, talle, ventas, reembolsos FROM Productos WHERE bool == 1")
    productos = cursor.fetchall()

    # Imprimir los resultados en el widget de texto
    for row in productos:
        texto.insert(tk.END, "Nombre del Producto: " + row[0] + "\n")
        texto.insert(tk.END, "Cantidad: " + str(row[1]) + "\n")
        if (row[2] == None):
            texto.insert(tk.END, "Talle: Universal\n")
        else:
            texto.insert(tk.END, "Talle: " + row[2] + "\n")
        texto.insert(tk.END, "Ventas: " + str(row[3]) + "\n")
        texto.insert(tk.END, "Reembolsos: " + str(row[4]) + "\n")
        texto.insert(tk.END, "-------------------------------------------\n")

    # Cerrar la conexión
    conn.close()

    # Agregar un botón para salir
    boton_salir = tk.Button(ventana, text="Salir", command=ventana.destroy)
    boton_salir.pack()
