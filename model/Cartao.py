from model.Text import *

class Cartao:
    def __init__(self, titulo):
        self.titulo = titulo
        self.descricao = Text("")
        self.log = list()
        self.arquivado = False


    def getTitulo(self):
        return self.titulo


    def addLog(self, text):
        self.log.append(text)


    def arquive(self):
        self.arquivado = True


    def restaure(self):
        self.arquivado = False


    def setDescricao(self, text):
        self.descricao = text

