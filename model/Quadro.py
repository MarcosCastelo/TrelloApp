from model.Lista import *
from model.Text import *
from model.Cartao import *

class Quadro:
    def __init__(self, titulo):
        self.titulo = titulo
        self.listas = list()


    def getLista(self, titulo_lista):
        for l in self.listas:
            if l.getTitulo() == titulo_lista:
                return l

        return None



    def criaLista(self, tituloLista):
        lista = Lista(tituloLista)
        self.listas.append(lista)

    def moverCartao(self, nome_cartao, listaOrigem, listaDestino):
        cartao_movido = self.getLista(listaOrigem).deletaCartao(nome_cartao)
        text = Text("movido para a lista: " + listaDestino)
        cartao_movido.addLog(text)
        self.getLista(listaDestino).adicionaCartao(cartao_movido.getTitulo())
        print(text.texto)


    def getCartao(self, nome_cartao, titulo_lista):
        return self.getLista(titulo_lista).getCartao(nome_cartao)


    def criaCartao(self, titulo_lista, nome_cartao):
        cartao = Cartao(nome_cartao)
        self.getLista(titulo_lista).adicionaCartao(cartao)


