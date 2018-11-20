class Etiqueta:
	def __init__(self, cor, titulo):
		self.cor = cor
		self.titulo = titulo


	def alterarTitulo(self, novo_titulo):
		self.titulo = novo_titulo


	def getTitulo(self):
		return self.titulo