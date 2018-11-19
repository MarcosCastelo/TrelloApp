from model.Lista import *

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
        cartao_movido = listaOrigem.arquivaCartao(nome_cartao)
        listaDestino.adicionaCartao(cartao_movido)

