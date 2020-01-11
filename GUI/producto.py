import datetime
import time

class Producto():
	def __init__(self, codigo, cantidad):
		self.codigo = codigo
		self.cantidad = cantidad
		
		

	def define_fechas(self):
		self.fechaIng = datetime.date.fromtimestamp(time.time())
		self.fechaCad = self.fechaIng + datetime.timedelta(days=30)
		print('Fecha de Ingreso: ',self.fechaIng, '\nFecha de Caducidad: ', self.fechaCad)

	def asignar_Codigo(self):
		if self.codigo=='1':
			self.nombre = "Producto 1"
		elif self.codigo=='2':
			self.nombre = "Producto 2"
		elif self.codigo=='3':
			self.nombre = "Producto 3"
		else:
			self.nombre = "null"
			print("no existe el producto")

		print(self.nombre)

	def asignar_lugar(self):
		print('Cantidad: ',self.cantidad)

#prod1 = Producto('3',5)
#prod1.asignar_Codigo()
#print(prod1.nombre)


		




