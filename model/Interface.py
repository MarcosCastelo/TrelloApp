from model.Quadro import Quadro
from model.Cartao import Cartao
from model.Lista import Lista

class Interface:
	def __init__(self):
		self.quadros = []
		self.quadro_atual = None


	def criarQuadro(self):
		quadro = Quadro()
		self.quadros.append(quadro)
		self.quadro_atual = quadro