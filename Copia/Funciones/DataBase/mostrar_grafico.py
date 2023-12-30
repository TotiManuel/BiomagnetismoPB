import tkinter as tk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt
from tkinter import messagebox
import sqlite3

def graficar(self):
    porcentaje_ganancias, porcentaje_perdidas = obtener_ganancias_y_perdidas_desde_bd(self)
    # Crear un gráfico de torta
    fig, ax = plt.subplots()
    ax.pie([porcentaje_ganancias, porcentaje_perdidas], labels=['Ganancias', 'Pérdidas'],
           autopct='%1.1f%%', startangle=90, colors=['green', 'red'])
    ax.axis('equal')  # Asegurar que el gráfico de torta sea circular

    # Mostrar el gráfico en una nueva ventana
    ventana_grafico = tk.Toplevel(self.root)
    ventana_grafico.title("Porcentaje de Ganancias y Pérdidas")

    canvas = FigureCanvasTkAgg(fig, master=ventana_grafico)
    canvas_widget = canvas.get_tk_widget()
    canvas_widget.pack()

def obtener_ganancias_y_perdidas_desde_bd(self):
    try:
        conn = sqlite3.connect('base_datos_biomagnetismo.db')
        cursor = conn.cursor()

            # Consultar las ventas y reembolsos desde la base de datos
        cursor.execute('SELECT SUM(ventas) FROM Productos')
        total_ventas = cursor.fetchone()[0] or 0

        cursor.execute('SELECT SUM(reembolsos) FROM Productos')
        total_reembolsos = cursor.fetchone()[0] or 0

        conn.close()

        ganancias_netas = total_ventas - total_reembolsos
        porcentaje_ganancias = (ganancias_netas / total_ventas) * 100 if total_ventas != 0 else 0
        porcentaje_perdidas = 100 - porcentaje_ganancias

        return porcentaje_ganancias, porcentaje_perdidas
    except Exception as e:
            messagebox.showerror("Error", f"Error al obtener las ganancias y pérdidas desde la base de datos: {str(e)}")
            return 0, 0