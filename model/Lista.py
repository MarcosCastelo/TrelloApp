from model.Cartao import *

class Lista:
    def __init__(self, titulo):
        self.setTitulo(titulo)
        self.cartoes = list()


    def getTitulo(self):
        return self.titulo


    def setTitulo(self, novo_titulo):
        self.titulo = novo_titulo


    def adicionaCartao(self, cartao):
        self.cartoes.append(cartao)


    def getCartao(self, nome_cartao):
        for c in self.cartoes:
            if c.getTitulo() == nome_cartao:
                return c

        return None


    def deletaCartao(self, nome_cartao):
        cartao = self.getCartao(nome_cartao)
        index = self.cartoes.index(cartao)
        return self.cartoes.pop(index)


    def arquivarCartao(self, nome_Cartao):
        self.getCartao(nome_Cartao).arquive()
