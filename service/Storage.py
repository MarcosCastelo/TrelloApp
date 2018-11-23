class Storage():
	def __init__(self):
		self.quadros = list()
		self.listas = list()
		self.cartoes = list()

	def buscaListas(self, nome_quadro):
		for lista in self.listas:
			if lista[0] == nome_quadro:
				return lista[1:]
		return None

	def inserirListas(self,nome_quadro,lista=[]):
		if buscaListas(nome_quadro) == None:
			self.listas.append(nome_quadro,lista)
