import tkinter as tk
from tkinter import ttk
from Class import ClassProducts
def buscar_productos():
	Products_All = []
	devolver = []
	with open ("./Version 1.1\Productos.txt") as products:
		productsTupla = products.readlines()
		for i in productsTupla:
			linea = i.strip().split(",")
			if linea[0] != "PRODUCTO":
				crearproduct = ClassProducts.Products(NameProduct=linea[0], ValueProduct=linea[1], Size=linea[2], Stock=linea[3])
				Products_All.append(crearproduct)
		for i in Products_All:
			devolver.append(i.NameProduct)
	return devolver
def buscar_precio_productos(producto):
	valor = int(spinbox_Amount.get())
	with open ("./Version 1.1\Productos.txt") as products:
		productsTupla = products.readlines()
		for i in productsTupla:
			linea = i.strip().split(",")
			if linea[0] != "PRODUCTO":
				if linea[0] == producto:
					price = float(linea[1])*valor
					return price
def buscar_talla_productos(producto):
	valor = int(spinbox_Amount.get())
	with open ("./Version 1.1\Productos.txt") as products:
		productsTupla = products.readlines()
		for i in productsTupla:
			linea = i.strip().split(",")
			if linea[0] != "PRODUCTO":
				if linea[0] == producto:
					price = float(linea[2])*valor
					return price
def validar_input(*args):
	ProductExact = buscar_productos()
	for i in ProductExact:
		valor = float(spinbox_Amount.get())
		if i == combobox_product.get() and valor > 0:
			thePrice = buscar_precio_productos(i)
			entry_price.config(state="normal")
			entry_price.delete(0, tk.END)
			entry_price.insert(tk.END, "$" + str(thePrice))
			entry_price.config(state="readonly")
def cobrar_venta():
	producto = combobox_product.get()
	cantidad = spinbox_Amount.get()
	precio = entry_price.get()
	print(f" el cliente compro {cantidad} {producto}/s por {precio}")
     
def main():
	global combobox_product, spinbox_Amount, entry_price, SizeExact
	rootSell = tk.Tk()
	rootSell.title("Registro de Ventas")
	rootSell.geometry("800x600+0+0")
	label_products = tk.Label(rootSell, text="Producto:")
	label_products.place(relx=0.01, rely=0.1)
	ProductExact = buscar_productos()
	combobox_product = ttk.Combobox(rootSell, values=ProductExact)
	combobox_product.place(relx=0.09, rely=0.1)
	combobox_product.set(ProductExact[0])
	label_size = tk.Label(rootSell, text="Talla:")
	label_size.place(relx=0.1, rely=0.1)
	SizeExact = buscar_talla_productos()
	combobox_product = ttk.Combobox(rootSell, values=ProductExact)
	combobox_product.place(relx=0.1, rely=0.1)
	combobox_product.set(ProductExact[0])
	combobox_product.bind("<<ComboboxSelected>>", validar_input)
	label_amount = tk.Label(rootSell, text="Cantidad:")
	label_amount.place(relx=0.01, rely=0.15)
	spinbox_Amount = tk.Spinbox(rootSell, from_=1, to=100)
	spinbox_Amount.place(relx=0.09, rely=0.15)
	label_price = tk.Label(rootSell, text="Precio:")
	label_price.place(relx=0.01, rely=0.20)
	entry_price = tk.Entry(rootSell)
	entry_price.config(state="readonly")
	entry_price.place(relx=0.09 , rely=0.20, relwidth=0.17)
	label_client = tk.Label(rootSell, text="Cliente:")
	label_client.place(relx=0.01, rely=0.25)
	button_sell = tk.Button(rootSell, text="Vender", command=cobrar_venta)
	button_sell.place(relx=0.01, rely=0.30)
	rootSell.mainloop()

if __name__=="__main__":
    main()