class Client:
	def __init__(self, NameClient, AgeClient, Adress, Contact):
		self.NameClient = NameClient
		self.AgeClient = AgeClient
		self.Adress = Adress
		self.Contact = Contact
		self.state = True
	def AddClient(self):
		pass
	def ModClient(self):
		pass
	def HideClient(self):
		self.state = False
	def Record(self):
		pass
	def __str__(self):
		return ("Esta Clase se encarga de la administracion de los servicios.\nRecibe como parametros: el nombre del servicio y  el monto del servicio.")
def main():
	pass
if __name__=="__main__":
	main()
