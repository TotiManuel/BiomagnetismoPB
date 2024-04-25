import sqlite3
import os
from tkinter import messagebox

def main():
	pass

class DataBase:
	def __init__(self):
		pass
	def CreateDataBase(self):
		if os.path.exists("base_datos_biomagnetismo.db") != True:
			conexion = sqlite3.connect('base_datos_biomagnetismo.db')
			cursor = conexion.cursor()
			cursor.execute('''
			CREATE TABLE IF NOT EXISTS Products (
			id INTEGER PRIMARY KEY,
			bool INTEGER,
			product TEXT,
			value REAL,
			stock INTEGER,
			sell INTEGER,
			refund INTEGER,
			size TEXT
			)
			''')
			conexion.commit()
			conexion.close()
			messagebox.showerror("Creado Con Exito", "Base de datos Creada.")
		else:
			messagebox.showerror("EXISTE", "Base de datos ya existe.")
	def AddProduct(self, ProductName, Value, Stock, Size):
		try:
			conexion = sqlite3.connect('base_datos_biomagnetismo.db')
			cursor = conexion.cursor()
			cursor.execute("INSERT INTO Products (bool, product, value, stock, sell, refund, size) VALUES (?,?,?,?,?,?,?)", (1, ProductName, Value, Stock, 0, 0,  Size))
			conexion.commit()
			conexion.close()
			messagebox.showerror("Producto Agregado", "Producto Agregado Correctamente.")
		except sqlite3.Error as error:
			messagebox.showerror("ERROR", "Error al agregar el producto.")
	def DoSell(self, Amount):
		try:
			conexion = sqlite3.connect('base_datos_biomagnetismo.db')
			cursor = conexion.cursor()
			#Actualizar Stock y Refund
			cursor.execute("SELECT stock FROM Products WHERE product=?", (self.ProductName,))
			Amount_Stock = cursor.fetchall()
			if Amount_Stock is not None and Amount_Stock[0][0]> 0:
				cursor.execute("UPDATE Products SET stock=stock-?, sell=sell+? WHERE product=?", (Amount, Amount, self.ProductName))
				messagebox.showerror("Venta Realizada", "Venta realizada con exito.")
			else:
				messagebox.showerror(f"Error", "No tiene mas productos en Stock.\nStock: " + str(Amount_Stock[0][0]))
			conexion.commit()
			conexion.close()
		except sqlite3.Error as error:
			print("Error con venta", error)
	def DoRefund(self, Amount):
		try:
			conexion = sqlite3.connect('base_datos_biomagnetismo.db')
			cursor = conexion.cursor()
			#Actualizar Stock y Refund
			cursor.execute("UPDATE Products SET stock=stock+?, refund=refund+? WHERE product=?", (Amount, Amount, self.ProductName))
			conexion.commit()
			conexion.close()
			print("Reembolso Actualizado")
		except sqlite3.Error as error:
			print("Error con reembolso", error)
	def GetAllOptions(self):
		try:
			conexion = sqlite3.connect('base_datos_biomagnetismo.db')
			cursor = conexion.cursor()
			cursor.execute("SELECT product FROM Products")
			products = cursor.fetchall()
			product = [product[0] for product in products]
			return(products)
		except sqlite3.Error as error:
			print("Error ", error)
	def GetOptions(self, ProductName):
		try:
			conexion = sqlite3.connect('base_datos_biomagnetismo.db')
			cursor = conexion.cursor()
			# Buscar por nombre
			cursor.execute("SELECT * FROM Products WHERE product LIKE ?",('%' + ProductName + '%',))
			Product_Found = cursor.fetchall()
			if Product_Found:
				print("Productos Encontrados")
				for product in Product_Found:
					print(f"ID: {product[0]}, Producto: {product[2]}, Valor: {product[3]}, Stock: {product[4]}, Ventas: {product[5]}, Reembolsos: {product[6]}, Talla: {product[7]}")
				print("Ventas sin tomar en cuenta los reembolsos: ", product[5] - product[6])
			else:
				print("Error al intentar encontrar el producto")
			conexion.close()
		except sqlite3.Error as error:
			print("Error al intentar buscar el producto:", error)
if __name__=="__main__":
	main()
	'''
	BD = DataBase()
	BD.CreateDataBase()
	BD.AddProduct("P", 5, 100, "M")
	BD.GetAllOptions()
	BD.DoSell(1)
	BD.GetOptions("Product")
	BD.DoRefund(1)
	BD.GetOptions("Product")
	'''
