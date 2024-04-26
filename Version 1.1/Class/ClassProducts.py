class Products:
	def __init__(self, NameProduct, ValueProduct, Size, Stock):
		self.NameProduct = NameProduct
		self.ValueProduct = ValueProduct
		self.Size = Size
		self.Stock = Stock
		self.vendido = 0
		self.reembolso = 0
	def Sell(self, amount, paymentMethod):
		self.Stock = self.Stock - amount
		print(f"Pago: {self.ValueProduct * amount} a traves de {paymentMethod}")
	def Refund(self, amount, paymentMethod):
		self.Stock = self.Stock + amount
		print(f"Se Devolvió: {self.ValueProduct * amount} a traves de {paymentMethod}")
	def SeeStock(self):
		print(f"Tienes {self.Stock} de {self.NameProduct}")
	def AddProduct(self):
		pass
	def AddStock(self, amount):
		self.Stock = self.Stock + amount
		print(f"Ahora tienes {self.Stock} de {self.NameProduct}")
	def HideProduct(self):
		self.state = False
	def __str__(self):
		return ("Esta Clase se encarga de la administracion de los productos.\nRecibe como parametros: el nombre del producto, la cantidad de stock, el monto del producto y el talle.")

def main():
	Producto1 = Products("caca", 500, "M", 5)
	print(Producto1.state)
	Producto1.Sell(2, "MercadoPago")
	Producto1.SeeStock()
	Producto1.AddStock(5)
	Producto1.HideProduct()
	print(Producto1.state)
if __name__=="__main__":
	main()
