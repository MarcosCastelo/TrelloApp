from model.Quadro import Quadro
from model.Cartao import Cartao
from model.Lista import Lista
from model.Etiqueta import Etiqueta
from model.Comentario import Comentario

class Service:
    def __init__(self):
        self.quadros = []
        self.quadro_atual = None
        self.lista_atual = None
        self.cartao_atual = None


    def criarQuadro(self, nome_quadro):
        quadro = Quadro(nome_quadro)
        self.quadros.append(quadro)
        self.quadro_atual = quadro

    def removerQuadro(self, nome_quadro):
        try:
            self.quadros.remove(self.selecionarQuadro(nome_quadro))
            return True
        except:
            return False


    def listarQuadros(self):
        lista_quadros = []
        for quadro in self.quadros:
            lista_quadros.append(quadro.getNome())

        return lista_quadros


    def listarListas(self):
        return self.quadro_atual.getListasTitulo()


    def criarLista(self, titulo_lista):
        if self.quadro_atual:
            lista = Lista(titulo_lista)
            self.quadro_atual.inserirLista(lista)
            self.lista_atual = lista

    def removerLista(self, titulo_lista):
        if self.quadro_atual:
            self.quadro_atual.removerListaTitulo(titulo_lista)


    def criarCartao(self, titulo_cartao):
        if self.lista_atual:
            cartao = Cartao(titulo_cartao)
            self.lista_atual.adicionarCartao(cartao)
            self.cartao_atual = cartao


    def selecionarQuadro(self, nome_quadro):
        for quadro in self.quadros:
            if quadro.getNome() == nome_quadro:
                self.quadro_atual = quadro
                return quadro

        return None


    def selecionarLista(self, titulo_lista):
        self.lista_atual = None
        if self.quadro_atual:
            self.lista_atual = self.quadro_atual.getLista(titulo_lista)
            if self.lista_atual:
                return self.lista_atual

        return None


    def selecionarCartao(self, titulo_cartao):
        self.cartao_atual = None
        if self.lista_atual:
            self.cartao_atual = self.lista_atual.getCartao(titulo_cartao)
            if self.cartao_atual:
                return cartao_atual
        else:
            return None


    def adicionarEtiqueta(self, cor, titulo):
        etiqueta = Etiqueta(cor, titulo)
        self.cartao_atual.adicionarEtiqueta(etiqueta)


    def adicionarComentario(self, nome, comentario):
        comentario = Comentario(nome,comentario)
        self.cartao_atual.adicionarComentario(comentario)


    def moverLista(self, titulo_lista, destino, posicao):
        lista = self.selecionarLista(titulo_lista)
        destino = self.selecionarQuadro(destino)
        self.removerLista(titulo_lista)
        return destino.inserirListaP(lista, posicao)