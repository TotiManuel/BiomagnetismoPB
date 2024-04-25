import sqlite3
import tkinter as tk

# Función para actualizar la lista
def actualizar_lista(event):
    # Obtener el texto del entry
    producto = buscador_producto.get()
    
    # Limpiar el widget de texto
    texto.delete('1.0', tk.END)

    # Conectarse a la base de datos
    conn = sqlite3.connect('base_datos_biomagnetismo.db')
    cursor = conn.cursor()

    # Ejecutar una consulta SQL con filtro por precio
    global productos
    cursor.execute("SELECT producto, stock, talle, ventas, reembolsos FROM Productos WHERE bool == 1 AND producto IN (?)", (producto,))
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
    
    if producto == "":
        cursor.execute("SELECT producto, stock, talle, ventas, reembolsos FROM Productos WHERE bool == 1")
        productos = cursor.fetchall()
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
    
# Crear una función para mostrar la ventana secundaria
def lista(self):
    # Crear una ventana secundaria
    ventana = tk.Toplevel(self.root)
    
    global buscador_producto
    buscador_producto = tk.Entry(ventana)
    buscador_producto.pack()
    # Vincular la función actualizar_lista al evento de modificación del entry
    buscador_producto.bind("<KeyRelease>", actualizar_lista)
    
    # Crear un widget de texto
    global texto
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

