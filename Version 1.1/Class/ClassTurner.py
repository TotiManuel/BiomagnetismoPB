class Turner:
	def __init__(self, Date, Time, Patient, Service):
		self.Date = Date
		self.Time = Time
		self.Patient = Patient
		self.Service = Service
		self.state = True
	def AddTurner(self):
		pass
	def ModTurner(self):
		pass
	def ConfirmTurner(self):
		pass
	def HideTurner(self):
		self.state = False
	def Record(self):
		pass
	def __str__(self):
		return ("Esta Clase se encarga de la administracion de los servicios.\nRecibe como parametros: el nombre del servicio y  el monto del servicio.")
def main():
	pass
if __name__=="__main__":
	main()
