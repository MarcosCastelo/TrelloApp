from model.Quadro import *
from model.Cartao import *
from model.Lista import *

class Interface:
    def __init__(self):
        self.quadros = []
        self.quadro_atual = None
        self.lista_atual = None
        self.cartao_atual = None


    def criarQuadro(self, nome_quadro):
        quadro = Quadro(nome_quadro)
        self.quadros.append(quadro)
        self.quadro_atual = quadro


    def listarQuadros(self):
        lista_quadros = []
        for quadro in self.quadros:
            lista_quadros.append(quadro.getNome())

        return lista_quadros


    def listarListas(self):
        return self.quadro_atual.getListas()


    def criarLista(self, titulo_lista):
        if self.quadro_atual:
            lista = Lista(titulo_lista)
            self.quadro_atual.inserirLista(lista)
            self.lista_atual = lista


    def criarCartao(self, titulo_cartao):
        if self.lista_atual:
            cartao = Cartao(titulo_cartao)
            self.lista_atual.adicionarCartao(cartao)
            self.cartao_atual = cartao


    def selecionarQuadro(self, nome_quadro):
        for quadro in self.quadros:
            if quadro.getNome() == nome_quadro:
                self.quadro_atual = quadro
                return quadro.getNome()

        return None


    def selecionarLista(self, titulo_lista):
        self.lista_atual = None
        if self.quadro_selecionado:
            self.lista_atual = self.quadro_atual.getLista(titulo_lista)
            if self.lista_atual:
                return True

        return False


    def selecionarCartao(self, titulo_cartao):
        self.cartao_atual = None
        if self.lista_atual:
            self.cartao_atual = self.lista_atual.getCartao(titulo_cartao)
            if self.cartao_atual:
                return True

        return False
