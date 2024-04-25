import tkinter as tk
from tkinter import messagebox, ttk
from Class import ClassDataBase

def AddDataBase():
	DataBase = ClassDataBase.DataBase()
	DataBase.CreateDataBase()

def AddSell():
	rootSell = tk.Tk()
	rootSell.title("Registro de Ventas")
	rootSell.geometry("800x600+0+0")
	label_products = tk.Label(rootSell, text="Producto:")
	label_products.place(relx=0.1, rely=0.1)
	label_amount = tk.Label(rootSell, text="Cantidad:")
	label_amount.place(relx=0.3, rely=0.1)
	label_price = tk.Label(rootSell, text="Precio:")
	label_price.place(relx=0.5, rely=0.1)
	label_client = tk.Label(rootSell, text="Cliente:")
	label_client.place(relx=0.7, rely=0.1)
	rootSell.mainloop()
def AddRefund():
	rootRefund = tk.Tk()
	rootRefund.title("Registro de Reembolsos")
	rootRefund.geometry("800x600+0+0")
	label_products = tk.Label(rootRefund, text="Producto:")
	label_products.place(relx=0.1, rely=0.1)
	label_amount = tk.Label(rootRefund, text="Cantidad:")
	label_amount.place(relx=0.3, rely=0.1)
	label_price = tk.Label(rootRefund, text="Precio:")
	label_price.place(relx=0.5, rely=0.1)
	label_client = tk.Label(rootRefund, text="Cliente:")
	label_client.place(relx=0.7, rely=0.1)
	rootRefund.mainloop()
def ViewStock():
	rootViewStock = tk.Tk()
	rootViewStock.title("Registro de Stock")
	rootViewStock.geometry("800x600+0+0")
	label_products = tk.Label(rootViewStock, text="Producto:")
	label_products.place(relx=0.1, rely=0.1)
	label_amount = tk.Label(rootViewStock, text="Cantidad:")
	label_amount.place(relx=0.3, rely=0.1)
	label_price = tk.Label(rootViewStock, text="Precio:")
	label_price.place(relx=0.5, rely=0.1)
	rootViewStock.mainloop()
def AddStock():
	rootAddProduct = tk.Tk()
	rootAddProduct.title("Registrar Stock")
	rootAddProduct.geometry("800x600+0+0")
	label_products = tk.Label(rootAddProduct, text="Producto:")
	label_products.place(relx=0.1, rely=0.1)
	label_amount = tk.Label(rootAddProduct, text="Cantidad:")
	label_amount.place(relx=0.1, rely=0.3)
	label_price = tk.Label(rootAddProduct, text="Precio:")
	label_price.place(relx=0.1, rely=0.5)
	label_client = tk.Label(rootAddProduct, text="Cliente:")
	label_client.place(relx=0.1, rely=0.7)
	products_list = ClassDataBase.DataBase()
	productslisted = products_list.GetAllOptions()
	combobox_product = ttk.Combobox(rootAddProduct, values=productslisted)
	combobox_product.place(relx=0.1, rely=0.2)
	spinbox_Amount = tk.Spinbox(rootAddProduct, from_=0, to=100)
	spinbox_Amount.place(relx=0.1, rely=0.4)
	rootAddProduct.mainloop()
def AddProduct():
	rootAddStock = tk.Tk()
	rootAddStock.title("Registrar Producto")
	rootAddStock.geometry("800x600+0+0")
	label_products = tk.Label(rootAddStock, text="Producto:")
	label_products.place(relx=0.1, rely=0.1)
	label_amount = tk.Label(rootAddStock, text="Cantidad:")
	label_amount.place(relx=0.3, rely=0.1)
	label_price = tk.Label(rootAddStock, text="Precio:")
	label_price.place(relx=0.5, rely=0.1)
	label_client = tk.Label(rootAddStock, text="Cliente:")
	label_client.place(relx=0.7, rely=0.1)
	rootAddStock.mainloop()
def HideProduct():
	rootHideProduct = tk.Tk()
	rootHideProduct.title("Eliminar Producto")
	rootHideProduct.geometry("800x600+0+0")
	label_products = tk.Label(rootHideProduct, text="Producto:")
	label_products.place(relx=0.1, rely=0.1)
	label_amount = tk.Label(rootHideProduct, text="Cantidad:")
	label_amount.place(relx=0.3, rely=0.1)
	label_price = tk.Label(rootHideProduct, text="Precio:")
	label_price.place(relx=0.5, rely=0.1)
	label_client = tk.Label(rootHideProduct, text="Cliente:")
	label_client.place(relx=0.7, rely=0.1)
	rootHideProduct.mainloop()
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
	Ajustes_menu.add_command(label="Crear Base de Datos", command=AddDataBase)
	
	# Etiqueta y entrada para el monto de la venta
	label_producto = tk.Label(root, text="BIENVENIDA!! ")
	label_producto.place(relx=0.01, rely=0.01, relwidth = 0.3)

	# Botones para agregar venta y reembolso
	boton_agregar_venta = tk.Button(root, text="Agregar Venta", command=AddSell)
	boton_agregar_venta.place(relx=0.01, rely=0.07, relwidth = 0.3)

	boton_reembolso = tk.Button(root, text="Reembolso", command=AddRefund)
	boton_reembolso.place(relx=0.01, rely=0.15, relwidth = 0.3)

	# Botón para mostrar el gráfico
	boton_mostrar_grafico = tk.Button(root, text="Mostrar Gráfico", command=prueba)
	boton_mostrar_grafico.place(relx=0.01, rely=0.23, relwidth = 0.3)
	
	# Botón para mostrar el stock
	boton_mostrar_grafico = tk.Button(root, text="Ver Stock", command=ViewStock)
	boton_mostrar_grafico.place(relx=0.01, rely=0.31, relwidth = 0.3)
	
	# Botón para Agregar Producto
	boton_agregar_producto = tk.Button(root, text="Agregar Producto", command=AddProduct)
	boton_agregar_producto.place(relx=0.01, rely=0.39, relwidth = 0.3)
	
	# Botón para Agregar Producto Existente
	boton_quitar_producto = tk.Button(root, text="Agregar Stock", command=AddStock)
	boton_quitar_producto.place(relx=0.01, rely=0.47, relwidth = 0.3)
	
	# Botón para Quitar Producto
	boton_quitar_producto = tk.Button(root, text="Quitar Producto", command=HideProduct)
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
