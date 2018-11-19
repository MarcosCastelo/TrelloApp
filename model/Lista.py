from model.Cartao import *

class Lista:
    def __init__(self, titulo):
        self.setTitulo(titulo)
        self.cartoes = list()


    def setTitulo(self, novo_titulo):
        self.titulo = novo_titulo


    def adicionarCartao(self, nome_Cartao):
        cartao = Cartao(nome_Cartao)
        self.cartoes.append(cartao)


    def getCartao(self, nome_Cartao):
        for c in self.cartoes:
            if c.getTitulo() == nome_Cartao:
                return c

        return False


    def arquivarCartao(self, nome_Cartao):
        cartao = self.getCartao(nome_Cartao)
        if cartao == False:
            return None
        else:
            index = self.cartoes.index(cartao)
            return self.cartoes.pop(index)