import tkinter as tk
from Class.Functions import agregar_base_de_datos

def agregardatabase():
	agregar_base_de_datos.agregar_database()

def prueba():
	print("prueba")

def main():
	root = tk.Tk()
	root.title("BioMagnetismo PB")
	root.geometry("500x500+0+0")
	# Barra de menú
	menu_bar = tk.Menu(root)
	root.config(menu=menu_bar)
	# Menú "Archivo"
	archivo_menu = tk.Menu(menu_bar, tearoff=0)
	menu_bar.add_cascade(label="Archivo", menu=archivo_menu)
	archivo_menu.add_command(label="Actualizar", command=prueba)
	archivo_menu.add_command(label="Salir", command=root.destroy)

	# Menú "Ajustes"
	Ajustes_menu = tk.Menu(menu_bar, tearoff=0)
	menu_bar.add_cascade(label="Ajustes", menu=Ajustes_menu)
	Ajustes_menu.add_command(label="Crear Base de Datos", command=agregardatabase)
	
	# Etiqueta y entrada para el monto de la venta
	label_producto = tk.Label(root, text="BIENVENIDA!! ")
	label_producto.place(relx=0.01, rely=0.01, relwidth = 0.3)

	# Botones para agregar venta y reembolso
	boton_agregar_venta = tk.Button(root, text="Agregar Venta", command=prueba)
	boton_agregar_venta.place(relx=0.01, rely=0.07, relwidth = 0.3)

	boton_reembolso = tk.Button(root, text="Reembolso", command=prueba)
	boton_reembolso.place(relx=0.01, rely=0.15, relwidth = 0.3)

	# Botón para mostrar el gráfico
	boton_mostrar_grafico = tk.Button(root, text="Mostrar Gráfico", command=prueba)
	boton_mostrar_grafico.place(relx=0.01, rely=0.23, relwidth = 0.3)
	
	# Botón para mostrar el stock
	boton_mostrar_grafico = tk.Button(root, text="Ver Stock", command=prueba)
	boton_mostrar_grafico.place(relx=0.01, rely=0.31, relwidth = 0.3)
	
	# Botón para Agregar Producto
	boton_agregar_producto = tk.Button(root, text="Agregar Producto", command=prueba)
	boton_agregar_producto.place(relx=0.01, rely=0.39, relwidth = 0.3)
	
	# Botón para Agregar Producto Existente
	boton_quitar_producto = tk.Button(root, text="Agregar Stock", command=prueba)
	boton_quitar_producto.place(relx=0.01, rely=0.47, relwidth = 0.3)
	
	# Botón para Quitar Producto
	boton_quitar_producto = tk.Button(root, text="Quitar Producto", command=prueba)
	boton_quitar_producto.place(relx=0.01, rely=0.55, relwidth = 0.3)
	
	# Botón para Turnero
	boton_turnero = tk.Button(root, text="Turnero", command=prueba)
	boton_turnero.place(relx=0.40, rely=0.07, relwidth = 0.3)
	
	# Botón para Listado de turnos
	boton_listado_turnos = tk.Button(root, text="Listado de Turnos", command=prueba)
	boton_listado_turnos.place(relx=0.40, rely=0.15, relwidth = 0.3)
	
	# Botón para Listado de Pacientes
	boton_listado_pacientes = tk.Button(root, text="Listado de Pacientes", command=prueba)
	boton_listado_pacientes.place(relx=0.40, rely=0.23, relwidth = 0.3)
	
	root.mainloop()
if __name__=="__main__":
	main()
