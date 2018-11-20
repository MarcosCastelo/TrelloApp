class Lista:
    def __init__(self, titulo):
        self.titulo = titulo
        self.cartoes = list()


    def temCartao(cartao):
        if cartao in self.cartoes:
            return True

        return False


    def adicionarCartao(self, cartao):
        self.cartoes.append(cartao)


    def removerCartao(self, cartao):
        if temCartao(cartao):
            self.cartoes.remove(cartao)


    def moverCartao(self, cartao, index):
        if temCartao(cartao):
            index_inicial = self.cartoes.index(cartao)
            temp_cartao = self.cartoes[index]
            self.cartoes[index] = cartao
            self.cartoes[index_inicial] = temp_cartao


    def getCartoes(self):
        return self.cartoes


    def getCartao(self, index):
        return self.getCartoes()[index]


    def getCartao(self, titulo_cartao):
        for cartao in self.cartoes:
            if cartao.getTitulo == titulo_cartao:
                return cartao

        