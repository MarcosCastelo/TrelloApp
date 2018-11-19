from model.Text import *

class Cartao:
    def __init__(self, titulo):
        self.titulo = titulo
        self.descricao = Text()
        self.log = list
        self.arquivado = False


    def getTitulo(self):
        return self.titulo


    def __repr__(self):
        return self.getTitulo()