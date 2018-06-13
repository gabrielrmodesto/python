class Data(object):
	def __init__(self,data,mes,ano):
		self.data = data
		self.mes = mes
		self.ano = ano

	def imprime(self):
		print "%s/%s/%s" % (self.data,self.mes,self.ano)