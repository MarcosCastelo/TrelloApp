class Quadro:
    def __init__(self, nome):
        self.nome = nome
        if nome == "":
            self.nome = "Quadro"
        self.listas = list()


    def getNome(self):
        return self.nome


    def temLista(self, lista):
        if lista in self.listas:
            return True

        return False


    def inserirLista(self, lista):
        self.listas.append(lista)

    def inserirListaP(self,lista,posicao):
        if len(self.listas) >= posicao:
            self.inserirLista(lista)
            for i in range(posicao,len(self.listas)-1):
                self.listas[i+1] = self.listas[i]

            self.listas[posicao] = lista
            return True
        return False

    def removerLista(self, lista):
        if self.temLista(lista):
            self.listas.remove(lista)
            return True

        return False

    def removerListaTitulo(self, titulo_lista):
        lista = self.getLista(titulo_lista)
        if lista:
            return self.removerLista(lista)
        else:
            return False


    def moverLista(self, lista, index):
        if temLista(lista):
            index_inicial = self.listas.index(lista)
            temp_lista = self.listas[index]
            self.listas[index] = lista
            self.listas[index_inicial] = temp_lista
            return True

        return False


    def getListas(self):
        return self.listas


    def getListasTitulo(self):
        titulos_listas = []
        for lista in self.getListas():
            titulos_listas.append(lista.getTitulo())

        return titulos_listas


    def getLista(self, index):
        self.getListas()[index]


    def getLista(self, titulo):
        for lista in self.getListas():
            if lista.getTitulo() == titulo:
                return lista

    def moverCartao(self, cartao, destino):
        origem.removerCartao(cartao)
        destino.adicionarCartao(cartao)
